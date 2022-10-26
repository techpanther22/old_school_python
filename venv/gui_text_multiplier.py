import pyautogui
import time
import random

random.seed(10)
time.sleep(4)

count = 0
while count<=50:
    pyautogui.typewrite("hello " + str(count))
    pyautogui.press("enter")
    count = count + 1
    time.sleep(random.random() * 10)
