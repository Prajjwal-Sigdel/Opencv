import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('C:\\Users\\prajj\\repo\\opencv\\images\\hero.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv.getAffineTransform(pts1, pts2)

dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow('Original', img)
# cv.imshow('Affined', dst)

plt.subplot(5, 5, 13), plt.imshow(cv.cvtColor(
    img, cv.COLOR_BGR2RGB)), plt.title('Input')
plt.subplot(1, 2, 2), plt.imshow(cv.cvtColor(
    dst, cv.COLOR_BGR2RGB)), plt.title('Output')
plt.show()
q
cv.waitKey(0)
cv.destroyAllWindows()
