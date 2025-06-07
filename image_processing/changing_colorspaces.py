import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # HSV Ranges
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 70])

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 40, 255])

    lower_green = np.array([40, 70, 70])
    upper_green = np.array([80, 255, 255])

    # Create masks
    mask_black = cv.inRange(hsv, lower_black, upper_black)
    mask_white = cv.inRange(hsv, lower_white, upper_white)
    mask_green = cv.inRange(hsv, lower_green, upper_green)

    # Combine black and white masks
    bw_mask = cv.bitwise_or(mask_black, mask_white)

    # Create blank image for output (same shape as frame)
    output = np.zeros_like(frame)

    # Set black & white areas to white (255,255,255)
    output[bw_mask > 0] = [255, 255, 255]

    # Set green areas to red (0,0,255)
    output[mask_green > 0] = [0, 0, 255]

    # Show result
    cv.imshow('Binary + Green as Red', output)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
