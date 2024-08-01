import sys
import time
sys.path.append('.')
from python.minecraft import pushKey
import pydirectinput
import keyboard

def run(command):
    time.sleep(0.5)
    for i in command:
        pushKey.push(i)

def equipment():
    pushKey.push("2")
    pushKey.push('enter')
    run("/enchant ")
    keyboard.send('@')
    time.sleep(0.5)
    run("p unbreaking 3")
    pushKey.push('enter')
    pushKey.push("e")

    pushKey.push("3")
    pushKey.push('enter')
    run("/enchant ")
    keyboard.send('@')
    time.sleep(0.5)
    run("p unbreaking 3")
    pushKey.push('enter')
    pushKey.push("e")

    pushKey.push("1")
    pushKey.push('enter')
    run("/enchant ")
    keyboard.send('@')
    time.sleep(0.5)
    run("p unbreaking 3")
    pushKey.push('enter')

    pushKey.push('enter')
    run("/tp ")
    keyboard.send('@')
    time.sleep(0.5)
    run("s 0 4 0")
    pushKey.push('enter')

if __name__ == '__main__':
    equipment()