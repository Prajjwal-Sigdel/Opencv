import cv2 as cv
import numpy as np

# Getting two images
img1 = cv.imread(
    'C:\\Users\\prajj\\repo\\opencv\\image_manipulation\\hero.jpg')
img2 = cv.imread(
    'C:\\Users\\prajj\\repo\\opencv\\image_manipulation\\logo.png')

# Ensure both images were read
assert img1 is not None, "img1 not found"
assert img2 is not None, "img2 not found"

# Resize img2 to match img1 if needed
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))

# Method 1: Saturated addition (OpenCV)
# added_img = cv.add(img1, img2)

# Method 2: Modulo addition (NumPy) — not recommended for visuals
added_img = img1 + img2

# Show the result
cv.imshow("Added Image", added_img)
cv.waitKey(0)
cv.destroyAllWindows()
