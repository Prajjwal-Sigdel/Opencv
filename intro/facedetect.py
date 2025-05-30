import cv2

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(
    'C:/Users/prajj/anaconda3/envs/opencv-env/Library/etc/haarcascades/haarcascade_frontalface_default.xml')


# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale (Haar cascade works on gray images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces (returns list of rectangles)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5)

    # Draw circle over each detected face
    for (x, y, w, h) in faces:
        # Calculate center and radius
        center = (x + w // 2, y + h // 2)
        radius = max(w, h) // 2
        cv2.circle(frame, center, radius, (0, 255, 0), 2)  # Green circle

    # flip the frame
    frame = cv2.flip(frame, 1)

    # Show the frame
    cv2.imshow('Face Detection with Circle', frame)

    # Exit on pressing 'ESC'
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
