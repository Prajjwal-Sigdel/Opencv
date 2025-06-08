import numpy as np
import cv2 as cv

img = cv.imread(
    'C:\\Users\\prajj\\repo\\opencv\\image_processing\\hero.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols = img.shape

M1 = np.float32([[1, 0, 50], [0, 1, 100]])
dst1 = cv.warpAffine(img, M1, (cols-100, rows-50))

M2 = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
dst2 = cv.warpAffine(img, M2, (cols, rows))

cv.namedWindow('Original', cv.WINDOW_NORMAL)
cv.namedWindow('Translate', cv.WINDOW_NORMAL)
cv.namedWindow('Rotate', cv.WINDOW_NORMAL)
cv.imshow('Original', img)
cv.imshow('Translate', dst1)
cv.imshow('Rotate', dst2)


cv.waitKey(0)
cv.destroyAllWindows()
