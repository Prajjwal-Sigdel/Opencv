import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load and preprocess image
img = cv.imread(
    'C:\\Users\\prajj\\repo\\opencv\\image_processing\\hero.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img = cv.medianBlur(img, 5)

# Apply thresholding
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                           cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY, 11, 2)

# Display results using matplotlib
titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
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

    frame = cv.flip(frame, 1)  # Mirror the frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    apply_blur = True  # Set Blur according to Boolean
    if apply_blur:
        gray = cv.medianBlur(gray, 5)

    thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,  # Set either cv.ADAPTIVE_THRESH_C OR cv.ADAPTIVE_THRESH_GUSSIAN_C
                                  cv.THRESH_BINARY, 11, 2)

    cv.imshow('The undisputed titan', thresh)

    if cv.waitKey(1) & 0xFF == 27:  # Press Esc to exit
        break

cap.release()
cv.destroyAllWindows()
