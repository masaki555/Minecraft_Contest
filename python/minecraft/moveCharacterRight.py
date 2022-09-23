import pydirectinput
import sys
import time

def moveCharacterRight():
    args = sys.argv
    sleep_time = float(args[1])
    pydirectinput.keyDown('d')
    time.sleep(sleep_time)
    pydirectinput.keyUp('d')

if __name__ == '__main__':
    moveCharacterRight()