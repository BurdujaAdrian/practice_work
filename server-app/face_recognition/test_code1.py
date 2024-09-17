import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the pre-trained model
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')


# Sliding window function
def sliding_window(image, step_size, window_size):
    # Slide a window across the image
    for y in range(0, image.shape[0], step_size):
        for x in range(0, image.shape[1], step_size):
            yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])


def detect_faces(image, net, confidence_threshold, window_size=(100, 100), step_size=90):
    (h, w) = image.shape[:2]
    faces = []

    # Slide a window over the image
    for (x, y, window) in sliding_window(image, step_size, window_size):
        if window.shape[0] != window_size[1] or window.shape[1] != window_size[0]:
            continue

            # Prepare the window for the model
        blob = cv2.dnn.blobFromImage(cv2.resize(window, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()

        # Loop through the detections and adjust for window position
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > confidence_threshold:
                box = detections[0, 0, i, 3:7] * np.array(
                    [window_size[0], window_size[1], window_size[0], window_size[1]])
                (startX, startY, endX, endY) = box.astype("int")

                # Adjust coordinates for the window's position in the original image
                faces.append((x + startX, y + startY, x + endX, y + endY))

    return faces


# Non-max suppression function remains unchanged
def non_max_suppression(boxes, overlapThresh=0.1):
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
faces = detect_faces(image, net, confidence_threshold=0.5)

# Apply non-max suppression to reduce overlapping face boxes
faces_nms = non_max_suppression(faces)

# Draw the final face detections on the image
final_image = image.copy()
for (startX, startY, endX, endY) in faces_nms:
    cv2.rectangle(final_image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# Convert the image to RGB and display it
image_rgb_nms = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)
plt.imshow(final_image)
plt.axis('off')
plt.show()


