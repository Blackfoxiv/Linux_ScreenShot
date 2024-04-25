# Linux_ScreenShot Usage Manual

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)

## Introduction
Linux_ScreenShot is a Python script that allows you to capture and save screenshots from your Linux computer. <br>
It uses the OpenCV library for image processing and the pyautogui library for interacting with the computer's screen.<br>
### Note: This Only Work in Linux Now, I'm so Sorry

## Installation<br>
To use Linux_ScreenShot, you will need to have Python installed on your Linux computer. You can download Python from the official website:
<br>[https://www.python.org/downloads/](https://www.python.org/downloads/).

Once you have Python installed, you can install the required libraries by running the following command in your terminal:<br>
<code>pip install opencv-python numpy pyperclip pyautogui</code><br>

## Usage
To use Linux_ScreenShot, simply run the script using the following command:<br>
<code>python Linux_ScreenShot.py</code> <br>or <code>python3 Linux_ScreenShot.py</code><br>

When the script starts, it will prompt you to press Enter to capture the screen. <br>
After you press Enter, you can draw a rectangle on the screen to select the area you want to capture. <br>

-Press Enter to Save it to File <br>
-Press <b>Y</b> to Copy to Clipboard.(<b>Sorry but it not working now, Don't worry i will fix it</b> <br>
-Press <b>C</b> to save the selected ROI as an image.( use Mouse draw a select region first) <br>
-Press <b>Q</b> to quit the program.<br>

#Default Path is './Screenshots/'
Optionally, you can enter a file name to save the image. <br>
If you skip this step, a random file name will be generated. <br>
The program will save the image in the ScreenShots directory in the current working directory. 
The program will display the saved image and its file name in the console. <br>
The program will also copy the file path of the saved image to the clipboard. <br>
You can use the copied file path to open the saved image in your preferred image viewer.<br>

Enjoy capturing screenshots and saving them to your desired location!
##Thanks You Very Muchs
