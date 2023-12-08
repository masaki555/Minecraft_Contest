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
import math
import getPosition
import init

def main():

    time.sleep(1)

   # 目標座標(x,z,y)
    x = -3
    z = 4
    y = -1

    x1, z1, y1 = getPosition.getPosition()
    print(x1, z1, y1)

    now = math.sqrt((x - x1)**2 + (y - y1)**2) # 目的座標と現在の座標の距離を計算
    min = now
    
    while True:
        monitorPlayerMove.forward(1)
        past = now
        x2, z2, y2 = getPosition.getPosition()
        print(x2, z2, y2) # 現在の座標を表示        
        now = math.sqrt((x - x2)**2 + (y - y2)**2) # 目的座標と現在の座標の距離を計算
        if(past != now): # 前回の座標と現在の座標が異なる場合
            monitorPlayerMove.forward(0)
            # 目的地に近づいている場合
            if(now<past):
                flag=0
            if(now>past): # 目的地から遠ざかっている場合
                flag=1
            if(flag==0):
                monitorPlayerMove.forward(1)
                if(min>now):
                    min=now # minに最小値を入れる
                while True:
                    past = now
                    x3, z3, y3 = getPosition.getPosition()
                    print(x3, z3, y3) # 現在の座標を表示
                    now = math.sqrt((x - x3)**2 + (y - y3)**2)
                    if(min>now): # minに最小値を入れる
                        min=now
                    if(min<now):
                        monitorPlayerMove.forward(0)
                        break
                break
            if(flag==1):
                monitorPlayerMove.back(1)
                while True:
                    past = now
                    x3, z3, y3 =  getPosition.getPosition()
                    print(x3, z3, y3)
                    now = math.sqrt((x - x3)**2 + (y - y3)**2)
                    if(min>now):
                        min=now
                    if(min<now):
                        monitorPlayerMove.back(0)
                        break
                break

    # # スクショと文字認識
    # image = ImageGrab.grab(cordinate) # スクショを撮る
    # image.save('image.png') # スクショを保存
    # tesseract_args = '-c tessedit_char_whitelist="0123456789-,. "' # 認識する文字の指定
    # text = pytesseract.image_to_string(image, config=tesseract_args) # 文字認識
    # text = text.replace(' ', '').rstrip() # 認識した文字から空白を削除
    # x1, z1, y1 = map(int, re.split('[,.]', text)) # 認識した文字を座標に変換
    # print(x1, z1, y1)
    x1, z1, y1 = getPosition.getPosition()
    while True:
        monitorPlayerMove.right(1)
        past = now
        x2, z2, y2 = getPosition.getPosition()
        print(x2, z2, y2)
        now = math.sqrt((x - x2)**2 + (y - y2)**2)
        if(past != now):
            monitorPlayerMove.right(0)
            if(now<past):
                flag=0
            if(now>past):
                flag=1
            if(flag==0):
                monitorPlayerMove.right(1)
                if(min>now):
                    min=now
                while True:
                    past = now
                    x3, z3, y3 = getPosition.getPosition()
                    print(x3, z3, y3)
                    now = math.sqrt((x - x3)**2 + (y - y3)**2)
                    if(min>now):
                        min=now
                    if(min<now):
                        monitorPlayerMove.right(0)
                        break
                break
            if(flag==1):
                monitorPlayerMove.left(1)
                while True:
                    past = now
                    x3, z3, y3 = getPosition.getPosition()
                    print(x3, z3, y3)
                    now = math.sqrt((x - x3)**2 + (y - y3)**2)
                    if(min>now):
                        min=now
                    if(min<now):
                        monitorPlayerMove.left(0)
                        break
                break

if __name__ == "__main__":
    init.init()
    main()