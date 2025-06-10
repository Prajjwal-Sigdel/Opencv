import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load a static image and apply different thresholding methods
img = cv.imread(
    'C:\\Users\\prajj\\repo\\opencv\\image_processing\\hero.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check the path"

ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY',
          'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Open webcam and apply real-time thresholding
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Unable to extract frames !!!")
        break

    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
    cv.imshow('The undisputed titan', thresh)

    if cv.waitKey(1) & 0xFF == 27:  # Press Esc to exit
        break

cap.release()
cv.destroyAllWindows()
