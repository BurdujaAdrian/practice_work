import cv2
from facenet_pytorch import MTCNN
from PIL import Image
import matplotlib.pyplot as plt

def detect_and_draw_faces(image):
    # Initialize MTCNN face detector
    mtcnn = MTCNN(keep_all=True, post_process=False, min_face_size=5)

    # Convert the image to PIL format for MTCNN
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Detect faces
    boxes, _ = mtcnn.detect(image_pil)

    # Draw bounding boxes on the image
    if boxes is not None:
        for box in boxes:
            (x1, y1, x2, y2) = box.astype(int)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            print(f"Bounding box: {(x1, y1, x2, y2)}")

    # Display the image with bounding boxes
    cv2.imshow("Detected Faces", image)
    cv2.imwrite("Test_file.jpg",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
if __name__ == "__main__":
    image_path = 'test_group3.jpg'  # Replace with your image path
    image = cv2.imread(image_path)
    detect_and_draw_faces(image)
