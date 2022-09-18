import pydirectinput
import threading
import sys
import time

sleep_time = 0.0

def pressShift():
    pydirectinput.keyDown('shift')
    time.sleep(sleep_time)
    pydirectinput.keyUp('shift')

def pressW():
    pydirectinput.keyDown('w')
    time.sleep(sleep_time)
    pydirectinput.keyUp('w')

def moveCharacterSneakForward():
    args = sys.argv
    global sleep_time 
    sleep_time = float(args[1])
    thread1 = threading.Thread(target=pressShift)
    thread2 = threading.Thread(target=pressW)
    thread1.start()
    thread2.start()

if __name__ == '__main__':
    moveCharacterSneakForward()