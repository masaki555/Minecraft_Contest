import pydirectinput
import time
import sys

################################
sleep_time = 0.05
################################

def push(key):
    pydirectinput.keyDown(key)
    time.sleep(sleep_time)
    pydirectinput.keyUp(key)

if __name__ == '__main__':
    push(sys.argv[1])