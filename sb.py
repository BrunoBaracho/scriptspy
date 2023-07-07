import pyautogui
import keyboard
import time

is_running = False
current_key = 'd'
counter = 0

def toggle():
    global is_running
    is_running = not is_running

keyboard.add_hotkey('y', toggle)
while True:
    if is_running:
        pyautogui.mouseDown(button='left')
        pyautogui.keyDown(current_key)
        time.sleep(98)
        pyautogui.keyUp(current_key)
        if current_key == 'a':
            current_key = 'd'
            counter += 1
        elif counter == 2:
            pyautogui.keyDown('k')
            pyautogui.keyUp('k')
            counter = 0
        else:
            current_key = 'a'