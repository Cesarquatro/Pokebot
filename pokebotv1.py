import pyautogui
import time
import numpy as np
import cv2

j=0
f=100
time.sleep(2)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt') 
time.sleep(5)

coordinates=np.zeros((10,2), dtype= np.float64)#coordinates:
#click-Menu:
coordinates[0,0], coordinates[0,1] = (806, 680)
#click-Appraise:
coordinates[3,0], coordinates[3,1] = (814, 301)
#click-Pokegenie:
coordinates[1,0], coordinates[1,1] = (801, 559)
#click-Anywhere:
coordinates[2,0], coordinates[2,1] = (801, 559)
#click-Pokemon:
coordinates[4,0], coordinates[4,1] = (674, 261)
#click-Change Name:
coordinates[5,0], coordinates[5,1] = (702, 320)
#click-Clipboard:
coordinates[6,0], coordinates[6,1] = (670, 522)
#click-Last coppied string:
coordinates[7,0], coordinates[7,1] = (600, 583)
#click-Green 'ok':
coordinates[8,0], coordinates[8,1] = (682, 418)
#click-Green 'ok':
coordinates[9,0], coordinates[9,1] = (682, 418)

mouseDown=np.zeros((1,2), dtype= np.float64)
mouseDown[0,0], mouseDown[0,1] = (793,370)

mouseUp=np.zeros((1,2), dtype= np.float64)
mouseUp[0,0], mouseUp[0,1] = (580,354)

while(j<f):
	for i in range(0,10):
		if ((i==4)or(i==5)):
			pyautogui.moveTo(coordinates[i,0],coordinates[i,1],1.2)
		else:
			pyautogui.moveTo(coordinates[i,0],coordinates[i,1],0.5)
		#time.sleep(2)
		pyautogui.click()
	time.sleep(0.2)
	pyautogui.moveTo(mouseDown[0,0],mouseDown[0,1],0.5)
	pyautogui.mouseDown()
	pyautogui.moveTo(mouseUp[0,0],mouseUp[0,1],0.6)
	pyautogui.mouseUp()
	j=j+1
		
time.sleep(2)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt') 