import pyautogui

def move_to(x, y, click = False):
    pyautogui.moveTo(x, y)
    # if click:
    #     pyautogui.click() 

def pause_game():
    pyautogui.press('esc')

def close_fist(): 
    pyautogui.mouseDown()

def open_hand():
    pyautogui.mouseUp()


move_to(20, 30)
close_fist()