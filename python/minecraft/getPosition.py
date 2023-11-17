import win32gui
from PIL import ImageGrab, Image
import pytesseract
from tesseract_pack import data_here
import time
import pydirectinput
import re
import monitorPlayerMove

##################################
game_name = 'Minecraft Education'
sleep_time = 0.05
##################################

def main():
    mcapp = win32gui.FindWindow(None,game_name)
    time.sleep(sleep_time)
    win32gui.SetForegroundWindow(mcapp)         #ウィンドウの指定
    time.sleep(sleep_time)
    pydirectinput.keyDown('esc')
    pydirectinput.keyUp('esc')
    time.sleep(sleep_time)

    hwnd = win32gui.GetForegroundWindow()
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bottom)
    cordinate = (left+45, top+131, right-800, bottom-845)

    TESSERACT_EXECUTABLE = data_here + "\\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd =  TESSERACT_EXECUTABLE

    time.sleep(1)

    # スクショと文字認識
    image = ImageGrab.grab(cordinate)
    image.save('image.png')
    text = pytesseract.image_to_string(image)

    print(text)

    # ','または'.'を除いて分割する
    delimiter_pattern = re.compile('[,\\.]')
    x1, z1, y1 = map(int, re.split(delimiter_pattern, text))

    print(x1, z1, y1)

    # 目標座標
    x = 0
    y = 0

    # 
    while True:
        monitorPlayerMove.forward(1)
        image = ImageGrab.grab(cordinate)
        image.save('image.png')
        text = pytesseract.image_to_string(image)
        delimiter_pattern = re.compile('[,\\.]')
        x2, z2, y2 = map(int, re.split(delimiter_pattern, text))
        if(x1 != x2 or y1 != y2):
            print(x2, z2, y2)
            monitorPlayerMove.forward(0)
            break
    
    # もしx-x1<x-x2(目的座標から遠ざかれば)ならば
    if x-x1 < x-x2:
        while True:
            monitorPlayerMove.back(1)
            image = ImageGrab.grab(cordinate)
            image.save('image.png')
            text = pytesseract.image_to_string(image)
            print(text)
            delimiter_pattern = re.compile('[,\\.]')
            x2, z2, y2 = map(int, re.split(delimiter_pattern, text))
            if -5 < x-x2 < 5:
                monitorPlayerMove.back(0)
                break
    if x-x1 > x-x2:
        while True:
            monitorPlayerMove.forward(1)
            image = ImageGrab.grab(cordinate)
            image.save('image.png')
            text = pytesseract.image_to_string(image)
            print(text)
            delimiter_pattern = re.compile('[,\\.]')
            x2, z2, y2 = map(int, re.split(delimiter_pattern, text))
            if -5 < x-x2 < 5:
                monitorPlayerMove.forward(0)
                break



    print(x,y)


if __name__ == "__main__":
    main()
