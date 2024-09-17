import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity

# Initialize FaceAnalysis with ArcFace model
app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=-1)  # Use ctx_id=-1 for CPU, ctx_id=0 for GPU


# Function to extract face embeddings
def extract_face_embedding(face_image):
    face_pil = Image.fromarray(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))
    faces = app.get(face_pil)
    if len(faces) > 0:
        # Assume we are interested in the first detected face
        embedding = faces[0].embedding
        return embedding
    return None


# YOLO face detection code
def load_yolo_model(config_path, weights_path):
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    return net


def detect_faces_yolo(image, net, confidence_threshold=0.1):
    # Prepare input blob for YOLO
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getLayerNames()

    # Retrieve output layer names
    out_layer_indices = net.getUnconnectedOutLayers()
    if isinstance(out_layer_indices[0], np.ndarray):
        out_layer_indices = out_layer_indices.flatten()

    output_layers = [layer_names[i - 1] for i in out_layer_indices]
    layer_outputs = net.forward(output_layers)

    height, width = image.shape[:2]
    boxes = []
    confidences = []
    class_ids = []

    for output in layer_outputs:
        for detection in output:
            # Ensure detection is a 2D array
            if len(detection.shape) != 2:
                continue

            for obj in detection:
                # Debug: print shape and type of obj
                print(f"Detection object shape: {obj.shape}, type: {type(obj)}")

                # Check if the obj is a valid detection
                if obj.ndim < 2 or obj.size < 7:
                    continue

                scores = obj[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > confidence_threshold:
                    # Convert YOLO box format to (x, y, w, h) and then to (x1, y1, x2, y2)
                    box = obj[0:4] * np.array([width, height, width, height])
                    (centerX, centerY, w, h) = box.astype("int")
                    x = int(centerX - (w / 2))
                    y = int(centerY - (h / 2))
                    boxes.append((x, y, x + w, y + h))
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

    # Optionally, use Non-Max Suppression to filter out overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, 0.1)
    if len(indices) > 0:
        indices = indices.flatten()
        boxes = [boxes[i] for i in indices]
        confidences = [confidences[i] for i in indices]
        class_ids = [class_ids[i] for i in indices]

    return filter_largest_box(boxes)


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


def find_most_similar_face(image, net, saved_embedding):
    faces = detect_faces_yolo(image, net)
    best_similarity = -1
    best_face = None
    for (x1, y1, x2, y2) in faces:
        face_image = image[y1:y2, x1:x2]
        embedding = extract_face_embedding(face_image)
        if embedding is not None:
            similarity = cosine_similarity([embedding], [saved_embedding])[0][0]
            if similarity > best_similarity:
                best_similarity = similarity
                best_face = (x1, y1, x2, y2)
    return best_face, best_similarity


# Load the crowd image
crowd_image = cv2.imread('test_group3.jpg')
net = load_yolo_model("yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

# Load saved embedding
saved_embedding = np.load('embeddings/person2.npy')

best_face, similarity = find_most_similar_face(crowd_image, net, saved_embedding)

if best_face is not None:
    (x1, y1, x2, y2) = best_face
    cv2.rectangle(crowd_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(crowd_image, f'Similarity: {similarity:.2f}', (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

cv2.imwrite("matched_image.jpg", crowd_image)
plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
