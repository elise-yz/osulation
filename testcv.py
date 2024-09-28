import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 1: Initialize MediaPipe Gesture Recognizer
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

# Initialize video capture
cap = cv2.VideoCapture(0)  # 0 for the default camera

# Function to display gesture and landmarks
def display_gesture(image, gesture, hand_landmarks):
    if hand_landmarks:
        for hand in hand_landmarks:
            for landmark in hand.landmark:
                h, w, c = image.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(image, (cx, cy), 5, (0, 255, 0), -1)  # Draw hand landmarks

    cv2.putText(image, f'Gesture: {gesture.category_name}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Start capturing video
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the image to the format required by MediaPipe
    mp_image = mp.Image.create_from_file(frame)

    # Recognize gestures
    recognition_result = recognizer.recognize(mp_image)

    # Get the top gesture and hand landmarks
    if recognition_result.gestures:
        top_gesture = recognition_result.gestures[0][0]
        hand_landmarks = recognition_result.hand_landmarks
    else:
        top_gesture = None
        hand_landmarks = []

    # Display the gesture and landmarks on the frame
    if top_gesture:
        display_gesture(frame, top_gesture, hand_landmarks)

    # Show the frame
    cv2.imshow('Gesture Recognizer', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
