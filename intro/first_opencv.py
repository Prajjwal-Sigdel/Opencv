import cv2
import sys
# Load an image
img = cv2.imread('.\\hero.jpg', cv2.IMREAD_COLOR_RGB)

# Show the image in a window
cv2.imshow('Image', img)

# Wait for a key and close
k = cv2.waitKey(0)
cv2.destroyAllWindows()
if k == ord("s"):
    cv2.imwrite("Stupid.jpg", img)
