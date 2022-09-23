import pydirectinput
import threading
import time
import sys

sleep_time = 0.0

def pressW():
    pydirectinput.keyDown('w')
    time.sleep(sleep_time)
    pydirectinput.keyUp('w')

def pressA():
    pydirectinput.keyDown('a')
    time.sleep(sleep_time)
    pydirectinput.keyUp('a')

def moveCharacterForwardLeft():
    args = sys.argv
    global sleep_time 
    sleep_time = float(args[1])
    thread1 = threading.Thread(target=pressW)
    thread2 = threading.Thread(target=pressA)
    thread1.start()
    thread2.start()

if __name__ == '__main__':
    moveCharacterForwardLeft()