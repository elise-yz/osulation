# Import the InferencePipeline object
from inference import InferencePipeline
import cv2
from dotenv import load_dotenv
import os
import pyautogui
from cv2_enumerate_cameras import enumerate_cameras
import mediapipe as mp

def move_to(x, y):
    pyautogui.moveTo(x, y)
    # if click:
    #     pyautogui.click() 

def pause_game():
    pyautogui.press('esc')

def close_fist(): 
    pyautogui.mouseDown()

def open_hand():
    pyautogui.mouseUp()

load_dotenv()

handGesture = mp.solutions.hands.Hands()
drawingTools = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
cap = cv2.VideoCapture(0)
image_width, image_height = 640, 480
if not cap.isOpened():
    print("Error: Unable to open video source")
else:
    # Get the width and height of the video frame
    image_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    image_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

api_key = os.getenv("ROBOFLOW_API_KEY")

def scale(x, y, screen_width, screen_height, img_width, img_height):
    x = int(x * screen_width / img_width)
    y = int(y * screen_height / img_height)
    # reflect x
    x = screen_width - x
    print(x, y)
    return x, y

def my_sink(result, video_frame):
    frame = result["output"].numpy_image
    frame = cv2.flip(frame, 1)
    frameHeight, frameWidth, _ = frame.shape
    rgbConvertedFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = handGesture.process(rgbConvertedFrame)
    hands = output.multi_hand_landmarks

    if hands:
        drawingTools.draw_landmarks(frame, hands[0])
        landmarks = hands[0].landmark
        for id, landmark in enumerate(landmarks):
            if id == 5:
                x = int(landmark.x*frameWidth)
                y = int(landmark.y*frameHeight)
                cv2.circle(img=frame, center=(x,y), radius=30, color=(0, 255, 255))
                mousePositionX = screen_width/frameWidth*x
                mousePositionY = screen_height/frameHeight*y
                pyautogui.moveTo(mousePositionX, mousePositionY)

    # click if fist, unclick if palm
    try:
        class_name = result["model_1"][0]["predictions"][0]['class']  # Class names array

        if class_name == "Rock":
            close_fist()
        else:
            open_hand()
    except:
        pass
    
CAMERA_NAME = "Logitech Webcam C925e" # Name of the webcame
CAMERA_INDEX = 0

for camera_info in enumerate_cameras():
    if camera_info.name == CAMERA_NAME:
        CAMERA_INDEX = camera_info.index

# initialize a pipeline object
pipeline = InferencePipeline.init_with_workflow(
    api_key=api_key,
    workspace_name="osulation",
    workflow_id="custom-workflow-2",
    video_reference=CAMERA_INDEX, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    max_fps=10,
    on_prediction=my_sink
)
pipeline.start() #start the pipeline
# pipeline.join() #wait for the pipeline thread to finish

# stop pipeline after 30 seconds
import time
time.sleep(30)
print("Terminating pipeline")

pipeline.terminate() #stop the pipeline