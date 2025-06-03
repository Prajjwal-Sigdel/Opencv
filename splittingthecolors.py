import cv2 as cv
import numpy as np

# Load image
# Replace with your image path
img = cv.imread('C:\\Users\\prajj\\repo\\opencv\\hero.jpg')

# Split channels
b, g, r = cv.split(img)

# Create blank (zero) channel
zeros = np.zeros_like(b)

# Merge to show each color in grayscale form
only_blue = cv.merge((b, zeros, zeros))
only_green = cv.merge((zeros, g, zeros))
only_red = cv.merge((zeros, zeros, r))

# Show them
cv.imshow('Red only', img[:, :, 0])
cv.imshow('Only Blue (Grayscale)', only_blue)
cv.imshow('Only Green (Grayscale)', only_green)
cv.imshow('Only Red (Grayscale)', only_red)

cv.waitKey(0)
cv.destroyAllWindows()
