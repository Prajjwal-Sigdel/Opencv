import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Create a fullscreen window
cv.namedWindow('frame', cv.WINDOW_NORMAL)
cv.setWindowProperty('frame', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv.flip(frame, 1)

    # Resizing the frame of video feed
    frame = cv.resize(frame, (1522, 864))

    # Draw a diagonal blue line with thickness of 5 px
    cv.line(frame, (0, 0), (511, 511), (255, 0, 0), 10)

    # Draw a circle
    cv.circle(frame, (447, 63), 63, (0, 0, 255), -1)

    # Draw an Ellipse
    cv.ellipse(frame, (256, 256), (100, 50), 0, 0, 180, 255, -1)

    # Draw a polygon
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(frame, [pts], True, (0, 255, 255))

    # Write a text (please use appropriate messages)
    font = cv.FONT_HERSHEY_PLAIN
    cv.putText(frame, 'OpenCV Drawing', (10, 500),
               font, 4, (255, 255, 255), 2, cv.LINE_AA)

    # Display the resulting frame
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
