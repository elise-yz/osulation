from inference_sdk import InferenceHTTPClient
import cv2
import mediapipe as mp
from dotenv import load_dotenv
from pynput import mouse, keyboard
from cv2_enumerate_cameras import enumerate_cameras
import pyautogui
import os
import time

# Load environment variables
load_dotenv()
api_key = os.getenv("ROBOFLOW_API_KEY")

# Initialize webcam and hand gesture recognition
CAMERA_NAME = "Logitech Webcam C925e" # Name of the webcame
CAMERA_INDEX = 0

for camera_info in enumerate_cameras():
    if camera_info.name == CAMERA_NAME:
        CAMERA_INDEX = camera_info.index

video = cv2.VideoCapture(CAMERA_INDEX) # Open video based on camera index
handGesture = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.5,
    model_complexity=0
)

drawingTools = mp.solutions.drawing_utils
screenWidth, screenHeight = pyautogui.size()

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="fQDjqbkxviXzBXoSjACM"
)

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

globalClickState = False

# Pause game using 'esc' key
def pause_game():
    keyboard_controller.press('esc')

# Close fist (for dragging)
def close_fist():
    global globalClickState
    if globalClickState: return
    mouse_controller.press(mouse.Button.left)
    globalClickState = True

# Open hand (for stopping drag)
def open_hand():
    global globalClickState
    if not globalClickState: return
    mouse_controller.release(mouse.Button.left)
    globalClickState = False

# Smoothing factor for mouse movement
previousMouseX, previousMouseY = None, None
smoothFactor = 0.2 # Smoothing factor (0.1 - 0.5 is generally good)

# Smoothing function
def smooth_movement(currentX, currentY, previousX, previousY, smoothFactor):
    if previousX is None or previousY is None:
        return currentX, currentY
    newX = previousX + smoothFactor * (currentX - previousX)
    newY = previousY + smoothFactor * (currentY - previousY)
    return newX, newY

# Main loop for capturing video and controlling mouse
while True:
    _, frame = video.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a mirror effect
    frameHeight, frameWidth, _ = frame.shape
    frameWidth *= 0.4 # Reduce the frame width for better performance
    frameHeight *= 0.4 # Reduce the frame height for better performance
    rgbConvertedFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = handGesture.process(rgbConvertedFrame)
    hands = output.multi_hand_landmarks


    if hands:
        hand = hands[0]
        drawingTools.draw_landmarks(frame, hand)
        landmarks = hand.landmark
        lmList = []

        # Collect landmarks with coordinates
        for id, landmark in enumerate(landmarks):
            cx, cy = int(landmark.x * frameWidth), int(landmark.y * frameHeight)
            lmList.append([id, cx, cy])
            if id == 5:  # Index finger base (for mouse control)
                x = cx
                y = cy
                cv2.circle(img=frame, center=(x, y), radius=30, color=(0, 255, 255))

                # Scale to screen dimensions
                mousePositionX = screenWidth / frameWidth * x
                mousePositionY = screenHeight / frameHeight * y

                # Smooth the mouse movement
                smoothedX, smoothedY = smooth_movement(mousePositionX, mousePositionY, previousMouseX, previousMouseY, smoothFactor)

                # Move the mouse to smoothed position
                mouse_controller.position = (smoothedX, smoothedY)

                # Update previous position
                previousMouseX, previousMouseY = smoothedX, smoothedY

        # Gesture logic to detect fist closure
        indexX, indexY, indexMid, handBottomY, pinkyX = 0, 0, 0, 0, 0
        for lms in lmList:
            if lms[0] == 7:
                indexX, indexY = lms[1], lms[2]
            elif lms[0] == 5:
                indexMid = lms[2]
            elif lms[0] == 19:
                pinkyX = lms[1]
            elif lms[0] == 0:
                handBottomY = lms[2]

        # Check for fist gesture (for dragging)
        if (indexY < handBottomY) and (indexY > indexMid):
            cv2.rectangle(rgbConvertedFrame, (indexX, indexY), (pinkyX, handBottomY), (0, 0, 255), 2)
            close_fist()
        else:
            open_hand()


    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()
