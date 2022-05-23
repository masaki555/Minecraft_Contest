import pydirectinput

import time

from minecraft import initCameraPos

################################
sleep_time = 0.05
################################

def moveCameraLeft():
    left, top, right, bottom = initCameraPos.getWindowsRect()
#    move = (int)((right - left) / 29 + 0.9)
    move = (int)((right - left) / 90 + 0.9)
    x, y = pydirectinput.position()
    pydirectinput.moveRel(move * -1 , 0 , relative=False) #moveでも動く
    if( x <= (((right - left)/2)) - (((right - left) / 90 + 0.9) * 33) ):
        initCameraPos.initCameraPos()
    time.sleep(sleep_time)
#    x, y = direct.position()
#    print({right}, {left},{x} , {y}, (((right - left)/2)) - ((((right - left) / 29 + 0.9) * 11)) )

if __name__ == '__main__':
    moveCameraLeft()