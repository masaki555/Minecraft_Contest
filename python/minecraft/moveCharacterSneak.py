import pydirectinput
import sys
import time


def moveCharacterSneak():
    args = sys.argv
    sleep_time = float(args[1])
    pydirectinput.keyDown('shift')
    time.sleep(sleep_time)
    pydirectinput.keyUp('shift')

if __name__ == '__main__':
    moveCharacterSneak()