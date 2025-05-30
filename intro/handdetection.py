import cv2
import numpy as np

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(
    'C:/Users/prajj/anaconda3/envs/opencv-env/Library/etc/haarcascades/haarcascade_frontalface_default.xml'
)

# Open the webcam
cap = cv2.VideoCapture(0)

# Read first frame for motion detection
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Face Detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        radius = max(w, h) // 2
        # Green circle on face
        cv2.circle(frame, center, radius, (0, 255, 0), 2)

    # Hand Movement Detection
    gray_blur = cv2.GaussianBlur(gray, (21, 21), 0)
    diff = cv2.absdiff(prev_gray, gray_blur)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours of moving regions
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) < 1000:  # Ignore small movements
            continue
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h),
                      (0, 0, 255), 2)  # Red box on movement

    # Show frame
    frame = cv2.flip(frame, 1)
    cv2.imshow('Face and Hand Movement Detection', frame)

    # Update previous frame
    prev_gray = gray_blur.copy()

    if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC
        break

cap.release()
cv2.destroyAllWindows()
