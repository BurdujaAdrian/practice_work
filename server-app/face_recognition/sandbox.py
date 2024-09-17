import cv2
import numpy as np
import matplotlib.pyplot as plt
from facenet_pytorch import InceptionResnetV1
import torch
from torchvision.transforms.functional import to_tensor
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize

# Initialize FaceNet model
model = InceptionResnetV1(pretrained='vggface2').eval()

# Load multiple saved embeddings
saved_embeddings = {
    'person1': normalize(np.load('embeddings/person1.npy')),
    'person2': normalize(np.load('embeddings/person2.npy')),
    # Add more saved embeddings as needed
}


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


def extract_face_embedding(face_image):
    face_resized = cv2.resize(face_image, (160, 160))
    face_pil = Image.fromarray(cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB))
    face_tensor = to_tensor(face_pil).unsqueeze(0)
    with torch.no_grad():
        embedding = model(face_tensor).numpy()

    # Normalize the embedding vector for better accuracy in cosine similarity
    normalized_embedding = normalize(embedding)
    return normalized_embedding


def filter_largest_box(boxes):
    if not boxes:
        return []
    boxes = sorted(boxes, key=lambda b: (b[2] - b[0]) * (b[3] - b[1]), reverse=True)
    largest_boxes = []
    for box in boxes:
        is_duplicate = False
        for existing_box in largest_boxes:
            iou = calculate_iou(box, existing_box)
            if iou > 0.5:
                is_duplicate = True
                break
        if not is_duplicate:
            largest_boxes.append(box)
    return largest_boxes


def calculate_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1_, y1_, x2_, y2_ = box2
    x_left = max(x1, x1_)
    y_top = max(y1, y1_)
    x_right = min(x2, x2_)
    y_bottom = min(y2, y2_)
    if x_right < x_left or y_bottom < y_top:
        return 0.0
    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2_ - x1_) * (y2_ - y1_)
    iou = intersection_area / float(box1_area + box2_area - intersection_area)
    return iou


def non_maximum_suppression(boxes, scores, iou_threshold=0.4):
    idxs = np.argsort(scores)[::-1]  # Sort scores in descending order
    filtered_boxes = []

    while len(idxs) > 0:
        i = idxs[0]  # Pick the box with the highest score
        filtered_boxes.append(boxes[i])

        # Compare IoU of this box with the remaining boxes
        remaining_idxs = []
        for j in idxs[1:]:
            iou = calculate_iou(boxes[i], boxes[j])
            if iou <= iou_threshold:
                remaining_idxs.append(j)

        idxs = remaining_idxs  # Update idxs to only keep non-overlapping boxes

    return filtered_boxes


# Function to find the most similar faces in the crowd
def find_similar_faces(image, net, saved_embeddings, threshold=0.4, iou_threshold=0.4):
    faces = detect_faces_yolo(image, net)
    all_matched_faces = []

    for (x1, y1, x2, y2) in faces:
        face_image = image[y1:y2, x1:x2]
        embedding = extract_face_embedding(face_image)

        for person, saved_embedding in saved_embeddings.items():
            similarity = cosine_similarity(embedding, saved_embedding)[0][0]

            if similarity > threshold:
                all_matched_faces.append((x1, y1, x2, y2, person, similarity))

    # Apply Non-Maximum Suppression to avoid overlapping matches
    if all_matched_faces:
        boxes = [(x1, y1, x2, y2) for (x1, y1, x2, y2, _, _) in all_matched_faces]
        scores = [similarity for (_, _, _, _, _, similarity) in all_matched_faces]
        final_boxes = non_maximum_suppression(boxes, scores, iou_threshold=iou_threshold)

        matched_faces = [match for match in all_matched_faces if
                         (match[0], match[1], match[2], match[3]) in final_boxes]
        return matched_faces

    return []


# Load the crowd image
crowd_image = cv2.imread('test_group7.jpg')
net = load_yolo_model("yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

# Detect and match multiple faces
matched_faces = find_similar_faces(crowd_image, net, saved_embeddings)

# Draw rectangles and labels on detected faces
for (x1, y1, x2, y2, person, similarity) in matched_faces:
    cv2.rectangle(crowd_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(crowd_image, f'{person} ({similarity:.2f})', (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

cv2.imwrite("matched_image.jpg", crowd_image)
plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
