import pydirectinput
import sys
import time

################################
sleep_time = 0.5
################################

def moveCharacterJump():
    args = sys.argv
    times = int(args[1])
    for i in range(times):
        pydirectinput.press('space')
        time.sleep(sleep_time)

if __name__ == '__main__':
    moveCharacterJump()