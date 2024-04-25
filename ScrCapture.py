import cv2
import numpy as np
import pyperclip
import pyautogui
import uuid
import os


start_point=(0,0)
end_point=(0,0)
isContinue = True
SRC_WIDTH, SRC_HEIGHT = pyautogui.size()
IMAGE_PATH = f"{os.getcwd()}/ScreenShots/"
MAIN_TITLE="SrcCapture - Enter: Save | Y: Copy | C: Save Crop | Q: Quit"
INPUT_TITLE="Enter File Name or Skip For Random"
if not os.path.exists(IMAGE_PATH):
    os.makedirs(IMAGE_PATH)
def draw_rectangle(event, x, y, flags, param:list[cv2.Mat]):
    global drawing, start_point,end_point

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        tmpImg = param[0].copy()
        drawing = False
        end_point = (x, y)
        cv2.rectangle(tmpImg, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow(MAIN_TITLE, tmpImg)

def save_image(frame):
    filename = ""
    while filename == "" or os.path.exists(filename):
        cv2.destroyWindow(MAIN_TITLE)
        name = input("Enter File Name or Skip For Random:\n").replace(" ", "_") or str(uuid.uuid4())
        filename = IMAGE_PATH + name + ".png"
    try:
        cv2.imwrite(filename, frame)
        print(f"Saved Image: {filename}")
    except Exception as e:
        print('Error: Cannot Save Image')

def copy_image(frame:cv2.Mat):
    pyperclip.copy(str(frame.copy().tolist()))
def stop():
    global isContinue
    isContinue = False
def reset_selection():
    global start_point, end_point
    start_point = (0, 0)
    end_point = (0, 0)
while True:
    try:
        # Đọc hình ảnh
        input("Press Enter To Capture...")
        reset_selection()
        frame = pyautogui.screenshot(region=(0,0,SRC_WIDTH,SRC_HEIGHT))
        frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        cv2.namedWindow(MAIN_TITLE)
        while True:
            cv2.imshow(MAIN_TITLE, frame)
            cv2.moveWindow(MAIN_TITLE, 0, 0)
            cv2.setMouseCallback(MAIN_TITLE, draw_rectangle,param=[frame])
            key = cv2.waitKey(0) & 0xFF
            match key:
                case 113:
                    break
                case 99:
                    save_image(frame[start_point[1]:end_point[1],start_point[0]:end_point[0]])
                    break
                case 121:
                    copy_image(frame)
                    break
                case 13:
                    save_image(frame)
                    break
                case _:
                    continue
        cv2.destroyAllWindows()
    except Exception or KeyboardInterrupt:
        break
# Đóng cửa sổ và giải phóng bộ nhớ
cv2.destroyAllWindows()