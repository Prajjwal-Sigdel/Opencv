import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\prajj\\repo\\opencv\\image_processing\\hero.jpg')
assert img is not None, "File could not be read, check with os.path.exists()"

cv.imshow('Original image', img)

res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

cv.imshow('Resized image', res)
cv.waitKey(0)
cv.destroyAllWindows()
