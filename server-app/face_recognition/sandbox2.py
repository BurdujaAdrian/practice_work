import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time

i = 0  # Global variable to track the image index

# Create a new directory to save grouped face images
os.makedirs('output_faces/grouped_faces', exist_ok=True)

# Load super-resolution model
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel("model-weights/ESPCN_x4.pb")
sr.setModel("espcn", 4)  # Set the model to upscale by a factor of 4

# Logarithmic filter for contrast enhancement
def apply_log_filter(image):
    image_log = np.log1p(np.array(image, dtype="float32"))
    cv2.normalize(image_log, image_log, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(image_log)

# YOLO face detection
def load_yolo_model(config_path, weights_path):
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    return net

def detect_faces_yolo(image, net, confidence_threshold=0.3, nms_threshold=0.0):
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

    # Apply non-maximum suppression to remove overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)

    # Ensure indices are correctly handled
    final_boxes = []
    if len(indices) > 0:
        if isinstance(indices[0], (list, np.ndarray)):
            final_boxes = [boxes[i[0]] for i in indices]  # List of lists case
        else:
            final_boxes = [boxes[i] for i in indices]  # Flat list case

    return final_boxes

# Save detected faces with and without enhancements
def save_faces(image, boxes):
    global i  # Declare i as a global variable to modify it

    for (x, y, w, h) in boxes:
        face_image = image[y:y + h, x:x + w]

        # Create a sub-folder for each face group
        folder_path = f'output_faces/grouped_faces/face_group_{i}'
        os.makedirs(folder_path, exist_ok=True)

        # Save original face
        cv2.imwrite(f"{folder_path}/face_{i}_original.jpg", face_image)

        # Apply super-resolution
        face_sr = sr.upsample(face_image)
        cv2.imwrite(f"{folder_path}/face_{i}_super_resolution.jpg", face_sr)

        # Apply logarithmic filter
        face_log = apply_log_filter(face_sr)
        cv2.imwrite(f"{folder_path}/face_{i}_log_filtered.jpg", face_log)

        i += 1

# Load the crowd image
crowd_image = cv2.imread('test_group1.jpg')
net = load_yolo_model("model-weights/yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

# Detect faces in the crowd image
faces = detect_faces_yolo(crowd_image, net)

# Save detected faces
save_faces(crowd_image, faces)

# Draw bounding boxes around detected faces and display the final image
for (x, y, w, h) in faces:
    cv2.rectangle(crowd_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

cv2.imwrite("output_faces/detected_faces.jpg", crowd_image)
