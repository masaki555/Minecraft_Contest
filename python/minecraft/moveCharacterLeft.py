import pydirectinput

import time

################################
sleep_time = 0.135
################################

def moveCharacterLeft():
    pydirectinput.keyDown('a')
    time.sleep(sleep_time)
    pydirectinput.keyUp('a')

if __name__ == '__main__':
    moveCharacterLeft()