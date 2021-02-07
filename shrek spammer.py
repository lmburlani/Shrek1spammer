import pyautogui
from time import sleep
time.sleep(5)
f = open("shrek", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")