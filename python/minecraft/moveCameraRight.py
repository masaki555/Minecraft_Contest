import pydirectinput

import time

from minecraft import initCameraPos

################################
sleep_time = 0.01
################################

def moveCameraRight():
    left, top, right, bottom = initCameraPos.getWindowsRect()
#    move = (int)((right - left) / 29 + 0.9)
    move = (int)((right - left) / 90 + 0.9)
    x, y = pydirectinput.position()
    pydirectinput.moveRel(move  , 0 , relative=False) #moveでも動く
    if( x >= ((((right - left) / 90 + 0.9) * 33) + ((right - left)/2)) ):
        initCameraPos.initCameraPos()
    time.sleep(sleep_time)
#    x, y = pydirectinput.position()
#    print({x} , {y})

if __name__ == '__main__':
    moveCameraRight()