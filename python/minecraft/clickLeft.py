import pydirectinput

import time

################################
sleep_time = 0.01
################################

def clickLeft():
    pydirectinput.keyDown('q')
    time.sleep(sleep_time)
    pydirectinput.keyUp('q')

if __name__ == '__main__':
    clickLeft()