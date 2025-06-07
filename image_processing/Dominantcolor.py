import cv2 as cv
import numpy as np

# Defining the Bucket function for 8 respective color groups


def Bucket_frame(frame, step=64):
    b = (frame[:, :, 0]//step)*step
    g = (frame[:, :, 1]//step)*step
    r = (frame[:, :, 2]//step)*step
    Buck = np.stack([b, g, r], axis=2).astype(np.uint8)
    return Buck

# def three_color_frame(frame):
#     b = frame[:, :, 0]
#     g = frame[:, :, 1]
#     r = frame[:, :, 2]

#     # Create an empty output image
#     output = np.zeros_like(frame)

#     # For each pixel, find max channel and assign pure color accordingly
#     max_channel = np.argmax(frame, axis=2)

#     output[max_channel == 0] = [255, 0, 0]  # Blue
#     output[max_channel == 1] = [0, 255, 0]  # Green
#     output[max_channel == 2] = [0, 0, 255]  # Red

#     return output


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
    Output = cv.imshow('Absolute Dominion', Bucket_frame(frame))

    # esc to quit
    if cv.waitKey(1) & 0xFF == 27:
        break

# Releasing the camera from usage and exiting the window
cap.release()
cv.destroyAllWindows()
