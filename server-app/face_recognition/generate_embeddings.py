import tensorflow as tf
import numpy as np
import cv2
import os

# Function to load a frozen graph (.pb file)
def load_graph(pb_file):
    with tf.io.gfile.GFile(pb_file, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
    return graph_def

# Load the FaceNet frozen graph
graph_def = load_graph(r'model-weights\20180408-102900\20180408-102900.pb')

# Create a new graph and import the frozen graph into it
with tf.compat.v1.Graph().as_default() as graph:
    tf.import_graph_def(graph_def, name='')

# YOLO Face Detection
def detect_faces_yolo(image, net, confidence_threshold=0.5, nms_threshold=0.4):
    height, width = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (832, 832), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for output in detections:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > confidence_threshold:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
    faces = []
    if len(indices) > 0:
        for i in indices.flatten():
            box = boxes[i]
            x, y, w, h = box
            faces.append((x, y, x + w, y + h))

    return faces

# Function to extract face embedding using the loaded frozen graph
def extract_face_embedding(face_image):
    face_image = cv2.resize(face_image, (160, 160))
    face_image = face_image.astype('float32') / 255.0
    face_image = np.expand_dims(face_image, axis=0)

    # Access the input, output, and phase_train tensors by name
    input_tensor = graph.get_tensor_by_name('input:0')
    output_tensor = graph.get_tensor_by_name('embeddings:0')
    phase_train_tensor = graph.get_tensor_by_name('phase_train:0')

    # Create a session to run the graph
    with tf.compat.v1.Session(graph=graph) as sess:
        # Set phase_train to False for inference
        embedding = sess.run(output_tensor, feed_dict={input_tensor: face_image, phase_train_tensor: False})

    return embedding.flatten()

# Load YOLO model for face detection
net = cv2.dnn.readNet('model-weights/yolov3-wider_16000.weights', 'yolov3-face.cfg')
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

# Load the image that may contain multiple faces or objects
image = cv2.imread('Artur.jpg')

# Detect faces using YOLO
faces = detect_faces_yolo(image, net)

if len(faces) == 0:
    print("No faces detected!")
else:
    # Process only the first face (if multiple faces are found, process others as needed)
    for i, (startX, startY, endX, endY) in enumerate(faces):
        face_image = image[startY:endY, startX:endX]  # Crop the face
        # Extract the embedding for the face
        face_embedding = extract_face_embedding(face_image)

        # Ensure the 'embeddings' directory exists
        os.makedirs('embeddings', exist_ok=True)

        # Save the embedding as a .npy file
        file_name = f'embeddings/person{2}.npy'
        np.save(file_name, face_embedding)
        print(f"Face {i+1} embedding saved as {file_name}")

        # Optionally, draw a bounding box around the detected face for visualization
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # Display the image with face bounding boxes
    cv2.imshow('Faces detected', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
