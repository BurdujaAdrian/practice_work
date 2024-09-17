import cv2
import numpy as np
import torch
from facenet_pytorch import MTCNN
from insightface import model_zoo
from torchvision.transforms.functional import to_tensor
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
from PIL import Image

# Initialize MTCNN for face alignment
mtcnn = MTCNN(keep_all=True)

# Load ArcFace model for embedding extraction
arcface_model = model_zoo.get_model('arcface_r100_v1')
arcface_model.prepare(ctx_id=0)

# Load the saved embedding (of the reference face) for comparison
saved_embedding = np.load('embeddings/person2.npy')


# YOLO face detection code remains unchanged
def load_yolo_model(config_path, weights_path):
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    return net


def detect_faces_yolo(image, net, confidence_threshold=0.7):
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
    return filter_largest_box(boxes)


# Filter overlapping or redundant boxes by keeping only the largest
def filter_largest_box(boxes):
    if not boxes:
        return []

    # Sort by box area in descending order
    boxes = sorted(boxes, key=lambda b: (b[2] - b[0]) * (b[3] - b[1]), reverse=True)
    largest_boxes = []
    for box in boxes:
        is_duplicate = False
        for existing_box in largest_boxes:
            iou = calculate_iou(box, existing_box)
            if iou > 0.5:  # If IoU is high, consider them the same face
                is_duplicate = True
                break
        if not is_duplicate:
            largest_boxes.append(box)
    return largest_boxes


# Calculate Intersection over Union (IoU) for bounding box overlap
def calculate_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1_, y1_, x2_, y2_ = box2

    # Determine the coordinates of the intersection rectangle
    x_left = max(x1, x1_)
    y_top = max(y1, y1_)
    x_right = min(x2, x2_)
    y_bottom = min(y2, y2_)

    if x_right < x_left or y_bottom < y_top:
        return 0.0  # No overlap

    # Calculate the area of the intersection rectangle
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # Calculate the areas of both the prediction and ground-truth rectangles
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2_ - x1_) * (y2_ - y1_)

    # Compute the intersection over union
    iou = intersection_area / float(box1_area + box2_area - intersection_area)
    return iou


# Use MTCNN to detect and align faces
def detect_and_align_faces(image):
    faces, _ = mtcnn.detect(image)
    aligned_faces = []
    if faces is not None:
        for box in faces:
            face = image[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
            aligned_faces.append(face)
    return aligned_faces


# Extract face embeddings using ArcFace
def extract_arcface_embedding(face_image):
    face_resized = cv2.resize(face_image, (112, 112))  # Resize to ArcFace input size
    face_tensor = to_tensor(Image.fromarray(face_resized))
    face_tensor = face_tensor.unsqueeze(0)  # Add batch dimension
    embedding = arcface_model.get_embedding(face_tensor).flatten().detach().cpu().numpy()
    return embedding


# Find the best matching face in the crowd
def find_best_match(image, net, saved_embedding):
    faces = detect_faces_yolo(image, net)
    best_similarity = float('inf')
    best_face = None

    for (x1, y1, x2, y2) in faces:
        face_image = image[y1:y2, x1:x2]
        aligned_faces = detect_and_align_faces(face_image)

        for aligned_face in aligned_faces:
            embedding = extract_arcface_embedding(aligned_face)
            similarity = euclidean(embedding, saved_embedding)

            if similarity < best_similarity:
                best_similarity = similarity
                best_face = (x1, y1, x2, y2)

    return best_face, best_similarity


# Load the crowd image and YOLO model
crowd_image = cv2.imread('test_group3.jpg')
net = load_yolo_model("yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

best_face, similarity = find_best_match(crowd_image, net, saved_embedding)

# Draw the best match on the image
if best_face is not None:
    (x1, y1, x2, y2) = best_face
    cv2.rectangle(crowd_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(crowd_image, f'Similarity: {similarity:.2f}', (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Save and display the result
cv2.imwrite("matched_image.jpg", crowd_image)
plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
