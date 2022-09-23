import pydirectinput
import sys
import time

def moveCharacterLeft():
    args = sys.argv
    sleep_time = float(args[1])
    pydirectinput.keyDown('a')
    time.sleep(sleep_time)
    pydirectinput.keyUp('a')

if __name__ == '__main__':
    moveCharacterLeft()