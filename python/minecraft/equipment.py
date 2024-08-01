import sys
import time
sys.path.append('.')
from python.minecraft import pushKey
import random
import pydirectinput
import keyboard

def run(command):
    time.sleep(0.5)
    for i in command:
        pushKey.push(i)

def equipment():
    pushKey.push('enter')
    run("/give ")
    keyboard.send('@')
    time.sleep(0.5)
    run("s diamond")
    pydirectinput.keyDown("shift")
    keyboard.send('_')
    pydirectinput.keyUp("shift")
    time.sleep(0.5)
    run("sword")
    pushKey.push('enter')

    pushKey.push('enter')
    run("/give ")
    keyboard.send('@')
    time.sleep(0.5)
    run("s diamond")
    pydirectinput.keyDown("shift")
    keyboard.send('_')
    pydirectinput.keyUp("shift")
    time.sleep(0.5)
    run("helmet")
    pushKey.push('enter')

    pushKey.push('enter')
    run("/give ")
    keyboard.send('@')
    time.sleep(0.5)
    run("s diamond")
    pydirectinput.keyDown("shift")
    keyboard.send('_')
    pydirectinput.keyUp("shift")
    time.sleep(0.5)
    run("boots")
    pushKey.push('enter')

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

    x = random.randint(-25,20)
    z = random.randint(-25,20)
    tp = "s "+str(x)+" 4 "+str(z)
    pushKey.push('enter')
    run("/tp ")
    keyboard.send('@')
    time.sleep(0.5)
    run(tp)
    pushKey.push('enter')

if __name__ == '__main__':
    equipment()
