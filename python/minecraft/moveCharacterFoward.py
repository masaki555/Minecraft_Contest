import pydirectinput
import sys
import time

def moveCharacterFoward():
    args = sys.argv
    sleep_time = float(args[1])
    pydirectinput.keyDown('w')
    time.sleep(sleep_time)
    pydirectinput.keyUp('w')

if __name__ == '__main__':
    moveCharacterFoward()