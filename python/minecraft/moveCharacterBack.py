import pydirectinput
import sys
import time


def moveCharacterBack():
    args = sys.argv
    sleep_time = float(args[1])
    pydirectinput.keyDown('s')
    time.sleep(sleep_time)
    pydirectinput.keyUp('s')

if __name__ == '__main__':
    moveCharacterBack()