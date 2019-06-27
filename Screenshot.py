import numpy as np
import pyautogui
import imutils
import cv2

img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
cv2.imwrite('img.png', img)
