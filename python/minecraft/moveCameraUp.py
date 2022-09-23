import pydirectinput

import time

from minecraft import initCameraPos

################################
sleep_time = 0.01
################################

def moveCameraUp():
    left, top, right, bottom = initCameraPos.getWindowsRect()
    move = (int)((right - left) / 29 + 0.9)
    x, y = pydirectinput.position()
    if( y >= (((bottom - top)/2) - (((right - left) / 29 + 0.9) * 2)) ):
        pydirectinput.moveRel(0  , move * -1 , relative=False) #moveでも動く
    time.sleep(sleep_time)
#    x, y = direct.position()
#    print({x} , {y})

if __name__ == '__main__':
    moveCameraUp()