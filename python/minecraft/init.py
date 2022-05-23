import time

import win32gui
import win32con
import win32api
import pydirectinput

################################
game_name = 'Minecraft: Education Edition'
sleep_time = 0.05
################################

def init():
    mcapp = win32gui.FindWindow(None,game_name)
    time.sleep(sleep_time)
    win32gui.SetForegroundWindow(mcapp)         #ウィンドウの指定
    time.sleep(sleep_time)
    hwnd = win32gui.GetForegroundWindow()
    time.sleep(sleep_time)
    win32gui.MoveWindow(hwnd, 0, -10, 940, 1000, True)
    time.sleep(sleep_time)
    left, top, right, bottom = win32gui.GetWindowRect(mcapp)
#   print({left} , {top} , {right} , {bottom} )
    init_x , init_y = (int)((left + right) / 2 + 0.9) , (int)((top + bottom) /2 + 0.9 + 10)  #10はウィンドウのメニューバーのサイズ
    pydirectinput.moveTo(init_x , init_y)
    time.sleep(sleep_time)
#   print( "init後" , {init_x} , {init_y})
#   x, y = pydirectinput.position()
#    print( "moveTo後" , {x} , {y})  
#   win32gui.SetWindowPos(mcapp,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE) #ウィンドウの指定(常に全面表示)
    pydirectinput.keyDown('esc')
    pydirectinput.keyUp('esc')
    time.sleep(sleep_time)
    pydirectinput.moveRel(0 , 0 , relative=False)  #アクティブ化したウィンドウを操作
    time.sleep(sleep_time)

if __name__ == '__main__':
    init()    