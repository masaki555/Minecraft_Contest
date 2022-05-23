import pydirectinput

import time

################################
sleep_time = 0.135
################################

def moveCharacterRight():
    pydirectinput.keyDown('d')
    time.sleep(sleep_time)
    pydirectinput.keyUp('d')

if __name__ == '__main__':
    moveCharacterRight()