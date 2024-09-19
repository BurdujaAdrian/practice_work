import cv2
import numpy as np
import matplotlib.pyplot as plt
from facenet_pytorch import InceptionResnetV1
import torch
from torchvision.transforms.functional import to_tensor
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from concurrent.futures import ThreadPoolExecutor

model = InceptionResnetV1(pretrained='vggface2').eval()

saved_embedding = np.load('embeddings/person7.npy')

def load_yolo_model(config_path, weights_path):
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    return net

def detect_faces_yolo(image, net, confidence_threshold=0.3, nms_threshold=0.4):
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getLayerNames()

    # Handle both cases for getUnconnectedOutLayers()
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


# Preprocess and batch process faces for embedding extraction
def preprocess_face_images(image, faces):
    face_tensors = []
    for (x, y, w, h) in faces:
        face_image = image[y:y+h, x:x+w]
        face_resized = cv2.resize(face_image, (160, 160))
        face_tensor = to_tensor(Image.fromarray(cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB))).unsqueeze(0)
        face_tensors.append(face_tensor)
    return torch.cat(face_tensors)

# Extract embeddings for the preprocessed faces
def extract_face_embeddings(face_tensors):
    with torch.no_grad():
        embeddings = model(face_tensors).numpy()
    return embeddings

# Parallel processing for similarity comparison
def compare_face_embeddings(embedding, saved_embedding):
    return cosine_similarity(embedding.reshape(1, -1), saved_embedding)[0][0]

# Find the most similar face in the crowd with parallelism
def find_most_similar_face(image, net, saved_embedding, similarity_threshold=0.1):
    faces = detect_faces_yolo(image, net)
    if not faces:
        return None, -1  # No face detected

    face_tensors = preprocess_face_images(image, faces)
    embeddings = extract_face_embeddings(face_tensors)

    best_similarity = -1
    best_face = None

    # Parallelize similarity calculations
    with ThreadPoolExecutor() as executor:
        similarities = list(executor.map(lambda emb: compare_face_embeddings(emb, saved_embedding), embeddings))

    for i, similarity in enumerate(similarities):
        if similarity > best_similarity and similarity > similarity_threshold:
            best_similarity = similarity
            best_face = faces[i]

    return best_face, best_similarity

# Load the crowd image and detect faces
crowd_image = cv2.imread('test_group6.jpg')
net = load_yolo_model("yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

best_face, similarity = find_most_similar_face(crowd_image, net, saved_embedding)

# Draw the best matching face and show similarity score
if best_face is not None:
    (x, y, w, h) = best_face
    cv2.rectangle(crowd_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(crowd_image, f'Similarity: {similarity:.2f}', (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Save and display the resulting image
cv2.imwrite("matched_image.jpg", crowd_image)
plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
