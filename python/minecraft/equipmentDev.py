import sys
import time
sys.path.append('.')
import pydirectinput

def push(key):
    pydirectinput.keyDown(key)
    time.sleep(0.05)
    pydirectinput.keyUp(key)

def equipment():
    push("space")
    time.sleep(1)
    push("2")
    push("e")
    push("3")
    push("e")
    push("1")

if __name__ == '__main__':
    equipment()