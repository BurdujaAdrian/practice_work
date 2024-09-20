import cv2
import numpy as np
import torch
from PIL import Image
from facenet_pytorch import InceptionResnetV1
from torchvision.transforms.functional import to_tensor
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import time
i = 0
# Initialize FaceNet model
model = InceptionResnetV1(pretrained='vggface2').eval()

# Load super-resolution model
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel("model-weights/ESPCN_x4.pb")
sr.setModel("espcn", 4)  # Set the model to upscale by a factor of 4


# Logarithmic filter for contrast enhancement
def apply_log_filter(image):
    image_log = np.log1p(np.array(image, dtype="float32"))
    cv2.normalize(image_log, image_log, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(image_log)


# YOLO face detection
def load_yolo_model(config_path, weights_path):
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    return net


def detect_faces_yolo(image, net, confidence_threshold=0.3, nms_threshold=0.0):
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getLayerNames()

    # Handle both cases for getUnconnectedOutLayers()
    unconnected_layers = net.getUnconnectedOutLayers()

    if isinstance(unconnected_layers, np.ndarray):
        output_layers = [layer_names[i - 1] for i in unconnected_layers.flatten()]
    else:
        output_layers = [layer_names[unconnected_layers - 1]]

    layer_outputs = net.forward(output_layers)
    height, width = image.shape[:2]
    boxes = []
    confidences = []

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
                boxes.append([x, y, int(w), int(h)])
                confidences.append(float(confidence))

    # Apply non-maximum suppression to remove overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)

    # Ensure indices are correctly handled
    final_boxes = []
    if len(indices) > 0:
        # Handle both array of arrays and flat list cases
        if isinstance(indices[0], (list, np.ndarray)):
            final_boxes = [boxes[i[0]] for i in indices]  # List of lists case
        else:
            final_boxes = [boxes[i] for i in indices]  # Flat list case

    return final_boxes


# Preprocess face before extracting embeddings
def preprocess_face_image(face_image):
    global i
    # Apply super-resolution
    face_sr = sr.upsample(face_image)


    # Apply logarithmic filter
    face_log = apply_log_filter(face_sr)
    cv2.imwrite(f"log_faces/faces_log_filter_{i}.jpg", face_log)
    i = i + 1
    plt.imshow(face_log)
    plt.axis('off')
    plt.show()
    time.sleep(0.7)

    # Resize to 160x160 for FaceNet input
    face_resized = cv2.resize(face_log, (160, 160))

    # Convert BGR to RGB for FaceNet
    face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)
    face_pil = Image.fromarray(face_rgb)
    face_tensor = to_tensor(face_pil).unsqueeze(0)
    return face_tensor


# Extract face embeddings
def extract_face_embedding(face_image):
    face_tensor = preprocess_face_image(face_image)
    with torch.no_grad():
        embedding = model(face_tensor).numpy()
    return embedding


# Find the most similar face in the crowd
def find_most_similar_face(image, net, saved_embedding, similarity_threshold=0.3):
    faces = detect_faces_yolo(image, net)
    best_similarity = -1
    best_face = None

    for (x, y, w, h) in faces:
        face_image = image[y:y + h, x:x + w]
        embedding = extract_face_embedding(face_image)
        similarity = cosine_similarity(embedding, saved_embedding)[0][0]

        if similarity > best_similarity and similarity > similarity_threshold:
            best_similarity = similarity
            best_face = (x, y, w, h)

    return best_face, best_similarity


# Load the crowd image
crowd_image = cv2.imread('test_group6.jpg')
saved_embedding = np.load('embeddings/person4_sr_log.npy')
net = load_yolo_model("yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

# Find the best matching face in the crowd
best_face, similarity = find_most_similar_face(crowd_image, net, saved_embedding)

if best_face is not None:
    (x, y, w, h) = best_face
    cv2.rectangle(crowd_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(crowd_image, f'Similarity: {similarity:.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0),
                2)

cv2.imwrite("matched_image_sr_log.jpg", crowd_image)
plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
