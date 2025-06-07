import cv2 as cv
import numpy as np

# Defining the Bucket function for 8 respective color groups


def Bucket_frame(frame, step=32):

    h, w, _ = frame.shape

    # Create a copy of frame
    output = frame.copy()

    # select the region of change
    region = output[0:h, 0:w//2]

    # Applying bucketing on the region
    b = (region[:, :, 0]//step)*step
    g = (region[:, :, 1]//step)*step
    r = (region[:, :, 2]//step)*step

    # Stack into a new Image
    Buck = np.stack([b, g, r], axis=2).astype(np.uint8)

    # Putting the Bucketed Region to the output frame
    output[0:h, 0:w//2] = Buck

    return output


# capturing the live footage from camera
cap = cv.VideoCapture(0)

while True:

    # Read every frame of the captured image
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    # Checking if the frame is succesfully extracted
    if ret is None:
        print("Unable to extract the frames from the video. Error Exiting !!! 1,2,3...")

    # Calling the function to send the each for grouping of colors:
    Output = Bucket_frame(frame)

    # Displaying the final result
    cv.imshow('The is a legendary thing', Output)

    # esc to quit
    if cv.waitKey(1) & 0xFF == 27:
        break

# Releasing the camera from usage and exiting the window
cap.release()
cv.destroyAllWindows()
