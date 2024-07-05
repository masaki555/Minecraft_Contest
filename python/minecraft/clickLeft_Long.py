import pydirectinput
import time

################################
sleep_time = 1.50
################################

def clickLeft_long():
    pydirectinput.keyDown('q')
    time.sleep(sleep_time)
    pydirectinput.keyUp('q')

if __name__ == '__main__':
    clickLeft_long()