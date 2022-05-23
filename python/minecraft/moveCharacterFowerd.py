import pydirectinput

import time

################################
sleep_time = 0.135
################################

def moveCharacterFowerd():
    pydirectinput.keyDown('w')
    time.sleep(sleep_time)
    pydirectinput.keyUp('w')

if __name__ == '__main__':
    moveCharacterFowerd()