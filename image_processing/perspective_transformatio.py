import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('C:\\Users\\prajj\\repo\\opencv\\image_processing\\sudoku.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols, ch = img.shape

pts1 = np.float32([
    [29.7, 26.7],    # Top-left
    [160.6, 7.4],   # Top-right
    [58.8, 130.6],   # Bottom-left
    [197.9, 83.4]   # Bottom-right
])

pts2 = np.float32([
    [0, 0],        # Top-left
    [250, 0],      # Top-right
    [0, 200],      # Bottom-left
    [250, 200]     # Bottom-right
])


M = cv.getPerspectiveTransform(pts1, pts2)

dst = cv.warpPerspective(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
