import torch
import torch.nn as nn
import torch.nn.functional as F
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from torchvision.transforms.functional import to_tensor, to_pil_image
from PIL import Image
import functools
import time

i = 0


# YOLO face detection code remains unchanged
def load_yolo_model(config_path, weights_path):
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    return net


def detect_faces_yolo(image, net, confidence_threshold=0.5):
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getLayerNames()
    try:
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    except IndexError:
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    layer_outputs = net.forward(output_layers)
    height, width = image.shape[:2]
    boxes = []
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_threshold:
                box = detection[0:4] * np.array([width, height, width, height])
                (centerX, centerY, w, h) = box.astype("int")
                x = int(centerX - (w / 2))
                y = int(centerY - (h / 2))
                boxes.append((x, y, x + w, y + h))
    return boxes


# Residual Dense Block definitions for ESRGAN remain unchanged
def make_layer(block, n_layers):
    layers = [block() for _ in range(n_layers)]
    return nn.Sequential(*layers)


class ResidualDenseBlock_5C(nn.Module):
    def __init__(self, nf=64, gc=32, bias=True):
        super(ResidualDenseBlock_5C, self).__init__()
        self.conv1 = nn.Conv2d(nf, gc, 3, 1, 1, bias=bias)
        self.conv2 = nn.Conv2d(nf + gc, gc, 3, 1, 1, bias=bias)
        self.conv3 = nn.Conv2d(nf + 2 * gc, gc, 3, 1, 1, bias=bias)
        self.conv4 = nn.Conv2d(nf + 3 * gc, gc, 3, 1, 1, bias=bias)
        self.conv5 = nn.Conv2d(nf + 4 * gc, nf, 3, 1, 1, bias=bias)
        self.lrelu = nn.LeakyReLU(negative_slope=0.2, inplace=True)

    def forward(self, x):
        x1 = self.lrelu(self.conv1(x))
        x2 = self.lrelu(self.conv2(torch.cat((x, x1), 1)))
        x3 = self.lrelu(self.conv3(torch.cat((x, x1, x2), 1)))
        x4 = self.lrelu(self.conv4(torch.cat((x, x1, x2, x3), 1)))
        x5 = self.conv5(torch.cat((x, x1, x2, x3, x4), 1))
        return x5 * 0.2 + x


class RRDB(nn.Module):
    def __init__(self, nf, gc=32):
        super(RRDB, self).__init__()
        self.RDB1 = ResidualDenseBlock_5C(nf, gc)
        self.RDB2 = ResidualDenseBlock_5C(nf, gc)
        self.RDB3 = ResidualDenseBlock_5C(nf, gc)

    def forward(self, x):
        out = self.RDB1(x)
        out = self.RDB2(out)
        out = self.RDB3(out)
        return out * 0.2 + x


class RRDBNet(nn.Module):
    def __init__(self, in_nc, out_nc, nf, nb, gc=32):
        super(RRDBNet, self).__init__()
        RRDB_block_f = functools.partial(RRDB, nf=nf, gc=gc)
        self.conv_first = nn.Conv2d(in_nc, nf, 3, 1, 1, bias=True)
        self.RRDB_trunk = make_layer(RRDB_block_f, nb)
        self.trunk_conv = nn.Conv2d(nf, nf, 3, 1, 1, bias=True)
        self.upconv1 = nn.Conv2d(nf, nf, 3, 1, 1, bias=True)
        self.upconv2 = nn.Conv2d(nf, nf, 3, 1, 1, bias=True)
        self.HRconv = nn.Conv2d(nf, nf, 3, 1, 1, bias=True)
        self.conv_last = nn.Conv2d(nf, out_nc, 3, 1, 1, bias=True)
        self.lrelu = nn.LeakyReLU(negative_slope=0.2, inplace=True)

    def forward(self, x):
        fea = self.conv_first(x)
        trunk = self.trunk_conv(self.RRDB_trunk(fea))
        fea = fea + trunk
        fea = self.lrelu(self.upconv1(F.interpolate(fea, scale_factor=2, mode='nearest')))
        fea = self.lrelu(self.upconv2(F.interpolate(fea, scale_factor=2, mode='nearest')))
        out = self.conv_last(self.lrelu(self.HRconv(fea)))
        return out


# Load ESRGAN model
def load_esrgan_model(model_path='model-weights/RRDB_PSNR_x4.pth'):
    model = RRDBNet(in_nc=3, out_nc=3, nf=64, nb=23)
    try:
        state_dict = torch.load(model_path, map_location=torch.device('cpu'))
        model.load_state_dict(state_dict)
    except FileNotFoundError:
        raise Exception(f"Model weights not found at {model_path}")
    model.eval()
    return model


# Function to enhance image with denoising, contrast enhancement, sharpening
def enhance_image(face_image):
    try:
        # Denoise
        denoised_image = cv2.fastNlMeansDenoisingColored(face_image, None, 10, 10, 7, 21)

        # Contrast enhancement (Histogram equalization)
        lab = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        l = cv2.equalizeHist(l)
        lab = cv2.merge((l, a, b))
        contrast_image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

        # Sharpening
        blurred = cv2.GaussianBlur(contrast_image, (5, 5), 1.0)
        sharpened_image = cv2.addWeighted(contrast_image, 1.5, blurred, -0.5, 0)

        return sharpened_image
    except Exception as e:
        print(f"Error enhancing image: {e}")
        return face_image


# Apply super-resolution using ESRGAN
def super_resolution(face_image, sr_model):
    try:
        face_pil = Image.fromarray(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))
        face_tensor = to_tensor(face_pil).unsqueeze(0)
        with torch.no_grad():
            sr_face_tensor = sr_model(face_tensor)
        sr_face_pil = to_pil_image(sr_face_tensor.squeeze(0).clamp(0, 1))
        sr_face_image = cv2.cvtColor(np.array(sr_face_pil), cv2.COLOR_RGB2BGR)
        return sr_face_image
    except Exception as e:
        print(f"Error in super-resolution: {e}")
        return face_image


# Load the frozen graph (.pb file)
def load_frozen_graph(pb_file_path):
    try:
        with tf.io.gfile.GFile(pb_file_path, "rb") as f:
            graph_def = tf.compat.v1.GraphDef()
            graph_def.ParseFromString(f.read())
        return graph_def
    except FileNotFoundError:
        raise Exception(f"Frozen graph not found at {pb_file_path}")


# Initialize the TensorFlow session and import the graph
frozen_graph = load_frozen_graph('model-weights/20180408-102900/20180408-102900.pb')

with tf.compat.v1.Session() as sess:
    tf.import_graph_def(frozen_graph, name="")
    input_tensor = sess.graph.get_tensor_by_name("input:0")
    output_tensor = sess.graph.get_tensor_by_name("embeddings:0")
    phase_train_tensor = sess.graph.get_tensor_by_name("phase_train:0")

    # Load the ESRGAN model
    sr_model = load_esrgan_model()


    def extract_face_embedding(face_image):
        try:
            face_image = enhance_image(face_image)
            face_image = super_resolution(face_image, sr_model)
            face_image = cv2.resize(face_image, (160, 160))
            face_image = face_image.astype('float32') / 255.0
            face_image = np.expand_dims(face_image, axis=0)
            embedding = sess.run(output_tensor, feed_dict={input_tensor: face_image, phase_train_tensor: False})
            return embedding.flatten()
        except Exception as e:
            print(f"Error in extracting face embedding: {e}")
            return None


    def match_face(known_embeddings, face_embedding):
        best_match = None
        highest_similarity = -1
        for name, embedding in known_embeddings.items():
            similarity = cosine_similarity([embedding], [face_embedding])[0][0]
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = name
        return best_match, highest_similarity


    # Load known face embeddings
    known_faces = {
        "Person1": np.load("embeddings/person1.npy"),
    }

    # Load your high-resolution image
    image = cv2.imread('test_couple.jpg')
    net = load_yolo_model("yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")
    faces = detect_faces_yolo(image, net, confidence_threshold=0.5)
    for (x1, y1, x2, y2) in faces:
        i+=1
        face_image = image[y1:y2, x1:x2]
        cv2.imwrite(f"test_faces/face_{i}.jpg",face_image)
        plt.imshow(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()
        time.sleep(0.5)

    best_face = None
    best_match_name = None
    best_similarity = -1

    for (x1, y1, x2, y2) in faces:
        face_image = image[y1:y2, x1:x2]
        embedding = extract_face_embedding(face_image)
        if embedding is not None:
            name, similarity = match_face(known_faces, embedding)
            if similarity > best_similarity:
                best_similarity = similarity
                best_face = face_image
                best_match_name = name

        # Draw bounding box and label on the image
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f'{best_match_name} ({best_similarity:.2f})', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display final image
    cv2.imwrite("preproceced_image.jpg", image)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
