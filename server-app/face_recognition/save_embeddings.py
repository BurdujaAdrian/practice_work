import cv2
import torch
import numpy as np
from facenet_pytorch import InceptionResnetV1
from torchvision.transforms.functional import to_tensor
from PIL import Image
import matplotlib.pyplot as plt

# Load YOLOv7-face model
def load_yolov7_model(model_path):
    model = torch.load(model_path)
    model.eval()
    return model

# Perform inference using YOLOv7-face
def detect_faces_yolov7(image, model, device):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0).float() / 255.0  # Normalize and prepare image
    img = img.to(device)

    with torch.no_grad():
        outputs = model(img)

    boxes = outputs[0][:, :4].cpu().numpy()  # Get bounding boxes
    return boxes

# Logarithmic filter for contrast enhancement
def apply_log_filter(image):
    image_log = np.log1p(np.array(image, dtype="float32"))
    cv2.normalize(image_log, image_log, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(image_log)

# Preprocess face before extracting embeddings
def preprocess_face_image(face_image):
    # Resize to 160x160 for FaceNet input
    face_resized = cv2.resize(face_image, (160, 160))

    # Convert BGR to RGB for FaceNet
    face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)
    face_pil = Image.fromarray(face_rgb)
    face_tensor = to_tensor(face_pil).unsqueeze(0)  # Convert to tensor
    return face_tensor

# Extract face embeddings
def extract_face_embedding(face_image, model):
    face_tensor = preprocess_face_image(face_image)
    with torch.no_grad():
        embedding = model(face_tensor).numpy()
    return embedding

# Main process
def main():
    # Load YOLOv7 model
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    yolov7_model = load_yolov7_model("model-weights/yolov3-wider_16000.weights").to(device)

    # Initialize FaceNet model
    facenet_model = InceptionResnetV1(pretrained='vggface2').eval()

    # Load and preprocess the image
    image = cv2.imread('Artur.jpg')

    # Detect faces using YOLOv7
    boxes = detect_faces_yolov7(image, yolov7_model, device)

    # Assuming one face is detected; you can loop for multiple faces
    if len(boxes) > 0:
        x1, y1, x2, y2 = map(int, boxes[0])  # Take the first detected face
        face_image = image[y1:y2, x1:x2]

        # Apply logarithmic filter
        face_log = apply_log_filter(face_image)

        # Extract face embeddings
        embedding = extract_face_embedding(face_log, facenet_model)
        print(embedding)

        # Save the embeddings to a file
        np.save('embeddings/person2_embedding.npy', embedding)
        print("Embeddings saved successfully.")

if __name__ == "__main__":
    main()
