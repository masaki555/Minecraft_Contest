import pydirectinput
import time
import sys

################################
sleep_time = 0.01
################################

def clickLeft_Continuous(n):
    i = 0
    num = int(n)
    while i < num:
        pydirectinput.keyDown("q")
        time.sleep(sleep_time)
        pydirectinput.keyUp("q")
        i = i + 1

if __name__ == "__main__":
    clickLeft_Continuous(sys.argv[1])
