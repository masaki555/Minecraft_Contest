import win32gui
import win32con
import win32api
import pydirectinput as direct
import pyautogui
import time
import sys

slee_time = 0.01
try:
    if len(sys.argv) >= 2:
        mcapp = win32gui.FindWindow(None,'Minecraft: Education Edition')
        time.sleep(1.00)
        left, top, right, bottom = win32gui.GetWindowRect(mcapp)
        print({left} , {top} , {right} , {bottom} )
        init_x , init_y = (int)((left + right) / 2 + 0.9) , (int)((top + bottom) /2 + 0.9 + 10)  #10はウィンドウのメニューバー
        direct.moveTo(init_x , init_y)
        time.sleep(slee_time)
        print( "init後" , {init_x} , {init_y})
        x, y = direct.position()
        print( "moveTo後" , {x} , {y})
        win32gui.SetForegroundWindow(mcapp)         #ウィンドウの指定
#        win32gui.SetWindowPos(mcapp,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        direct.keyDown('esc')
        direct.keyUp('esc')
        time.sleep(slee_time)
        direct.moveRel(0 , 0 , relative=False) #moveでも動く
        time.sleep(slee_time)
        
        if sys.argv[1] == "click":                  #左クリック
            time.sleep(1.00)
            direct.mouseDown(button="left")
            time.sleep(float(sys.argv[2]))
            direct.mouseUp(button="left")
            time.sleep(slee_time)
            print("キーボード操作後" ,{x} , {y})
            for i in range(4):
                move = (int)((right - left) / 29 + 0.9)
                direct.moveRel(move * 3 , 0 , relative=False) #moveでも動く
                time.sleep(slee_time)
                x, y = direct.position()
                print({x} , {y})
            direct.moveTo(init_x , init_y)
            x, y = direct.position()
            print({x} , {y})
            #print({init_x} , {init_y})
                
        elif sys.argv[1] == "rclick":               #右クリック
            time.sleep(1.00)
            direct.mouseDown(button="right")
            time.sleep(float(sys.argv[2]))
            direct.mouseUp(button="right")
        elif sys.argv[1] == "press":                 #キーボード
            time.sleep(1.00)
            direct.keyDown(sys.argv[2])
            time.sleep(float(sys.argv[3]))
            direct.keyUp(sys.argv[2])
        else:
            sys.exit()
        direct.keyDown('esc')
        direct.keyUp('esc')
        time.sleep(0.1)
    else:
        sys.exit()
    
except KeyboardInterrupt:
    sys.exit()




