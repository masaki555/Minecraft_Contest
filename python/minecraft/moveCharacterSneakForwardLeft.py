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

def pressShift():
    pydirectinput.keyDown('shift')
    time.sleep(sleep_time)
    pydirectinput.keyUp('shift')

def moveCharacterSneakForwardLeft():
    args = sys.argv
    global sleep_time 
    sleep_time = float(args[1])
    thread1 = threading.Thread(target=pressW)
    thread2 = threading.Thread(target=pressA)
    thread3 = threading.Thread(target=pressShift)
    thread1.start()
    thread2.start()
    thread3.start()

if __name__ == '__main__':
    moveCharacterSneakForwardLeft()