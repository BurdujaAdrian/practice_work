import cv2
import numpy as np
from facenet_pytorch import InceptionResnetV1
from torchvision.transforms.functional import to_tensor
from PIL import Image
import torch
import os

# Initialize FaceNet model
model = InceptionResnetV1(pretrained='vggface2').eval()

# Create 'embeddings' folder if it doesn't exist
if not os.path.exists('embeddings'):
    os.makedirs('embeddings')

# Function to detect a face using OpenCV's Haar Cascade for simplicity
def detect_single_face(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        # Return the first face found
        (x, y, w, h) = faces[0]
        return image[y:y+h, x:x+w]
    else:
        return None

# Function to preprocess face image before embedding extraction
def preprocess_face_image(face_image):
    face_resized = cv2.resize(face_image, (160, 160))
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

# Load the image of the person (change 'person1.jpg' to your image file)
image_path = 'Denis2jpg.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Could not load image at {image_path}. Please check the path.")
else:
    # Detect the face
    face_image = detect_single_face(image)

    if face_image is not None:
        # Extract and save the face embeddings
        embedding = extract_face_embedding(face_image)
        np.save('embeddings/person1.npy', embedding)
        print(f"Embeddings saved to 'embeddings/person1.npy'")
    else:
        print("No face detected in the image.")
