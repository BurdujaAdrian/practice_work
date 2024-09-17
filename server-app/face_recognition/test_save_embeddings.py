import cv2
import numpy as np
from facenet_pytorch import InceptionResnetV1
import torch
from torchvision.transforms.functional import to_tensor
from PIL import Image

# Initialize FaceNet model (pretrained)
model = InceptionResnetV1(pretrained='vggface2').eval()


# Function to load and process the image, extract face, and get embeddings
def extract_face_embeddings(image_path, output_path='embeddings/person4.npy'):
    image = cv2.imread(image_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(160, 160))

    if len(faces) == 1:  # Ensure only one face is detected
        (x, y, w, h) = faces[0]
        face_image = image[y:y + h, x:x + w]
        face_pil = Image.fromarray(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))
        face_tensor = to_tensor(face_pil).unsqueeze(0)  # Convert to tensor and add batch dimension

        # Extract embeddings
        with torch.no_grad():
            embedding = model(face_tensor).numpy()

        # Save embeddings to .npy file
        np.save(output_path, embedding)
        print(f"Face embedding saved to {output_path}")
    else:
        print(f"Error: Expected 1 face, but found {len(faces)}")


# Example usage
extract_face_embeddings("Denis2jpg.jpg")
