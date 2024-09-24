import pydirectinput
import time
import sys

################################
sleep_time = 0.01
################################

def eat(n):
    pydirectinput.keyDown(n)
    time.sleep(sleep_time)
    pydirectinput.keyUp(n)
    pydirectinput.keyDown('e')
    time.sleep(2)
    pydirectinput.keyUp('e')
    pydirectinput.keyDown('1')
    time.sleep(sleep_time)
    pydirectinput.keyUp('1')

if __name__ == '__main__':
    eat(sys.argv[1])