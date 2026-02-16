import pyautogui

def click_next(x, y):
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.click()
