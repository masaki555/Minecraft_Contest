import pydirectinput

import time

import sys

################################
sleep_time = 0.50
################################

def pushKey(key):
    pydirectinput.keyDown(key)
    time.sleep(sleep_time)
    pydirectinput.keyUp(key)

if __name__ == '__main__':
    pushKey(sys.argv[1])