import pyautogui
import keyboard
import time

is_running = False
current_key = 'a'

def toggle():
    global is_running
    is_running = not is_running

keyboard.add_hotkey('y', toggle)
while True:
    if is_running:
        pyautogui.mouseDown(button='left')
        pyautogui.keyDown(current_key)
        time.sleep(77)
        pyautogui.keyUp(current_key)
        if current_key == 'a':
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
            current_key = 'd'
        else:
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
            current_key = 'a'