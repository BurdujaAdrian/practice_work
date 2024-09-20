import cv2
import numpy as np
from facenet_pytorch import InceptionResnetV1
from torchvision.transforms.functional import to_tensor
from PIL import Image
import torch

# Initialize FaceNet model
model = InceptionResnetV1(pretrained='vggface2').eval()

# Initialize OpenCV's super-resolution model
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# Load pre-trained super-resolution model (e.g., ESPCN)
sr.readModel("model-weights/ESPCN_x4.pb")  # Download the model and place it in the correct path
sr.setModel("espcn", 4)  # Set the model to upscale by a factor of 4


# Logarithmic filter for contrast enhancement
def apply_log_filter(image):
    # Convert to float32 and apply logarithmic transformation
    image_log = np.log1p(np.array(image, dtype="float32"))
    # Normalize back to range [0, 255]
    cv2.normalize(image_log, image_log, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(image_log)


# Function to detect a single face using OpenCV's Haar Cascade
def detect_single_face(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        return image[y:y + h, x:x + w]
    return None


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


# Load the image of the person (change 'person1.jpg' to your image file)
image_path = 'Grubii2.png'
image = cv2.imread(image_path)

if image is None:
    print(f"Could not load image at {image_path}.")
else:
    # Detect the face
    face_image = detect_single_face(image)

    if face_image is not None:
        # Extract and save the face embeddings
        embedding = extract_face_embedding(face_image)
        np.save('embeddings/person4_sr_log.npy', embedding)
        print(f"Embeddings saved to 'embeddings/person1_sr_log.npy'")
    else:
        print("No face detected in the image.")
