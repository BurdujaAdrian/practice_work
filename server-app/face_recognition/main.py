import cv2
import numpy as np
import torch
from PIL import Image
from facenet_pytorch import InceptionResnetV1
from torchvision.transforms.functional import to_tensor
from sklearn.metrics.pairwise import cosine_similarity
import requests
import json
import argparse
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

model = InceptionResnetV1(pretrained='vggface2').eval()

sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel(os.path.join(script_dir, "model-weights/ESPCN_x4.pb"))
sr.setModel("espcn", 4)


def apply_log_filter(image):
    image_log = np.log1p(np.array(image, dtype="float32"))
    cv2.normalize(image_log, image_log, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(image_log)


def preprocess_face_image(face_image):
    face_sr = sr.upsample(face_image)
    face_log = apply_log_filter(face_sr)
    face_resized = cv2.resize(face_log, (160, 160))
    face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)
    face_pil = Image.fromarray(face_rgb)
    face_tensor = to_tensor(face_pil).unsqueeze(0)
    return face_tensor


def extract_face_embedding(face_image):
    face_tensor = preprocess_face_image(face_image)
    with torch.no_grad():
        embedding = model(face_tensor).numpy()
    return embedding


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
    boxes, confidences = [], []
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


def admin_login(base_url, admin_email, admin_password):
    url = f"{base_url}/api/admins/auth-with-password"
    data = {"identity": admin_email, "password": admin_password}
    response = requests.post(url, json=data)
    if response.status_code != 200:
        raise Exception(f"Failed to authenticate admin: {response.text}")
    return response.json()["token"]


def load_people_from_pocketbase(base_url, collection_name, token, group_list):
    # Join group_list elements into a comma-separated string to send in the filter
    group_filter = " || ".join([f'Group="{group}"' for group in group_list])

    # Create the URL with the filter query
    url = f"{base_url}/api/collections/{collection_name}/records?filter={group_filter}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch records: {response.text}")

    data = response.json()["items"]
    people = []

    for person in data:
        person_id = person['id']
        person_name = person['name']
        embedding = None
        url2 = f"pb_data/storage/4i53pyqjukl7lxi/{person_id}/{person['Photo']}"
        image = cv2.imread(url2)
        if 'Embedding' in person and person['Embedding']:
            embedding = np.array(json.loads(person['Embedding']), dtype=np.float32)
        people.append({'id': person_id, 'name': person_name, 'Embedding': embedding, 'Photo': image})

    return people


def save_embeddings_to_pocketbase(base_url, collection_name, person_id, embedding, token):
    url = f"{base_url}/api/collections/{collection_name}/records/{person_id}"
    embedding_str = json.dumps(embedding.tolist())
    data = {'embedding': embedding_str}
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = requests.patch(url, json=data, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to save embedding: {response.text}")


def generate_and_save_embeddings(base_url, collection_name, people, net, token):
    for person in people:
        if person['Embedding'] is None:
            image = person["Photo"]
            face_image = detect_faces_yolo(image, net)[0]
            (x, y, w, h) = face_image
            cropped_face = image[y:y + h, x:x + w]
            embedding = extract_face_embedding(cropped_face)
            save_embeddings_to_pocketbase(base_url, collection_name, person['id'], embedding, token)
            person['embedding'] = embedding


def find_most_similar_face_for_person(image, net, people, similarity_threshold=0.3):
    faces = detect_faces_yolo(image, net)  # Detect all faces in the image
    if not faces:
        return []
    person_matches = []
    for person in people:
        best_similarity, best_match = -1, None
        for (x, y, w, h) in faces:
            face_image = image[y:y + h, x:x + w]
            embedding = extract_face_embedding(face_image)
            similarity = cosine_similarity(embedding, person['embedding'].reshape(1, -1))[0][0]
            if similarity > best_similarity and similarity > similarity_threshold:
                best_similarity = similarity
                best_match = {'person': person, 'box': (x, y, w, h), 'similarity': similarity}
        if best_match:
            person_matches.append(best_match)
    return person_matches


def match_faces_in_crowd(base_url, collection_name, crowd_image_path, yolo_cfg, yolo_weights, admin_email, admin_password, group_list):
    token = admin_login(base_url, admin_email, admin_password)
    net = load_yolo_model(yolo_cfg, yolo_weights)
    people = load_people_from_pocketbase(base_url, collection_name, token, group_list)
    generate_and_save_embeddings(base_url, collection_name, people, net, token)

    crowd_image = cv2.imread(crowd_image_path)
    matches = find_most_similar_face_for_person(crowd_image, net, people)

    similarity_dict = {}

    for match in matches:
        (x, y, w, h) = match['box']
        person_name = match['person']['name']
        similarity = match['similarity'] * 100  # Convert to percentage

        # Add to the dictionary
        similarity_dict[person_name] = f'{similarity:.2f}%'

        # Draw rectangle and similarity score on the image
        cv2.rectangle(crowd_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(crowd_image, f'{person_name}: {similarity:.2f}%', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Print the dictionary
    print(similarity_dict)
    cv2.imwrite("matched_image_sr_log_pocketbase.jpg", crowd_image)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Face recognition in crowd images with group filtering")
    parser.add_argument("crowd_image_path", help="Path to the crowd image")
    parser.add_argument("group_list", nargs='+', help="List of student groups to filter")
    args = parser.parse_args()

    base_url = 'http://127.0.0.1:8090'
    collection_name = 'Students'
    yolo_cfg = os.path.join(script_dir, 'model-weights/yolov3-face.cfg')
    yolo_weights = os.path.join(script_dir, 'model-weights/yolov3-wider_16000.weights')
    admin_email = 'admin@gmail.com'
    admin_password = '1234567890'

    match_faces_in_crowd(base_url, collection_name, args.crowd_image_path, yolo_cfg, yolo_weights, admin_email, admin_password, args.group_list)