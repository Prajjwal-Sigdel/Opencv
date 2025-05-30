import cv2 as cv
import numpy as np

img = np.full((512, 512, 3), 255, dtype=np.uint8)

cv.ellipse(img, (256, 170), (90, 90), 0, 120, 420, (0, 0, 255), -1)
cv.ellipse(img, (256, 170), (50, 50), 0, 0, 360, (255, 255, 255), -1)

cv.ellipse(img, (170, 340), (90, 90), 0, -30, 270, (0, 255, 0), -1)
cv.ellipse(img, (170, 340), (50, 50), 0, 0, 360, (255, 255, 255), -1)

cv.ellipse(img, (360, 340), (90, 90), 0, -60, 240, (255, 0, 0), -1)
cv.ellipse(img, (360, 340), (50, 50), 0, 0, 360, (255, 255, 255), -1)


cv.imshow("The Logo : ", img)
cv.waitKey(0)
