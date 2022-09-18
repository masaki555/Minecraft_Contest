import pydirectinput
import threading
import sys
import time

sleep_time = 0.0

def pressShift():
    pydirectinput.keyDown('shift')
    time.sleep(sleep_time)
    pydirectinput.keyUp('shift')

def pressD():
    pydirectinput.keyDown('d')
    time.sleep(sleep_time)
    pydirectinput.keyUp('d')

def moveCharacterSneakRight():
    args = sys.argv
    global sleep_time 
    sleep_time = float(args[1])
    thread1 = threading.Thread(target=pressShift)
    thread2 = threading.Thread(target=pressD)
    thread1.start()
    thread2.start()

if __name__ == '__main__':
    moveCharacterSneakRight()