import cv2
import numpy as np
import torch
from PIL import Image
from facenet_pytorch import InceptionResnetV1
from torchvision.transforms.functional import to_tensor
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import requests
import json

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


# Function to preprocess the face image before extracting embeddings
def preprocess_face_image(face_image):
    # Apply super-resolution
    face_sr = sr.upsample(face_image)

    # Apply logarithmic filter
    face_log = apply_log_filter(face_sr)

    # Resize to 160x160 for FaceNet input
    face_resized = cv2.resize(face_log, (160, 160))

    # Convert BGR to RGB for FaceNet
    face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)
    face_pil = Image.fromarray(face_rgb)
    face_tensor = to_tensor(face_pil).unsqueeze(0)
    return face_tensor


# Function to extract face embeddings
def extract_face_embedding(face_image):
    face_tensor = preprocess_face_image(face_image)
    with torch.no_grad():
        embedding = model(face_tensor).numpy()
    return embedding


# YOLO face detection
def load_yolo_model(config_path, weights_path):
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    return net


def detect_faces_yolo(image, net, confidence_threshold=0.3, nms_threshold=0.0):
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getLayerNames()

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

    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)

    final_boxes = []
    if len(indices) > 0:
        if isinstance(indices[0], (list, np.ndarray)):
            final_boxes = [boxes[i[0]] for i in indices]
        else:
            final_boxes = [boxes[i] for i in indices]

    return final_boxes


# Function to fetch all persons and embeddings from PocketBase
def load_embeddings_from_pocketbase(base_url, collection_name):
    url = f"{base_url}/api/collections/{collection_name}/records"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch records: {response.text}")

    data = response.json()["items"]

    people = []
    for person in data:
        person_id = person['id']
        person_name = person['name']
        embedding = np.array(json.loads(person['embedding']), dtype=np.float32)  # Assuming embedding is saved as JSON
        people.append({'id': person_id, 'name': person_name, 'embedding': embedding})

    return people


# Find the most similar face in the crowd by comparing to all people in the PocketBase database
def find_most_similar_face(image, net, people, similarity_threshold=0.3):
    faces = detect_faces_yolo(image, net)
    best_matches = []

    for (x, y, w, h) in faces:
        face_image = image[y:y + h, x:x + w]
        embedding = extract_face_embedding(face_image)

        best_similarity = -1
        best_match = None

        for person in people:
            similarity = cosine_similarity(embedding, person['embedding'].reshape(1, -1))[0][0]
            if similarity > best_similarity and similarity > similarity_threshold:
                best_similarity = similarity
                best_match = {'person': person, 'box': (x, y, w, h), 'similarity': similarity}

        if best_match:
            best_matches.append(best_match)

    return best_matches


# Main function to process the image and match faces
def match_faces_in_crowd(base_url, collection_name, crowd_image_path, yolo_cfg, yolo_weights):
    # Load YOLO model
    net = load_yolo_model(yolo_cfg, yolo_weights)

    # Load embeddings from PocketBase
    people = load_embeddings_from_pocketbase(base_url, collection_name)

    # Load the crowd image
    crowd_image = cv2.imread(crowd_image_path)

    # Find matching faces
    matches = find_most_similar_face(crowd_image, net, people)

    # Draw the results on the image
    for match in matches:
        (x, y, w, h) = match['box']
        person_name = match['person']['name']
        similarity = match['similarity']

        # Draw rectangle around the face
        cv2.rectangle(crowd_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Display name and similarity
        cv2.putText(crowd_image, f'{person_name}: {similarity:.2f}', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Save and display the final image
    cv2.imwrite("matched_image_sr_log_pocketbase.jpg", crowd_image)
    plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()


# Example usage
base_url = 'http://localhost:8090'
collection_name = 'people' 
crowd_image_path = 'test_group3.jpg'  # Path to the crowd image
yolo_cfg = 'yolov3-face.cfg'  # Path to YOLO configuration file
yolo_weights = 'model-weights/yolov3-wider_16000.weights'  # Path to YOLO weights file

match_faces_in_crowd(base_url, collection_name, crowd_image_path, yolo_cfg, yolo_weights)
