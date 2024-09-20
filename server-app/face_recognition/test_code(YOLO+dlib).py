import cv2
import face_recognition
import numpy as np
import matplotlib.pyplot as plt

# Load saved face embedding from .npy file
saved_embedding = np.load('embeddings/person1.npy')

# YOLO face detection code remains unchanged
def load_yolo_model(config_path, weights_path):
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    return net

def detect_faces_yolo(image, net, confidence_threshold=0.5):
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getLayerNames()
    try:
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    except IndexError:
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    layer_outputs = net.forward(output_layers)
    height, width = image.shape[:2]
    boxes = []
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
                boxes.append((x, y, x + w, y + h))
    return boxes

# Extract face embeddings using dlib's face_recognition
def extract_face_embedding(face_image):
    face_encodings = face_recognition.face_encodings(face_image)
    if len(face_encodings) > 0:
        return face_encodings[0]
    return None

# Function to find the most similar face in the crowd
def find_most_similar_face(image, net, saved_embedding):
    faces = detect_faces_yolo(image, net)
    best_similarity = -1
    best_face = None

    for (x1, y1, x2, y2) in faces:
        face_image = image[y1:y2, x1:x2]
        embedding = extract_face_embedding(face_image)
        if embedding is not None:
            similarity = np.dot(embedding, saved_embedding) / (np.linalg.norm(embedding) * np.linalg.norm(saved_embedding))

            if similarity > best_similarity:
                best_similarity = similarity
                best_face = (x1, y1, x2, y2)

    return best_face, best_similarity

# Load the crowd image
crowd_image = cv2.imread('test_group3.jpg')
net = load_yolo_model("yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

# Find the most similar face in the crowd
best_face, similarity = find_most_similar_face(crowd_image, net, saved_embedding)

if best_face is not None:
    (x1, y1, x2, y2) = best_face
    cv2.rectangle(crowd_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(crowd_image, f'Similarity: {similarity:.2f}', (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display final image with the bounding box of the most similar face
cv2.imwrite("matched_image.jpg", crowd_image)
plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
