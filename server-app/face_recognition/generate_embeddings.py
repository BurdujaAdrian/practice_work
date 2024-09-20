import cv2
import numpy as np
from facenet_pytorch import InceptionResnetV1
import torch
from torchvision.transforms.functional import to_tensor
from PIL import Image
import dlib
from sklearn.neighbors import NearestNeighbors

# Initialize FaceNet model (pretrained)
model = InceptionResnetV1(pretrained='vggface2').eval()

# Initialize dlib's face detector and shape predictor for alignment
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


# Function for face alignment based on dlib facial landmarks
def align_face(image, rect):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    landmarks = predictor(gray, rect)

    left_eye = (landmarks.part(36).x, landmarks.part(36).y)
    right_eye = (landmarks.part(45).x, landmarks.part(45).y)

    dY = right_eye[1] - left_eye[1]
    dX = right_eye[0] - left_eye[0]
    angle = np.degrees(np.arctan2(dY, dX))

    center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale=1.0)

    (h, w) = image.shape[:2]
    aligned_face = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC)

    return aligned_face


# Function to enhance small or low-resolution faces using interpolation
def enhance_face_resolution(face_image, target_size=(160, 160)):
    return cv2.resize(face_image, target_size, interpolation=cv2.INTER_CUBIC)


# Function to extract face embeddings
def extract_face_embedding(face_image):
    face_pil = Image.fromarray(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))
    face_tensor = to_tensor(face_pil).unsqueeze(0)

    with torch.no_grad():
        embedding = model(face_tensor).numpy()

    return embedding


# Function to load saved embeddings from a database
def load_saved_embeddings(embedding_files):
    embeddings = []
    labels = []
    for file in embedding_files:
        emb = np.load(file)
        embeddings.append(emb)
        labels.append(file)  # Using filename as the label for simplicity
    return np.vstack(embeddings), labels


# Function to perform face matching using KNN with a threshold
def match_face(embedding, database_embeddings, labels, k=3, distance_threshold=0.6):
    # Initialize KNN model
    knn = NearestNeighbors(n_neighbors=k, metric='euclidean')
    knn.fit(database_embeddings)

    # Find the k nearest neighbors
    distances, indices = knn.kneighbors(embedding, n_neighbors=k)

    # Check if the closest distance is below the threshold
    if distances[0][0] < distance_threshold:
        top_label = labels[indices[0][0]]
        confidence = 1 - (distances[0][0] / distance_threshold)  # Convert distance to confidence
        return top_label, confidence
    else:
        return None, 0


# Full process: detect, align, enhance, and match
def process_and_match_face(image_path, embedding_files):
    image = cv2.imread(image_path)
    faces = detector(image, 1)

    if len(faces) == 1:  # Ensure only one face is detected
        rect = faces[0]
        aligned_face = align_face(image, rect)

        (x, y, w, h) = (rect.left(), rect.top(), rect.width(), rect.height())
        face_image = aligned_face[y:y + h, x:x + w]

        # Enhance the face resolution if necessary
        enhanced_face = enhance_face_resolution(face_image)

        # Extract embedding from the face
        face_embedding = extract_face_embedding(enhanced_face)

        # Load saved embeddings from the database
        database_embeddings, labels = load_saved_embeddings(embedding_files)

        # Match the face against the database
        match_label, confidence = match_face(face_embedding, database_embeddings, labels)

        if match_label:
            print(f"Match found: {match_label} with confidence {confidence:.2f}")
        else:
            print("No match found.")
    else:
        print(f"Error: Expected 1 face, but found {len(faces)}")


# Example usage
embedding_files = ['embeddings/person1.npy', 'embeddings/person2.npy', 'embeddings/person3.npy',
                   'embeddings/person4.npy']
process_and_match_face("Denis2jpg.jpg", embedding_files)