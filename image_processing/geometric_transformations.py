import numpy as np
import cv2 as cv

img = cv.imread('../image_processing/diddy.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

# OR

height, width = img.shape[:2]
res = cv.resize(img, (4*width, 4*height), interpolation=cv.INTER_CUBIC)

cv.imshow('Resized Image', res)

cv.waitKey(0)
cv.destroyAllWindows()
