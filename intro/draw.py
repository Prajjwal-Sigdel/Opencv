import numpy as np
import cv2 as cv

# Create a black image
img = np.full((512, 512, 3), [0, 0, 128], dtype=np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 10)

# Draw a circle
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Draw a Ellipse
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Draw a polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))

# Writting a text
font = cv.FONT_HERSHEY_PLAIN
cv.putText(img, 'Aayush is Gay', (10, 500), font,
           4, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow('Blue Line', img)
cv.waitKey(0)
cv.destroyAllWindows()
