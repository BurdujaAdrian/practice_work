import cv2
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
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

# Find the most similar face in the crowd
def find_most_similar_face(image, yolov7_model, saved_embedding, similarity_threshold=0.5, device=None):
    faces = detect_faces_yolov7(image, yolov7_model, device)
    best_similarity = -1
    best_face = None

    facenet_model = InceptionResnetV1(pretrained='vggface2').eval()

    for (x1, y1, x2, y2) in faces:
        face_image = image[int(y1):int(y2), int(x1):int(x2)]

        # Apply log filter
        face_log = apply_log_filter(face_image)

        # Extract embeddings
        embedding = extract_face_embedding(face_log, facenet_model)

        # Compare embeddings
        similarity = cosine_similarity(embedding, saved_embedding)[0][0]

        if similarity > best_similarity and similarity > similarity_threshold:
            best_similarity = similarity
            best_face = (x1, y1, x2, y2)

    return best_face, best_similarity

# Main process
def main():
    # Load the saved embeddings
    saved_embedding = np.load('embeddings/person2_embedding.npy')

    # Load YOLOv7-face model
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    yolov7_model = load_yolov7_model("model-weights/yolov7-face.pt").to(device)

    # Load the crowd image
    crowd_image = cv2.imread('test_group3.jpg')

    # Find the most similar face
    best_face, similarity = find_most_similar_face(crowd_image, yolov7_model, saved_embedding, device=device)

    if best_face is not None:
        x1, y1, x2, y2 = map(int, best_face)
        cv2.rectangle(crowd_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(crowd_image, f'Similarity: {similarity:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Save and display the result
    cv2.imwrite("matched_image_sr_log.jpg", crowd_image)
    plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
