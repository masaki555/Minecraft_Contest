import pydirectinput
import time

################################
sleep_time = 0.01
################################

def center():
    pydirectinput.keyDown("\\")
    time.sleep(sleep_time)
    pydirectinput.keyUp("\\")
    #pydirectinput.keyDown("end")
    #time.sleep(sleep_time)
    #pydirectinput.keyUp("end")


if __name__ == '__main__':
    center()