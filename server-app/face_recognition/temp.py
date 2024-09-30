import cv2

if hasattr(cv2.dnn_superres, 'DnnSuperResImpl_create'):
    print("DnnSuperResImpl_create() is available!")
else:
    print("DnnSuperResImpl_create() is not available.")
