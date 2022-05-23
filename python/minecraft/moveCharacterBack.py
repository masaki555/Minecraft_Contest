import pydirectinput

import time

################################
sleep_time = 0.135
################################

def moveCharacterBack():
    pydirectinput.keyDown('s')
    time.sleep(sleep_time)
    pydirectinput.keyUp('s')

if __name__ == '__main__':
    moveCharacterBack()