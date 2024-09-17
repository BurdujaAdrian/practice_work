import cv2
import numpy as np
import matplotlib.pyplot as plt
from facenet_pytorch import InceptionResnetV1
import torch
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


# Load your high-resolution image
image = cv2.imread('test_group3.jpg')
net = load_yolo_model("yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

# Detect faces in the image
faces = detect_faces_yolo(image, net, confidence_threshold=0.5)

# Load the pre-trained FaceNet model (InceptionResnetV1)
facenet_model = InceptionResnetV1(pretrained='vggface2').eval()


# Function to extract FaceNet embeddings
def get_facenet_embedding(face_image):
    # Preprocess the face image for FaceNet (160x160)
    face_image_resized = cv2.resize(face_image, (160, 160))
    face_image_resized = face_image_resized.astype(np.float32) / 255.0  # Normalize to [0, 1]

    # Convert to torch tensor and normalize to [-1, 1]
    face_tensor = torch.tensor(face_image_resized).permute(2, 0, 1).unsqueeze(0)  # Convert to (1, 3, 160, 160)
    face_tensor = (face_tensor - 0.5) * 2  # Normalize to [-1, 1]

    # Get embedding
    with torch.no_grad():
        embedding = facenet_model(face_tensor).numpy().flatten()
    return embedding


# Iterate through detected faces, save them, and extract embeddings
for (x1, y1, x2, y2) in faces:
    i += 1
    face_image = image[y1:y2, x1:x2]

    # Save face image for reference
    cv2.imwrite(f"test_faces/face_{i}.jpg", face_image)

    # Extract FaceNet embeddings
    embedding = get_facenet_embedding(face_image)
    print(f"Face {i} embedding: {embedding}")

    # Display the face
    plt.imshow(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    time.sleep(0.6)

# Draw bounding boxes around detected faces
for (x1, y1, x2, y2) in faces:
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display final image with bounding boxes
cv2.imwrite("preprocessed_image.jpg", image)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
