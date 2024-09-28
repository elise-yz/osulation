# Import the InferencePipeline object
from inference import InferencePipeline
import cv2
from dotenv import load_dotenv
import os
import pyautogui
from cv2_enumerate_cameras import enumerate_cameras

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

screen_width, screen_height = pyautogui.size()

api_key = os.getenv("ROBOFLOW_API_KEY")

def scale(x, y, screen_width, screen_height, img_width, img_height):
    x = int(x * screen_width / img_width)
    y = int(y * screen_height / img_height)
    # reflect x
    x = screen_width - x
    return x, y

def my_sink(result, video_frame):
    # move mouse to center of the hand
    # print(result["model_1"])
    try:
        x = int(result["model_1"][0]["predictions"][0]["x"])
        y = int(result["model_1"][0]["predictions"][0]["y"])
        image_width = result["model_1"][0]["image"]["width"]
        image_height = result["model_1"][0]["image"]["height"]
        newX, newY = scale(x, y, screen_width, screen_height, image_width, image_height)
        move_to(newX, newY)
    except:
        pass

    # click if fist, unclick if palm
    try:
        if result["model_1"][0]["predictions"][0]["class"] == "Rock":
            close_fist()
            # print("Fist")
        else:
            open_hand()
            # print("Palm")
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