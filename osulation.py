import cv2
from cv2_enumerate_cameras import enumerate_cameras
import streamlit as st
import pyautogui

def start_camera():
    CAMERA_NAME = "Logitech Webcam C925e" # Name of the webcame
    CAMERA_INDEX = 0
    

    for camera_info in enumerate_cameras():
        if camera_info.name == CAMERA_NAME:
            CAMERA_INDEX = camera_info.index

    cv2.namedWindow("Osulation!", cv2.WND_PROP_FULLSCREEN) # Make video fullscreen
    cv2.setWindowProperty("Osulation!", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    stream = cv2.VideoCapture(CAMERA_INDEX) # Open video based on camera index

    if not stream.isOpened(): # If stream is not working
        print("No stream :(")
        exit()

    fps = stream.get(cv2.CAP_PROP_FPS) 

    while True:
        ret, frame = stream.read()
        if not ret: # If no frames are returned
            print("No camera info")
            break
        
        cv2.imshow("Osulation!", frame)
        if cv2.waitKey(1) == ord('q'): # Press q to quit
            break

    stream.release()
    cv2.destroyAllWindows()     

st.title('demo')

start_button = st.button('Start playing!')
if start_button:
    start_camera()