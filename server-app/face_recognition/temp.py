import torch
import torch.nn as nn
import torch.nn.functional as F
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from torchvision.transforms.functional import to_tensor, to_pil_image
from PIL import Image
import functools
img = cv2.imread("test_group1.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
cv2.imwrite("pre_display_image_check.jpg", cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 90])
plt.imshow(img_rgb)
plt.show()