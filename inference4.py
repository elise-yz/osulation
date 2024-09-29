# pynput test
from inference_sdk import InferenceHTTPClient
import cv2
from cv2_enumerate_cameras import enumerate_cameras
import mediapipe as mp
from dotenv import load_dotenv
from pynput import mouse, keyboard
import pyautogui
import os

load_dotenv()
api_key = os.getenv("ROBOFLOW_API_KEY")

CAMERA_NAME = "Logitech Webcam C925e" # Name of the webcame
CAMERA_INDEX = 0

for camera_info in enumerate_cameras():
    if camera_info.name == CAMERA_NAME:
        CAMERA_INDEX = camera_info.index

video = cv2.VideoCapture(CAMERA_INDEX) # Open video based on camera index

handGesture = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
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

def pause_game():
    keyboard_controller.press('esc')

def close_fist():
    global globalClickState
    if globalClickState: return
    mouse_controller.press(mouse.Button.left)
    globalClickState = True

def open_hand():
    global globalClickState
    if not globalClickState: return
    mouse_controller.release(mouse.Button.left)
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
                x = cx
                y = cy
                cv2.circle(img=frame, center=(x,y), radius=30, color=(0, 255, 255))
                mousePositionX = screenWidth/frameWidth*x
                mousePositionY = screenHeight/frameHeight*y
                mouse_controller.position = (mousePositionX, mousePositionY)
        
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
        
        if (indexY < handBottomY) and (indexY > indexMid):
            cv2.rectangle(rgbConvertedFrame, (indexX, indexY), (pinkyX, handBottomY), (0, 0, 255), 2)
            close_fist()
        else:
            open_hand()

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()