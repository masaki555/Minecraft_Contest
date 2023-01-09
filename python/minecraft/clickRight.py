import pydirectinput

import time

################################
sleep_time = 1.50
################################

def clickLeft():
    pydirectinput.keyDown('e')
    time.sleep(sleep_time)
    pydirectinput.keyUp('e')

if __name__ == '__main__':
    clickLeft()