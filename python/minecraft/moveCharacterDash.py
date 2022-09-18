import pydirectinput
import threading
import sys
import time

################################
sleep_time = 0.0
wait_time = 0.2
################################

def firstPress():
    pydirectinput.press('w')
    time.sleep(sleep_time+wait_time)

def secondPress():
    time.sleep(wait_time)
    pydirectinput.keyDown('w')
    time.sleep(sleep_time)
    pydirectinput.keyUp('w')

def moveCharacterDash():
    args = sys.argv
    global sleep_time
    sleep_time = float(args[1])
    thread1 = threading.Thread(target=firstPress)
    thread2 = threading.Thread(target=secondPress)
    thread1.start()
    thread2.start()

if __name__ == '__main__':
    moveCharacterDash()