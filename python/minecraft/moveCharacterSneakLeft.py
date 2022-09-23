import pydirectinput
import threading
import sys
import time

sleep_time = 0.0

def pressShift():
    pydirectinput.keyDown('shift')
    time.sleep(sleep_time)
    pydirectinput.keyUp('shift')

def pressA():
    pydirectinput.keyDown('a')
    time.sleep(sleep_time)
    pydirectinput.keyUp('a')

def moveCharacterSneakLeft():
    args = sys.argv
    global sleep_time 
    sleep_time = float(args[1])
    thread1 = threading.Thread(target=pressShift)
    thread2 = threading.Thread(target=pressA)
    thread1.start()
    thread2.start()

if __name__ == '__main__':
    moveCharacterSneakLeft()