import cv2
import numpy as np
import matplotlib.pyplot as plt

net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')

image = cv2.imread('test_group3.jpg')
(h, w) = image.shape[:2]

blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
net.setInput(blob)

detections = net.forward()

output_image = image.copy()

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.10:
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        cv2.rectangle(output_image, (startX, startY), (endX, endY), (0, 255, 0), 2)

image_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

def detect_faces_multiscale(image, net, min_confidence=0.11):
    (h, w) = image.shape[:2]
    scale_factors = [1.0, 0.9, 0.8, 0.7]
    faces = []

    for scale in scale_factors:
        resized_img = cv2.resize(image, (int(w * scale), int(h * scale)))
        blob = cv2.dnn.blobFromImage(cv2.resize(resized_img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > min_confidence:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h]) / scale
                faces.append(box.astype("int"))
    return faces

faces = detect_faces_multiscale(image, net)

pre_nms_image = image.copy()
for (startX, startY, endX, endY) in faces:
    cv2.rectangle(pre_nms_image, (startX, startY), (endX, endY), (255, 0, 0), 2)

image_rgb_pre_nms = cv2.cvtColor(pre_nms_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb_pre_nms)
plt.axis('off')
plt.show()

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

faces_nms = non_max_suppression(faces)

final_image = image.copy()
for (startX, startY, endX, endY) in faces_nms:
    cv2.rectangle(final_image, (startX, startY), (endX, endY), (0, 255, 0), 2)

image_rgb_nms = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb_nms)
plt.axis('off')
plt.show()
