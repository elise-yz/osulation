import cv2
from cv2_enumerate_cameras import enumerate_cameras

CAMERA_NAME = "Logitech Webcam C925e" # Name of the webcame
CAMERA_INDEX = 0

for camera_info in enumerate_cameras():
    if camera_info.name == CAMERA_NAME:
        CAMERA_INDEX = camera_info.index

stream = cv2.VideoCapture(CAMERA_INDEX) # Open video based on camera index

if not stream.isOpened(): # If stream is not working
    print("No stream :(")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS) 
width = int(stream.get(3)) # Set video dimensions
height = int(stream.get(4))

while True:
    ret, frame = stream.read()
    if not ret: # If no frames are returned
        print("No camera info")
        break
    
    frame = cv2.resize(frame, (width, height))
    cv2.imshow("Osulation!", frame)
    if cv2.waitKey(1) == ord('q'): # Press q to quit
        break

stream.release()
cv2.destroyAllWindows() 