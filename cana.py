import pyautogui
import keyboard
import time

is_running = False
current_key = 's'

def toggle():
    global is_running
    is_running = not is_running

keyboard.add_hotkey('y', toggle)
while True:
    if is_running:
        pyautogui.mouseDown(button='left')
        pyautogui.keyDown(current_key)
        time.sleep(13)
        pyautogui.keyUp(current_key)
        if current_key == 'a':
            pyautogui.keyDown('d')
            time.sleep(1)
            pyautogui.keyUp('d')
            current_key = 's'
        else:
            current_key = 'a'