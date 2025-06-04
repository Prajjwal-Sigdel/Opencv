import cv2 as cv
import numpy as np

# Getting two images
img1 = cv.imread(
    'C:\\Users\\prajj\\repo\\opencv\\image_manipulation\\hero.jpg')
img2 = cv.imread(
    'C:\\Users\\prajj\\repo\\opencv\\image_manipulation\\logo.png')

# Checking if extracted properly
assert img1 is not None, "File could not be read, check with os.path.exists() "
assert img2 is not None, "File could not be read, check with os.path.exists() "

# Checking the size of two images before resizing
print('The size of first image: ', img1.size)
print('The size of second image: ', img2.size)

# Resizing the images for combination of images
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))


# Checking the size of two images after resizing
print('The size of first image: ', img1.size)
print('The size of second image: ', img2.size)

# Combining two images with proper ratio
comb = cv.addWeighted(img1, 0.7, img2, 0.3, 20)

# Displaying the combined image
cv.imshow('Combined_Image', comb)

# Assiging the exit key
cv.waitKey(0)
cv.destroyAllWindows()
