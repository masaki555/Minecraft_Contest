import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)
import time
import monitorPlayerMove
import numpy as np 
from matplotlib import pylab as plt
import math
import getPosition

def main():

    time.sleep(1)

   # 目標座標(x,z,y)を入力
    x = int(sys.argv[1])
    z = 4
    y = int(sys.argv[2])

    x1, z1, y1 = getPosition.getPosition()
    print(x1, z1, y1) # 現在の座標を表示
    now = math.sqrt((x - x1)**2 + (y - y1)**2) # 目的座標と現在の座標の距離を計算
    min = now
    
    while True:
        monitorPlayerMove.forward(1)
        past = now
        time.sleep(0.5)
        x2, z2, y2 = getPosition.getPosition()
        print(x2, z2, y2) # 現在の座標を表示        
        now = math.sqrt((x - x2)**2 + (y - y2)**2) # 目的座標と現在の座標の距離を計算
        if(past != now): # 前回の座標と現在の座標が異なる場合
            monitorPlayerMove.forward(0)
            time.sleep(0.2)
            if(now<past): # 目的地に近づいている場合
                flag=0
            if(now>past): # 目的地から遠ざかっている場合
                flag=1
            if(flag==0):
                monitorPlayerMove.forward(1)
                if(min>now):
                    min=now 
                while True: 
                    past = now
                    time.sleep(0.2)
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
                time.sleep(0.2)
                x1, z1, y1 = getPosition.getPosition()
                now = math.sqrt((x - x1)**2 + (y - y1)**2) # 目的座標と現在の座標の距離を計算
                min = now
                monitorPlayerMove.back(1)
                if(min>now):
                    min=now
                while True:
                    past = now
                    time.sleep(0.2)
                    x3, z3, y3 =  getPosition.getPosition()
                    print(x3, z3, y3)
                    now = math.sqrt((x - x3)**2 + (y - y3)**2)
                    if(min>now):
                        min=now
                    if(min<now):
                        monitorPlayerMove.back(0)
                        break
                break
        if(past == now): # 前回の座標と現在の座標が同じ場合
            monitorPlayerMove.forward(0)
            monitorPlayerMove.back(1)
            time.sleep(1)
            monitorPlayerMove.back(0)
            x1, z1, y1 = getPosition.getPosition()
            print(x1, z1, y1) # 現在の座標を表示
            now = math.sqrt((x - x1)**2 + (y - y1)**2) # 目的座標と現在の座標の距離を計算
            min = now
            continue

    x1, z1, y1 = getPosition.getPosition()
    print(x1, z1, y1) # 現在の座標を表示
    now = math.sqrt((x - x1)**2 + (y - y1)**2) # 目的座標と現在の座標の距離を計算
    min = now

    while True:
        monitorPlayerMove.right(1)
        past = now
        time.sleep(0.2)
        x2, z2, y2 = getPosition.getPosition()
        print(x2, z2, y2) # 現在の座標を表示
        now = math.sqrt((x - x2)**2 + (y - y2)**2) # 目的座標と現在の座標の距離を計算
        if(past != now): # 前回の座標と現在の座標が異なる場合
            monitorPlayerMove.right(0)
            time.sleep(0.2)
            if(now<past): # 目的地に近づいている場合
                flag=0
            if(now>past): # 目的地から遠ざかっている場合
                flag=1
            if(flag==0):
                monitorPlayerMove.right(1)
                if(min>now):
                    min=now
                while True:
                    past = now
                    time.sleep(0.2)
                    x3, z3, y3 = getPosition.getPosition()
                    print(x3, z3, y3) # 現在の座標を表示
                    now = math.sqrt((x - x3)**2 + (y - y3)**2)
                    if(min>now): # minに最小値を入れる
                        min=now
                    if(min<now):
                        monitorPlayerMove.right(0)
                        break
                break
            if(flag==1):
                time.sleep(0.2)
                x1, z1, y1 = getPosition.getPosition()
                now = math.sqrt((x - x1)**2 + (y - y1)**2) # 目的座標と現在の座標の距離を計算
                min = now
                monitorPlayerMove.left(1)
                if(min>now):
                    min=now
                while True:
                    past = now
                    time.sleep(0.2)
                    x3, z3, y3 =  getPosition.getPosition()
                    print(x3, z3, y3)
                    now = math.sqrt((x - x3)**2 + (y - y3)**2)
                    if(min>now):
                        min=now
                    if(min<now):
                        monitorPlayerMove.left(0)
                        break
                break
        if(past == now): # 前回の座標と現在の座標が同じ場合
            monitorPlayerMove.right(0)
            monitorPlayerMove.left(1)
            time.sleep(1)
            monitorPlayerMove.left(0)
            x1, z1, y1 = getPosition.getPosition()
            print(x1, z1, y1) # 現在の座標を表示
            now = math.sqrt((x - x1)**2 + (y - y1)**2) # 目的座標と現在の座標の距離を計算
            min = now
            continue

if __name__ == "__main__":
    main()