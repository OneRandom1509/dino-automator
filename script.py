import pyautogui as gui 
import keyboard 
from PIL import Image, ImageGrab 
import time 
import math 


def get_pixel(image, x, y): 

	px = image.load() 
	return px[x, y] 


def start(): 

	# set size of the image to be taken 
	x, y, width, height = 0, 102, 1920, 872

	# calculating time 
	jumping_time = 0
	last_jumping_time = 0
	current_jumping_time = 0
	last_interval_time = 0

	y1, y2, x1, x2 = 590, 550, 540, 600

	time.sleep(3) 
	print("Started!")
	while True: 
		t1 = time.time() 
	# press q to exit the robot 
		if keyboard.is_pressed('q'): 
			print("Stopped!")
			break

		sct_img = gui.screenshot(region=(x, y, width, height)) 
		sct_img.save("dino.jpg") 

		bg_color = get_pixel(sct_img, 100, 100) 

		for i in reversed(range(x1, x2)): 
			if get_pixel(sct_img, i, y1) != bg_color or get_pixel(sct_img, i, y2) != bg_color: 
				keyboard.press('up') 
				jumping_time = time.time()-t1
				current_jumping_time = jumping_time 
				break

		interval_time = current_jumping_time - last_jumping_time 

		# game is accelerating if the intervals not same 
		if last_interval_time != 0 and math.floor(interval_time) != math.floor(last_interval_time): 
			x2 += 3
			if x2 >= width: 
				x2 = width 

		# get the last jump 
		last_jumping_time = jumping_time 
		# get the time between the last jump and the previous one 
		last_interval_time = interval_time 


start() 
