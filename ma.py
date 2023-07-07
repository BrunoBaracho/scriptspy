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
        time.sleep(46)
        pyautogui.keyUp(current_key)
        if current_key == 'a':
            current_key = 'd'
        else:
            current_key = 'a'