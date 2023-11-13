import cv2
import numpy as np
import pyautogui

while True:
    image = pyautogui.screenshot(region=(200,350,255,250)) #Taking screenshot
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

    cv2.imshow('image',image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break