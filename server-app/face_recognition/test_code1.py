import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

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

    start_time = time.time()  # Start timing
    layer_outputs = net.forward(output_layers)
    detection_time = time.time() - start_time  # Calculate detection time
    print(f"Face detection took: {detection_time:.2f} seconds")

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
    final_boxes = []

    if len(indices) > 0:
        if isinstance(indices[0], (list, np.ndarray)):
            final_boxes = [boxes[i[0]] for i in indices]
        else:
            final_boxes = [boxes[i] for i in indices]

    return final_boxes

# Load the crowd image
crowd_image = cv2.imread('test_group3.jpg')
net = load_yolo_model("model-weights/yolov3-face.cfg", "model-weights/yolov3-wider_16000.weights")

# Detect faces and measure time taken
faces = detect_faces_yolo(crowd_image, net)

# Draw bounding boxes around detected faces and display the final image
for (x, y, w, h) in faces:
    cv2.rectangle(crowd_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save and display the final image
cv2.imwrite("output_faces/detected_faces.jpg", crowd_image)
plt.imshow(cv2.cvtColor(crowd_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
