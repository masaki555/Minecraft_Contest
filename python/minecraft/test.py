import sys
sys.path.append('.')

import init
import initCameraPos
import moveCameraRight
import moveCameraLeft
import moveCameraUp
import moveCameraDown
import clickLeft
import clickRight
import moveCharacterFowerd
import moveCharacterBack
import moveCharacterLeft
import moveCharacterRight
import setTime
import detectZombie2

init.init()
for i in range(1):
    print(i) 
    moveCameraLeft.moveCameraLeft()
print("OK")
for i in range(100):
    detectZombie2.getScreenImage()
init.init()