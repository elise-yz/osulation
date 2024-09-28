# Import the InferencePipeline object
from inference import InferencePipeline
import cv2
from dotenv import load_dotenv
import os
import pyautogui

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
    # move mouse to center of the hand
    try:
        pred_x = result["model_predictions"][0].xyxy[0][0]
        pred_y = result["model_predictions"][0].xyxy[0][1]
        
        newX, newY = scale(pred_x, pred_y, screen_width, screen_height, image_width, image_height)
        # print(result["model_predictions"][0].xyxy[0][0:2])
        move_to(newX, newY)
    except:
        pass

    # click if fist, unclick if palm
    try:
        class_id = result["model_predictions"][0].class_id  # Class IDs array
        class_names = result["model_predictions"][0].data['class_name']  # Class names array
        pred_class = class_names[class_id]  # Get the first class name

        if pred_class == "fist":
            # close_fist()
            print("Fist")
        else:
            # open_hand()
            print("Palm")
    except:
        pass
    

# initialize a pipeline object
pipeline = InferencePipeline.init_with_workflow(
    api_key=api_key,
    workspace_name="osulation",
    workflow_id="custom-workflow-3",
    video_reference=0, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
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