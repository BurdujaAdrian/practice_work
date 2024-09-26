import numpy as np

# Load the .npy file
data = np.load('embeddings/person1.npy')

# Display the contents
print(data)

# If you want to see the shape or type of the data:
print("Shape:", data.shape)
print("Data type:", data.dtype)
