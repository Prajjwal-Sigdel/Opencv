import cv2 as cv
import numpy as np

# Load image
# Fixed typo in file extension
img = cv.imread('C:\\Users\\prajj\\repo\\opencv\\hero.jpg')

# Check if image is loaded
if img is None:
    print("Error loading image")
    exit()

# Modify and show the modified pixel
for i in range(100):
    img[i, i] = [0, 0, 0]
cv.imshow('Hello', img)

# Create a blank image with the same shape
dominant = np.zeros_like(img)

# Get the indexes of the maximum channel per pixel
max_idx = np.argmax(img, axis=2)

# Set the maximum value to 255 for the dominant channel
for i in range(3):  # B, G, R channels
    dominant[:, :, i] = (max_idx == i) * 255

# Show the result
cv.imshow('Dominant Color Highlighted', dominant)

print(img.shape)
print(img.size)

cv.waitKey(0)
cv.destroyAllWindows()
