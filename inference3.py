from inference_sdk import InferenceHTTPClient
import cv2
import mediapipe as mp
import pyautogui
from dotenv import load_dotenv
import os
import numpy as np

# Load environment variables
load_dotenv()
api_key = os.getenv("ROBOFLOW_API_KEY")

# Set pyautogui settings
pyautogui.PAUSE = 0.05  # Set the pause to 50 milliseconds
pyautogui.MINIMUM_DURATION = 0.01  # Set the minimum duration to 10 milliseconds

# Initialize the webcam video capture
video = cv2.VideoCapture(0)

# Initialize Mediapipe hand tracking
handGesture = mp.solutions.hands.Hands(
    static_image_mode=False,  # Continuous tracking, better for video.
    max_num_hands=1,  # Track only one hand for faster performance.
    min_detection_confidence=0.5,  # Adjust detection confidence.
    min_tracking_confidence=0.5,  # Adjust tracking confidence.
    model_complexity=0  # Adjust model complexity for faster performance.
)

# Mediapipe drawing tools
drawingTools = mp.solutions.drawing_utils

# Get screen dimensions for mouse control
screenWidth, screenHeight = pyautogui.size()

# Initialize RoboFlow client
client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=api_key
)

# Function to pause the game by simulating an "ESC" keypress
def pause_game():
    pyautogui.press('esc')

# State to track whether the mouse is clicked (for dragging)
globalClickState = False

def close_fist():
    global globalClickState
    if globalClickState: return
    pyautogui.mouseDown()  # Simulate mouse click and hold (dragging)
    globalClickState = True

def open_hand():
    global globalClickState
    if not globalClickState: return
    pyautogui.mouseUp()  # Release the mouse button (stop dragging)
    globalClickState = False

# Parameters for smoothing the mouse movement
previousMouseX, previousMouseY = None, None
smoothFactor = 0.3  # Adjust this value to control the smoothness (0.1-0.5 is a good range)

# Smoothing function for the mouse movement
def smooth_movement(currentX, currentY, previousX, previousY, smoothFactor):
    if previousX is None or previousY is None:
        return currentX, currentY  # No previous position, just return current position
    # Interpolate the movement to make it smoother
    newX = previousX + smoothFactor * (currentX - previousX)
    newY = previousY + smoothFactor * (currentY - previousY)
    return newX, newY

# Main loop to capture video and control mouse
while True:
    _, frame = video.read()  # Capture a frame from the webcam
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally (mirror effect)
    frameHeight, frameWidth, _ = frame.shape  # Get frame dimensions
    rgbConvertedFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Mediapipe
    output = handGesture.process(rgbConvertedFrame)  # Process the frame for hand tracking
    hands = output.multi_hand_landmarks  # Get the detected hands
    
    if hands:  # If hands are detected
        hand = hands[0]  # Get the first hand
        drawingTools.draw_landmarks(frame, hand)  # Draw hand landmarks on the frame
        landmarks = hand.landmark  # Get the hand landmarks
        lmList = []  # List to store landmarks with IDs and positions
        
        # Loop through the landmarks and store the positions
        for id, landmark in enumerate(landmarks):
            cx, cy = int(landmark.x * frameWidth), int(landmark.y * frameHeight)
            lmList.append([id, cx, cy])
            if id == 5:  # Use the index finger base (landmark 5) for mouse control
                x = int(landmark.x * frameWidth)
                y = int(landmark.y * frameHeight)
                cv2.circle(img=frame, center=(x, y), radius=30, color=(0, 255, 255))  # Draw a circle on the finger
                
                # Calculate new mouse position (in screen coordinates)
                mousePositionX = screenWidth / frameWidth * x
                mousePositionY = screenHeight / frameHeight * y
                
                # Smooth the mouse movement
                smoothedX, smoothedY = smooth_movement(mousePositionX, mousePositionY, previousMouseX, previousMouseY, smoothFactor)
                
                # Move the mouse to the smoothed position
                pyautogui.moveTo(smoothedX, smoothedY)
                
                # Update the previous mouse position
                previousMouseX, previousMouseY = smoothedX, smoothedY
        
        # Gesture logic for determining when to "click" or "release"
        indexX = indexY = indexMid = handBottomX = handBottomY = pinkyX = pinkyY = 0
        for lms in lmList:
            if lms[0] == 7:  # Index finger tip
                indexX, indexY = lms[1], lms[2]
            elif lms[0] == 5:  # Index finger base
                indexMid = lms[2]
            elif lms[0] == 19:  # Pinky finger tip
                pinkyX, pinkyY = lms[1], lms[2]
            elif lms[0] == 0:  # Hand bottom (wrist)
                handBottomX, handBottomY = lms[1], lms[2]

        # Check if the user is making a fist (for clicking)
        if (indexY < handBottomY) and (indexY > indexMid):
            cv2.rectangle(rgbConvertedFrame, (indexX, indexY), (pinkyX, handBottomY), (0, 0, 255), 2)
            close_fist()  # Simulate mouse click
        else:
            open_hand()  # Release mouse click

    # Display the frame (optional for debugging)
    # cv2.imshow('Virtual Mouse', frame)
    # cv2.waitKey(1)
