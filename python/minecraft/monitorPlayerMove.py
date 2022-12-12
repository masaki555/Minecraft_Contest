import pydirectinput
import threading
import sys
import time

def forward(sleep_time):
    pydirectinput.keyDown('w')
    time.sleep(sleep_time)
    pydirectinput.keyUp('w')

def left(sleep_time):
    pydirectinput.keyDown('a')
    time.sleep(sleep_time)
    pydirectinput.keyUp('a')

def right(sleep_time):
    pydirectinput.keyDown('d')
    time.sleep(sleep_time)
    pydirectinput.keyUp('d')

def back(sleep_time):
    pydirectinput.keyDown('s')
    time.sleep(sleep_time)
    pydirectinput.keyUp('s')

def forwardLeft(sleep_time):
    #### threading.Thread(target = よびだす関数名, args = 引数(タプル) ) で指定
    thread1 = threading.Thread(target=forward,args=(sleep_time,))
    thread2 = threading.Thread(target=left, args=(sleep_time,))
    thread1.start()
    thread2.start()

def forwardRight(sleep_time):
    thread1 = threading.Thread(target=forward,args=(sleep_time,))
    thread2 = threading.Thread(target=right, args=(sleep_time,))
    thread1.start()
    thread2.start()

def backLeft(sleep_time):
    thread1 = threading.Thread(target=back,args=(sleep_time,))
    thread2 = threading.Thread(target=left, args=(sleep_time,))
    thread1.start()
    thread2.start()

def backRight(sleep_time):
    thread1 = threading.Thread(target=back,args=(sleep_time,))
    thread2 = threading.Thread(target=right, args=(sleep_time,))
    thread1.start()
    thread2.start()

############## ジャンプ，ダッシュはsystem関数の方でいい説 ##############

# def jump():
#     pydirectinput.press('space')
#     time.sleep(0.5)

# def dash_1(sleep_time):
#     pydirectinput.press('w')
#     time.sleep(sleep_time+0.2)

# def dash_2(sleep_time):
#     time.sleep(0.2)
#     pydirectinput.keyDown('w')
#     time.sleep(sleep_time)
#     pydirectinput.keyUp('w')

# def dash(sleep_time):
#     thread1 = threading.Thread(target=dash_1, args=(sleep_time,))
#     thread2 = threading.Thread(target=dash_2, args=(sleep_time,))
#     thread1.start()
#     thread2.start()

#########################################################################

def monitorPlayerMove():
    
    while True:
        f=open('python/movedata/share_MoveData.txt','r',encoding='UTF-8')
        datalist = f.readlines()
        # datalist[0]は
        # datalist[1]はsleepする時間(秒)
        key = datalist[0]       
        key=key.rstrip('\n')
        st = datalist[1]
        st= st.rstrip('\n')
        sleep_time = int(st)

        if(key=='F'):
            forward(sleep_time)
        elif(key=='L'):
            left(sleep_time)
        elif(key=='R'):
            right(sleep_time)
        elif(key=='B'):
            back(sleep_time)
        elif(key=='FL'):
            forwardLeft(sleep_time)
        elif(key=='FR'):
            forwardRight(sleep_time)
        elif(key=='BL'):
            backLeft(sleep_time)
        elif(key=='BR'):
            backRight(sleep_time)
        elif(key=='Finish'):
            break
        elif(key=='Wait'):
            pass
        else:
            print('error')
        time.sleep(0.1)
        f.close()



if __name__ == '__main__':
    monitorPlayerMove()
