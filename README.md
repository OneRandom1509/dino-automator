# dino-automator
A simple python script using `pyautogui` and `keyboard` modules to automate chrome's dino game. This was written for as part of IEEE ComSoc's recruitment process.

## Getting Started
1. Clone this repository using the git clone command 
```
git clone https://github.com/OneRandom1509/dino-automator
```

2. Navigate to the cloned repository's directory in your terminal and run this python command to install all the dependencies
```
pip install -r requirements.txt
``` 

3. Run the `script.py` file and go to your `chrome://dino` page to see the magic!! If you want to quit the script, simply press the `q` key in your keyboard

P.S You have a buffer time of 3 seconds by default to switch to your browser window :)

## Known Issues
1. Since the "obstacles' region" might be different for different screen/window sizes, you might have to tinker around a bit to find the optimum region

2. This script isn't perfect. Because of the static adaptability code, it might fail to clear some obstacles in close succession. The max score this script has reached is `2763`