import pydirectinput
import sys

def upKey(key):
    pydirectinput.keyUp(key)

if __name__ == '__main__':
    upKey(sys.argv[1])