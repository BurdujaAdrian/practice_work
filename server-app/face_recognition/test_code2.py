import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the pre-trained model
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')


def detect_faces(image, net, confidence_threshold):
    (h, w) = image.shape[:2]

    # Prepare the image for the model by resizing and creating a blob
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    faces = []

    # Loop through the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            # Compute the coordinates of the face bounding box
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            faces.append((startX, startY, endX, endY))

    return faces


def non_max_suppression(boxes, overlapThresh=0.3):
    if len(boxes) == 0:
        return []

    boxes = np.array(boxes)
    pick = []
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)

    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[idxs[:last]]
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))

    return boxes[pick].astype("int")


# Load your high-resolution image
image = cv2.imread('test_group4.jpg')

# Detect faces in the high-resolution image
faces = detect_faces(image, net, confidence_threshold=0.15)

# Apply non-max suppression to reduce overlapping face boxes
faces_nms = non_max_suppression(faces)

# Draw the final face detections on the image
final_image = image.copy()
for (startX, startY, endX, endY) in faces_nms:
    cv2.rectangle(final_image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# Convert the image to RGB and display it
image_rgb_nms = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb_nms)
plt.axis('off')
plt.show()
