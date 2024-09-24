import pydirectinput
import sys

def downKey(key):
    pydirectinput.keyDown(key)

if __name__ == '__main__':
    downKey(sys.argv[1])