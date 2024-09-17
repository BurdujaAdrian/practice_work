import cv2
import numpy as np
import matplotlib.pyplot as plt
from facenet_pytorch import InceptionResnetV1
import torch
from torchvision.transforms.functional import to_tensor
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity


# Initialize FaceNet model
model = InceptionResnetV1(pretrained='vggface2').eval()

saved_embedding = np.load('embeddings/person5.npy')


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
    return boxes


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


# Extract face embeddings for crowd image
def extract_face_embedding(face_image):
    face_resized = cv2.resize(face_image, (160, 160))
    face_pil = Image.fromarray(cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB))
    face_tensor = to_tensor(face_pil).unsqueeze(0)
    with torch.no_grad():
        embedding = model(face_tensor).numpy()
    return embedding


# Find top 10 most similar faces in the crowd
def find_top_10_similar_faces(crowd_image, net, saved_embedding):
    # Process the crowd image using YOLO and extract embeddings from detected faces.
    detected_faces = detect_faces_yolo(crowd_image, net)

    similarities = []

    for face in detected_faces:
        x1, y1, x2, y2 = face
        face_img = crowd_image[y1:y2, x1:x2]
        embedding = extract_face_embedding(face_img, facenet_model)

        # Reshape embeddings to 2D arrays
        embedding_reshaped = embedding.reshape(1, -1)
        saved_embedding_reshaped = saved_embedding.reshape(1, -1)

        # Compute cosine similarity
        similarity = cosine_similarity(embedding_reshaped, saved_embedding_reshaped)[0][0]
        similarities.append((face, similarity))

    # Sort by similarity (descending order) and get the top 10
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_10_faces = similarities[:10]

    return top_10_faces


# Load the crowd image
crowd_image = cv2.imread('test_group6.jpg')
net = load_yolo_model("yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

# Get the top 10 most similar faces
top_10_faces = find_top_10_similar_faces(crowd_image, net, saved_embedding)

# Draw boxes around the top 10 faces with similarity scores
for (x1, y1, x2, y2), similarity in top_10_faces:
    cv2.rectangle(crowd_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(crowd_image, f'Similarity: {similarity:.2f}', (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Save and display the image
cv2.imwrite("top_10_matched_image.jpg", crowd_image)
plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()


'''face = detect_faces_yolo(crowd_image, net)

#crowd_image_copy = crowd_image
#for (x1 ,y1, x2, y2) in face:
#    cv2.rectangle(crowd_image_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
#plt.imshow(cv2.cvtColor(crowd_image_copy, cv2.COLOR_BGR2RGB))'''