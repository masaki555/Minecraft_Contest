import pydirectinput

import time

################################
sleep_time = 0.01
################################

def clickLeft():
    pydirectinput.mouseDown(button="left")
    time.sleep(sleep_time)
    pydirectinput.mouseUp(button="left")

if __name__ == '__main__':
    clickLeft()