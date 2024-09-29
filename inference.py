from inference_sdk import InferenceHTTPClient

import cv2
import mediapipe as mp
import pyautogui
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ROBOFLOW_API_KEY")

pyautogui.PAUSE = 0.05  # Set the pause to 50 milliseconds
pyautogui.MINIMUM_DURATION = 0.01  # Set the minimum duration to 10 milliseconds

video = cv2.VideoCapture(0)

handGesture = handGesture = mp.solutions.hands.Hands(
    static_image_mode=False,  # Continuous tracking, better for video.
    max_num_hands=1,  # Track only one hand for faster performance.
    min_detection_confidence=0.5,  # Adjust detection confidence.
    min_tracking_confidence=0.5,  # Adjust tracking confidence.
    model_complexity=0  # Adjust model complexity.
)

drawingTools = mp.solutions.drawing_utils
screenWidth, screenHeight = pyautogui.size()

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="fQDjqbkxviXzBXoSjACM"
)

def pause_game():
    pyautogui.press('esc')

globalClickState = False

def close_fist():
    global globalClickState
    if globalClickState: return
    pyautogui.mouseDown()
    globalClickState = True

def open_hand():
    global globalClickState
    if not globalClickState: return
    pyautogui.mouseUp()
    globalClickState = False

while True:
    _, frame = video.read()
    frame = cv2.flip(frame, 1)
    frameHeight, frameWidth, _ = frame.shape
    rgbConvertedFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = handGesture.process(rgbConvertedFrame)
    hands = output.multi_hand_landmarks

    if hands:
        hand = hands[0]
        drawingTools.draw_landmarks(frame, hand)
        landmarks = hand.landmark
        lmList = []
        for id, landmark in enumerate(landmarks):
            cx, cy = int(landmark.x * frameWidth), int(landmark.y * frameHeight)
            lmList.append([id, cx, cy])
            if id == 5:
                x = int(landmark.x*frameWidth)
                y = int(landmark.y*frameHeight)
                cv2.circle(img=frame, center=(x,y), radius=30, color=(0, 255, 255))
                mousePositionX = screenWidth/frameWidth*x
                mousePositionY = screenHeight/frameHeight*y
                pyautogui.moveTo(mousePositionX, mousePositionY)
        indexX = 0
        indexY = 0
        indexMid = 0
        handBottomX = 0
        handBottomY = 0
        pinkyX = 0
        pinkyY = 0
        for lms in lmList:
            if lms[0] == 7:
                indexX, indexY = lms[1], lms[2]
            elif lms[0] == 5:
                indexMid = lms[2]
            elif lms[0] == 19:
                pinkyX, pinkyY = lms[1], lms[2]
            elif lms[0] == 0:
                handBottomX, handBottomY = lms[1], lms[2]
        if (indexY < handBottomY) and (indexY > indexMid):
            cv2.rectangle(rgbConvertedFrame, (indexX, indexY), (pinkyX, handBottomY), (0, 0, 255), 2)
            close_fist()
        else:
            open_hand()

    # cv2.imshow('Virtual Mouse', frame)
    # cv2.waitKey(1)