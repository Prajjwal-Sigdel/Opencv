# importing numpy and cv2 libraries for image processing and manipulation
import numpy as nb
import cv2 as cv

# accessing the camera of this decive and checking if it went well
cap = cv.VideoCapture(
    'C:\\Users\\prajj\\OneDrive\\Pictures\\Camera Roll\\aayush_intro.mp4')
if not cap.isOpened():
    print("Cannot open camrea !!!")
    exit()
while True:

    # reading a frame and checking for true value of ret
    ret, frame = cap.read()

    if not ret:
        print("AN error occured")
        break

    # working with frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2HLS)

    # Displaying the image taken
    cv.imshow('AAyush is Gay', cv.flip(gray, 2))

    # checking if the user wants to exit the window he is in
    if cv.waitKey(1) == ord('q'):
        break

# releasing the hardware components used
cap.release()
cv.destroyAllWindows()
