import sys
import time
sys.path.append('.')
from python.minecraft import pushKey

def run(command):
    time.sleep(0.5)
    for i in command:
        pushKey.push(i)

def equipment():
    time.sleep(1)
    pushKey.push("2")
    pushKey.push("e")
    pushKey.push("3")
    pushKey.push("e")
    pushKey.push("1")

if __name__ == '__main__':
    equipment()