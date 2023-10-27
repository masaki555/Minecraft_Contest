import pydirectinput
import threading
import sys
import time

################################
sleep_time = 0.5
wait_time1 = 0.2
wait_time2 = 100.0
################################

def firstPress():
    pydirectinput.press('w')

def secondPress():
    time.sleep(wait_time1)
    pydirectinput.keyDown('w')

def moveCharacterJumpDash():
    args = sys.argv
    times = int(args[1])
    thread1 = threading.Thread(target=firstPress)
    thread2 = threading.Thread(target=secondPress)
    thread1.start()
    thread2.start()
    time.sleep(times)
    #for i in range(times):
        #pydirectinput.press('space')
        #time.sleep(sleep_time) 
    pydirectinput.keyUp('w')

if __name__ == '__main__':
    moveCharacterJumpDash()