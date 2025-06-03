import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\prajj\\repo\\opencv\\diddy.jpg')

# Show the original image
cv.imshow('Before party', img)

# Cut and paste some heads
ball = img[236: 500, 606: 870]
img[232: 496, 228: 492] = ball

# Remving the respective channel 0 or 1 or 2 from the image so here the blue element is missing on every pixel
img[:, :, 2] = 0

print(ball.shape)
# print(hello.shape)

cv.imshow('Diddy party', img)

cv.waitKey(0)
cv.destroyAllWindows()
