import pyautogui 
import keyboard 
import time 
import math 

# to get the colour of the pixel
def get_pixel(image, x, y): 

	px = image.load() 
	return px[x, y] 


def main(): 

    # resolution of the screenshot to be taken
	x, y, width, height = 0, 102, 1920, 872

	jumping_time = 0
	last_jumping_time = 0
	current_jumping_time = 0
	last_interval_time = 0

	# obstacle region
	y1, y2, x1, x2 = 590, 550, 540, 590

    # 3 second buffer time to go to the browser
	time.sleep(3) 
	print("Started!")

    # start of the script
	while True: 
		t1 = time.time() 

	    # press q to exit
		if keyboard.is_pressed('q'): 
			print("Stopped!")
			break

        # screenshotting the 
		img = pyautogui.screenshot(region=(x, y, width, height)) 
		bg_color = get_pixel(img, 100, 100) 

        # checking for obsacles by comparing bg_color to color of each pixel in the search region
		for i in reversed(range(x1, x2)): 
			if get_pixel(img, i, y1) != bg_color or get_pixel(img, i, y2) != bg_color: 
				keyboard.press('up') 
				jumping_time = time.time()-t1
				current_jumping_time = jumping_time
				break

		interval_time = current_jumping_time - last_jumping_time 

		# game is accelerating if the intervals are not same 
		if last_interval_time != 0 and math.floor(interval_time) != math.floor(last_interval_time): 
            # increasing the width of searching region to adapt
			x2 += 3 
			if x2 >= width: 
				x2 = width 

		# updating variables
		last_jumping_time = jumping_time 
		last_interval_time = interval_time 

if __name__ == "__main__":
    main()