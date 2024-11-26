import cv2
import numpy as np
import torch
from PIL import Image
from facenet-pytorch import InceptionResnetV1
from torchvision.transforms.functional import to_tensor
from sklearn.metrics.pairwise import cosine_similarity
import requests
import json
import argparse
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

try:
    model = InceptionResnetV1(pretrained='vggface2').eval()
except Exception as e:
    print(f"Error loading FaceNet model: {e}")

try:
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(os.path.join(script_dir, "model-weights/ESPCN_x4.pb"))
    sr.setModel("espcn", 4)
except Exception as e:
    print(f"Error loading super-resolution model: {e}")


def apply_log_filter(image):
    try:
        image_log = np.log1p(np.array(image, dtype="float32"))
        cv2.normalize(image_log, image_log, 0, 255, cv2.NORM_MINMAX)
        return np.uint8(image_log)
    except Exception as e:
        print(f"Error applying log filter: {e}")
        return image


def preprocess_face_image(face_image):
    try:
        face_sr = sr.upsample(face_image)
        face_log = apply_log_filter(face_sr)
        face_resized = cv2.resize(face_log, (160, 160))
        face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)
        face_pil = Image.fromarray(face_rgb)
        face_tensor = to_tensor(face_pil).unsqueeze(0)
        return face_tensor
    except Exception as e:
        print(f"Error preprocessing face image: {e}")
        return None


def extract_face_embedding(face_image):
    face_tensor = preprocess_face_image(face_image)
    if face_tensor is None:
        return None
    try:
        with torch.no_grad():
            embedding = model(face_tensor).numpy()
        return embedding
    except Exception as e:
        print(f"Error extracting face embedding: {e}")
        return None


def load_yolo_model(config_path, weights_path):
    try:
        net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
        return net
    except Exception as e:
        print(f"Error loading YOLO model: {e}")
        return None


def detect_faces_yolo(image, net, confidence_threshold=0.3, nms_threshold=0.0):
    try:
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
    except Exception as e:
        print(f"Error detecting faces with YOLO: {e}")
        return []


def admin_login(base_url, admin_email, admin_password):
    try:
        url = f"{base_url}/api/admins/auth-with-password"
        data = {"identity": admin_email, "password": admin_password}
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()["token"]
    except Exception as e:
        print(f"Error during admin login: {e}")
        return None


def load_people_from_pocketbase(base_url, collection_name, token, group_list):
    try:
        group_filter = " || ".join([f'Group_name="{Group}"' for Group in group_list])
        url = f"{base_url}/api/collections/Groups/records?filter={group_filter}"
        headers = {"Authorization": f"Bearer {token}"}
        group_response = requests.get(url, headers=headers)
        group_response.raise_for_status()
        group_data = group_response.json().get("items", [])
        group_id_list = [group.get('id') for group in group_data if group.get('id')]
        student_filter = " || ".join([f'Group="{group_id}"' for group_id in group_id_list])
        url = f"{base_url}/api/collections/{collection_name}/records?filter={student_filter}"
        student_response = requests.get(url, headers=headers)
        student_response.raise_for_status()
        student_data = student_response.json().get("items", [])
        people = []
        for person in student_data:
            person_id = person.get('id')
            surname = person.get('Surname', '').strip()
            name = person.get('Name', '').strip()
            person_name = f"{surname}_{name}" if surname and name else None
            print(f"Processing Person ID: {person_id}, Full Name: {person_name}")  # Debugging

            photo_filename = person.get('Photo', '').translate(str.maketrans("ăîțș", "____"))
            photo_url = f"D:\\practice_work\\database\\pb_data\\storage\\4i53pyqjukl7lxi\\{person_id}\\{photo_filename}"
            try:
                image = cv2.imread(photo_url)
                if image is None:
                    print(f"Error: Unable to load image for person ID {person_id}")
                    continue
            except Exception:
                continue
            embedding = None
            if person.get('Embedding'):
                embedding = json.loads(person['Embedding'])
            people.append({'id': person_id, 'name': person_name, 'Embedding': embedding, 'Photo': image})
        return people
    except Exception as e:
        print(f"Error loading people from PocketBase: {e}")
        return []


def save_embeddings_to_pocketbase(base_url, collection_name, person_id, embedding, token):
    try:
        url = f"{base_url}/api/collections/{collection_name}/records/{person_id}"
        data = {'Embedding': json.dumps(embedding.flatten().tolist())}  # Convert embedding to JSON string
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        print(f"Payload for person {person_id}: {data}")
        response = requests.patch(url, json=data, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Error saving embedding to PocketBase for person ID {person_id}: {e}")




def generate_and_save_embeddings(base_url, collection_name, people, net, token):
    for person in people:
        if person['Embedding'] is not None:
            continue
        image = person["Photo"]
        if image is None:
            continue
        faces = detect_faces_yolo(image, net)
        if not faces:
            continue
        (x, y, w, h) = faces[0]
        cropped_face = image[y:y + h, x:x + w]
        embedding = extract_face_embedding(cropped_face)
        if embedding is not None:
            save_embeddings_to_pocketbase(base_url, collection_name, person['id'], embedding, token)
            person['Embedding'] = embedding  # Update local copy



def find_most_similar_face_for_person(image, net, people, similarity_threshold=0.3):
    try:
        faces = detect_faces_yolo(image, net)
        if not faces:
            return []
        person_matches = []
        for person in people:
            best_similarity, best_match, best_face = -1, None, None
            for (x, y, w, h) in faces:
                face_image = image[y:y + h, x:x + w]
                embedding = extract_face_embedding(face_image)
                if embedding is not None:
                    person_embedding = np.array(person['Embedding']) if person['Embedding'] else None
                    if person_embedding is not None:
                        similarity = cosine_similarity(embedding, person_embedding.reshape(1, -1))[0][0]
                        if similarity > best_similarity and similarity > similarity_threshold:
                            best_similarity = similarity
                            best_match = {'person': person, 'box': (x, y, w, h), 'similarity': similarity}
                            best_face = face_image
            if best_match and best_face is not None:
                person_matches.append({'match': best_match, 'face_image': best_face})
        return person_matches
    except Exception as e:
        print(f"Error finding most similar face: {e}")
        return []


def save_faces_for_people(matches, output_dir):
    print(f"Processing person: {matches}")
    os.makedirs("../server-app/face_recognition/"+ output_dir, exist_ok=True)
    for match in matches:
        person = match['match']['person']
        face_image = match['face_image']
        person_name = person['name']

        # Save the cropped face as "<person_name>.png"
        face_image_path = os.path.join("../server-app/face_recognition/"+ output_dir, f"{person_name}.png")
        cv2.imwrite(face_image_path, face_image)
        print(f"Saved face for {person_name} at {face_image_path}")


def match_faces_in_crowd(base_url, collection_name, crowd_image_path, yolo_cfg, yolo_weights, admin_email, admin_password, group_list, output_dir):
    try:
        token = admin_login(base_url, admin_email, admin_password)
        if not token:
            return
        net = load_yolo_model(yolo_cfg, yolo_weights)
        if not net:
            return
        people = load_people_from_pocketbase(base_url, collection_name, token, group_list)
        generate_and_save_embeddings(base_url, collection_name, people, net, token)
        crowd_image = cv2.imread(crowd_image_path)
        if crowd_image is None:
            print("Error: Crowd image could not be loaded.")
            return
        matches = find_most_similar_face_for_person(crowd_image, net, people)
        save_faces_for_people(matches, output_dir)
    except Exception as e:
        print(f"Error in matching faces in crowd: {e}")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Face recognition in crowd images with group filtering")
        parser.add_argument("crowd_image_path", help="Path to the crowd image")
        parser.add_argument("group_list", nargs='+', help="List of student groups to filter")
        output_dir = 'recognised_faces'
        args = parser.parse_args()
        base_url = 'http://127.0.0.1:8090'
        collection_name = 'Students'
        yolo_cfg = os.path.join(script_dir, 'model-weights/yolov3-face.cfg')
        yolo_weights = os.path.join(script_dir, 'model-weights/yolov3-wider_16000.weights')
        admin_email = 'admin@gmail.com'
        admin_password = '1234567890'
        match_faces_in_crowd(base_url, collection_name, args.crowd_image_path, yolo_cfg, yolo_weights, admin_email, admin_password, args.group_list, output_dir)
    except Exception as e:
        print(f"Error in main execution: {e}")