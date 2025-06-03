import cv2 as cv
import numpy as np

live = cv.VideoCapture(0)
if not live.isOpened():
    print("Unable to record from camera !!!")
    exit()

cv.namedWindow('Toggle_live')
cv.createTrackbar('Blue', 'Toggle_live', 1, 1, lambda x: None)
cv.createTrackbar('Green', 'Toggle_live', 1, 1, lambda x: None)
cv.createTrackbar('Red', 'Toggle_live', 1, 1, lambda x: None)

while True:
    ret, frame = live.read()
    if not ret:
        print('The frame is not captured')

    # filp the captured frame
    frame = cv.flip(frame, 1)

    # Getting the trackbar positions
    b = cv.getTrackbarPos('Blue', 'Toggle_live')
    g = cv.getTrackbarPos('Green', 'Toggle_live')
    r = cv.getTrackbarPos('Red', 'Toggle_live')

    # Copy the frame and Modified live capture according to the trackbar changes

    Modified = frame.copy()
    if b == 0:
        Modified[:, :, 0] = 0  # Turns off blue
    if g == 0:
        Modified[:, :, 1] = 0  # Turns off green
    if r == 0:
        Modified[:, :, 2] = 0  # Turns off red

    # Show the modified frame
    cv.imshow('Modified Capture', Modified)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release Resources
live.release()
cv.destroyAllWindows()
