import pydirectinput

import time

from minecraft import initCameraPos

################################
sleep_time = 0.01
################################

def moveCameraDown():
    left, top, right, bottom = initCameraPos.getWindowsRect()
    move = (int)((right - left) / 29 + 0.9)
    x, y = pydirectinput.position()
    if( y <= ((((right - left) / 29 + 0.9) * 3) + ((bottom - top)/2)) ):
        pydirectinput.moveRel(0  , move , relative=False) #moveでも動く
    time.sleep(sleep_time)
#    x, y = direct.position()
#    print({x} , {y})

if __name__ == '__main__':
    moveCameraDown()