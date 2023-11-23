import win32gui
from PIL import ImageGrab, Image
import pytesseract
from tesseract_pack import data_here
import time
import pydirectinput
import re
import monitorPlayerMove
import win32com.client
import numpy as np 
from matplotlib import pylab as plt
import monitorPlayerCamera
import getPosition

##################################
game_name = 'Minecraft Education'
sleep_time = 0.05
##################################

def main():
    print("position:")
    print(getPosition.getPosition())
    mcapp = win32gui.FindWindow(None,game_name)
    time.sleep(sleep_time)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(mcapp) #ウィンドウの指定
    time.sleep(sleep_time)
    pydirectinput.keyDown('esc')
    pydirectinput.keyUp('esc')
    time.sleep(sleep_time)

    hwnd = win32gui.GetForegroundWindow()
    left, top, right, bottom = win32gui.GetWindowRect(hwnd) # ウィンドウの座標を取得
    cordinate = (left+95, top+131, right-725, bottom-845) # ウィンドウの座標からスクショを撮る範囲を指定

    TESSERACT_EXECUTABLE = data_here + "\\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd =  TESSERACT_EXECUTABLE

    time.sleep(1)

    # 目標座標(x,z,y)
    x = 0
    z = 0
    y = 0

    # スクショと文字認識
    image = ImageGrab.grab(cordinate) # スクショを撮る
    image.save('image.png') # スクショを保存

    # image41 = np.array(image.convert('L'), 'f')
    # image42 = (image41 > 110) * 255
    # image43 = Image.fromarray(image42)

    tesseract_args = '-c tessedit_char_whitelist="0123456789-,. "' # 認識する文字の指定
    text = pytesseract.image_to_string(image, config=tesseract_args) # 文字認識
    print(text) # 認識した文字を表示
    text = text.replace(' ', '').rstrip() # 認識した文字から空白を削除
    print(text) # 認識した文字を表示
    x1, z1, y1 = map(int, re.split('[,.]', text)) # 認識した文字を座標に変換
    print(x1, z1, y1)
    
    while True:
        monitorPlayerMove.forward(1) # 前に進む
        image = ImageGrab.grab(cordinate) # スクショを撮る
        image.save('image.png') # スクショを保存
        text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip() # スクショから文字を認識
        x2, z2, y2 = map(int, re.split('[,.]', text)) # 認識した文字を座標に変換
        print(x2, z2, y2) # 現在の座標を表示
        if(x1 != x2): # x座標が変化した場合
            monitorPlayerMove.forward(0) # 前に進むのをやめる
            if(x-x1 < x-x2): # 目標座標に近づいている場合
                flag = 0
            if(x-x1 > x-x2): # 目標座標から遠ざかっている場合
                flag = 1
            if(flag == 0):
                while True:
                    monitorPlayerMove.forward(1) # 前に進む
                    image = ImageGrab.grab(cordinate)
                    image.save('image.png')
                    text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip()
                    x3, z3, y3 = map(int, re.split('[,.]', text))
                    print(x3, z3, y3)
                    if(x == x3): # 目標座標に到達した場合
                        monitorPlayerMove.forward(0) # 前に進むのをやめる
                        break
            if(flag == 1):
                while True:
                    monitorPlayerMove.back(1) # 後ろに進む
                    image = ImageGrab.grab(cordinate)
                    image.save('image.png')
                    text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip()
                    x3, z3, y3 = map(int, re.split('[,.]', text))
                    print(x3, z3, y3)
                    if(x == x3): # 目標座標に到達した場合
                        monitorPlayerMove.back(0) # 後ろに進むのをやめる
                        break
        if(y1 != y2): # y座標が変化した場合
            monitorPlayerMove.forward(0) # 前に進むのをやめる
            if(y-y1 < y-y2): # 目標座標yに近づいている場合
                flag = 0
            if(y-y1 > y-y2): # 目標座標yから遠ざかっている場合
                flag = 1
            if(flag == 0):
                while True:
                    monitorPlayerMove.forward(1) # 前に進む
                    image = ImageGrab.grab(cordinate)
                    image.save('image.png')
                    text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip()
                    x3, z3, y3 = map(int, re.split('[,.]', text))
                    print(x3, z3, y3)
                    if(y == y3): # 目標座標yに到達した場合
                        monitorPlayerMove.forward(0) # 前に進むのをやめる
                        break
            if(flag == 1):
                while True:
                    monitorPlayerMove.back(1) # 後ろに進む
                    image = ImageGrab.grab(cordinate)
                    image.save('image.png')
                    text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip()
                    x3, z3, y3 = map(int, re.split('[,.]', text))
                    print(x3, z3, y3)
                    if(y == y3): # 目標座標yに到達した場合
                        monitorPlayerMove.back(0) # 後ろに進むのをやめる
                        break
        break

    # スクショと文字認識
    image = ImageGrab.grab(cordinate) # スクショを撮る
    image.save('image.png') # スクショを保存
    tesseract_args = '-c tessedit_char_whitelist="0123456789-,. "' # 認識する文字の指定
    text = pytesseract.image_to_string(image, config=tesseract_args) # 文字認識
    print(text) # 認識した文字を表示
    text = text.replace(' ', '').rstrip() # 認識した文字から空白を削除
    print(text) # 認識した文字を表示
    x1, z1, y1 = map(int, re.split('[,.]', text)) # 認識した文字を座標に変換
    print(x1, z1, y1)
    while True:
        monitorPlayerMove.right(1) # 右に進む
        image = ImageGrab.grab(cordinate) # スクショを撮る
        image.save('image.png') # スクショを保存
        text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip() # スクショから文字を認識
        x2, z2, y2 = map(int, re.split('[,.]', text)) # 認識した文字を座標に変換
        print(x2, z2, y2) # 現在の座標を表示
        if(x1 != x2): # x座標が変化した場合
            monitorPlayerMove.right(0) # 右に進むのをやめる
            if(x-x1 < x-x2): # 目標座標に近づいている場合
                flag = 0
            if(x-x1 > x-x2): # 目標座標から遠ざかっている場合
                flag = 1
            if(flag == 0):
                while True:
                    monitorPlayerMove.right(1) # 右に進む
                    image = ImageGrab.grab(cordinate)
                    image.save('image.png')
                    text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip()
                    x3, z3, y3 = map(int, re.split('[,.]', text))
                    print(x3, z3, y3)
                    if(x == x3): # 目標座標に到達した場合
                        monitorPlayerMove.right(0) # 右に進むのをやめる
                        break
            if(flag == 1):
                while True:
                    monitorPlayerMove.left(1) # 左に進む
                    image = ImageGrab.grab(cordinate)
                    image.save('image.png')
                    text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip()
                    x3, z3, y3 = map(int, re.split('[,.]', text))
                    print(x3, z3, y3)
                    if(x == x3): # 目標座標に到達した場合
                        monitorPlayerMove.left(0) # 左に進むのをやめる
                        break
        if(y1 != y2): # y座標が変化した場合
            monitorPlayerMove.right(0) # 右に進むのをやめる
            if(y-y1 < y-y2): # 目標座標yに近づいている場合
                flag = 0
            if(y-y1 > y-y2): # 目標座標yから遠ざかっている場合
                flag = 1
            if(flag == 0):
                while True:
                    monitorPlayerMove.right(1) # 右に進む
                    image = ImageGrab.grab(cordinate)
                    image.save('image.png')
                    text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip()
                    x3, z3, y3 = map(int, re.split('[,.]', text))
                    print(x3, z3, y3)
                    if(y == y3): # 目標座標yに到達した場合
                        monitorPlayerMove.right(0) # 右に進むのをやめる
                        break
            if(flag == 1):
                while True:
                    monitorPlayerMove.left(1) # 左に進む
                    image = ImageGrab.grab(cordinate)
                    image.save('image.png')
                    text = pytesseract.image_to_string(image, config=tesseract_args).replace(' ', '').rstrip()
                    x3, z3, y3 = map(int, re.split('[,.]', text))
                    print(x3, z3, y3)
                    if(y == y3): # 目標座標yに到達した場合
                        monitorPlayerMove.left(0) # 左に進むのをやめる
                        break
        break

if __name__ == "__main__":
    main()

# 【問題点】本間にこれ動くんか？
# 【問題点】壁にぶつかったとき座標の変化が無くなる事の対処を考える->壁にぶつかったら右に90度回転して前に進む?
# 【問題点】座標の読み取り時に，枠の長さが変化することで読み取りがうまくいかないことがある->会場の場所を2桁の座標の位置にしてもらう．
