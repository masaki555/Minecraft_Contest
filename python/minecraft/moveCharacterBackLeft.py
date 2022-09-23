import pydirectinput
import threading
import time
import sys

sleep_time = 0.0

def pressA():
    pydirectinput.keyDown('a')
    time.sleep(sleep_time)
    pydirectinput.keyUp('a')

def pressS():
    pydirectinput.keyDown('s')
    time.sleep(sleep_time)
    pydirectinput.keyUp('s')

def moveCharacterBackLeft():
    args = sys.argv
    global sleep_time
    sleep_time = float(args[1])
    thread1 = threading.Thread(target=pressA)
    thread2 = threading.Thread(target=pressS)
    thread1.start()
    thread2.start()

if __name__ == '__main__':
    moveCharacterBackLeft()