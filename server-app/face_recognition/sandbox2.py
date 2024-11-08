import cv2
import numpy as np
import torch
from PIL import Image
from facenet_pytorch import InceptionResnetV1, MTCNN
from torchvision.transforms.functional import to_tensor
from sklearn.metrics.pairwise import cosine_similarity
import requests
import json
import argparse
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Load models
model = InceptionResnetV1(pretrained='vggface2').eval()
mtcnn = MTCNN(keep_all=True, post_process=False)

# Initialize super-resolution model
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel(os.path.join(script_dir, "model-weights/ESPCN_x4.pb"))
sr.setModel("espcn", 4)

def apply_log_filter(image):
    image_log = np.log1p(np.array(image, dtype="float32"))
    cv2.normalize(image_log, image_log, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(image_log)

def preprocess_face_image(face_image):
    if face_image is None or face_image.size == 0:
        raise ValueError("Received an empty face image for preprocessing.")
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

def detect_faces_mtcnn(image):
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    boxes, _ = mtcnn.detect(image_pil)
    if boxes is not None:
        final_boxes = boxes.astype(int).tolist()
        visualize_faces(image,final_boxes)
        for (x1, y1, x2, y2) in final_boxes:
            print(f"Detected face at: (x1={x1}, y1={y1}, x2={x2}, y2={y2}), width={x2-x1}, height={y2-y1}")
        return final_boxes
    else:
        print("No faces detected.")
        return []

def visualize_faces(image, boxes):
    for (x1, y1, x2, y2) in boxes:
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)  # Press any key to close the window
    cv2.destroyAllWindows()



def admin_login(base_url, admin_email, admin_password):
    url = f"{base_url}/api/admins/auth-with-password"
    data = {"identity": admin_email, "password": admin_password}
    response = requests.post(url, json=data)
    if response.status_code != 200:
        raise Exception(f"Failed to authenticate admin: {response.text}")
    return response.json()["token"]

def load_people_from_pocketbase(base_url, collection_name, token, group_list):
    group_filter = " || ".join([f'Group="{group}"' for group in group_list])
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
        people.append({'id': person_id, 'name': person_name, 'embedding': embedding, 'Photo': image})

    return people

def save_embeddings_to_pocketbase(base_url, collection_name, person_id, embedding, token):
    url = f"{base_url}/api/collections/{collection_name}/records/{person_id}"
    embedding_str = json.dumps(embedding.tolist())
    data = {'Embedding': embedding_str}
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = requests.patch(url, json=data, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to save embedding: {response.text}")

def generate_and_save_embeddings(base_url, collection_name, people, token):
    for person in people:
        if person['embedding'] is None:
            image = person["Photo"]
            faces = detect_faces_mtcnn(image)
            if faces:
                (x, y, w, h) = faces[0]  # Take the first detected face
                cropped_face = image[y:y + h, x:x + w]
                embedding = extract_face_embedding(cropped_face)
                #save_embeddings_to_pocketbase(base_url, collection_name, person['id'], embedding, token)
                person['embedding'] = embedding


def find_most_similar_face_for_person(image, people, similarity_threshold=0.3):
    faces = detect_faces_mtcnn(image)
    if not faces:
        print("No faces detected in the crowd image.")
        return []

    person_matches = []
    for person in people:
        best_similarity, best_match = -1, None
        for (x, y, w, h) in faces:
            if w <= 0 or h <= 0:
                continue  # Skip invalid face regions

            face_image = image[y:y + h, x:x + w]
            if face_image.size == 0:
                print("Skipping empty face image.")
                continue

            try:
                embedding = extract_face_embedding(face_image)
            except ValueError as e:
                print(f"Error processing face image: {e}")
                continue

            similarity = cosine_similarity(embedding, person['embedding'].reshape(1, -1))[0][0]
            if similarity > best_similarity and similarity > similarity_threshold:
                best_similarity = similarity
                best_match = {'person': person, 'box': (x, y, w, h), 'similarity': similarity}

        if best_match:
            person_matches.append(best_match)

    return person_matches


def match_faces_in_crowd(base_url, collection_name, crowd_image_path, admin_email, admin_password, group_list):
    token = admin_login(base_url, admin_email, admin_password)
    people = load_people_from_pocketbase(base_url, collection_name, token, group_list)
    generate_and_save_embeddings(base_url, collection_name, people, token)

    crowd_image = cv2.imread(crowd_image_path)
    matches = find_most_similar_face_for_person(crowd_image, people)

    similarity_dict = {}

    for match in matches:
        (x, y, w, h) = match['box']
        person_name = match['person']['name']
        similarity = match['similarity'] * 100
        similarity_dict[person_name] = f'{similarity:.2f}%'
        cv2.rectangle(crowd_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(crowd_image, f'{person_name}: {similarity:.2f}%', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    print(similarity_dict)
    cv2.imwrite("matched_image_sr_log_pocketbase.jpg", crowd_image)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Face recognition in crowd images with group filtering")
    parser.add_argument("crowd_image_path", help="Path to the crowd image")
    parser.add_argument("group_list", nargs='+', help="List of student groups to filter")
    args = parser.parse_args()

    base_url = 'http://127.0.0.1:8090'
    collection_name = 'Students'
    admin_email = 'admin@gmail.com'
    admin_password = '1234567890'

    match_faces_in_crowd(base_url, collection_name, args.crowd_image_path, admin_email, admin_password, args.group_list)
