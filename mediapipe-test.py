import cv2
import mediapipe as mp
import pyautogui


video = cv2.VideoCapture(0)


handGesture = mp.solutions.hands.Hands()
drawingTools = mp.solutions.drawing_utils
screenWidth, screenHeight = pyautogui.size()


while True:
   _, frame = video.read()
   frame = cv2.flip(frame, 1)
   frameHeight, frameWidth, _ = frame.shape
   rgbConvertedFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   output = handGesture.process(rgbConvertedFrame)
   hands = output.multi_hand_landmarks


   if hands:
       for hand in hands:
           drawingTools.draw_landmarks(frame, hand)
           landmarks = hand.landmark
           for id, landmark in enumerate(landmarks):
               if id == 5:
                   x = int(landmark.x*frameWidth)
                   y = int(landmark.y*frameHeight)
                   cv2.circle(img=frame, center=(x,y), radius=30, color=(0, 255, 255))
                   mousePositionX = screenWidth/frameWidth*x
                   mousePositionY = screenHeight/frameHeight*y
                   pyautogui.moveTo(mousePositionX, mousePositionY)




   cv2.imshow('Virtual Mouse', frame)
   cv2.waitKey(1)