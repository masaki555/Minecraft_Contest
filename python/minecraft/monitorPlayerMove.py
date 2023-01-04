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
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('a')
    time.sleep(sleep_time)
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('w')


def forwardRight(sleep_time):
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('d')
    time.sleep(sleep_time)
    pydirectinput.keyUp('d')
    pydirectinput.keyUp('w')

def backLeft(sleep_time):
    pydirectinput.keyDown('s')
    pydirectinput.keyDown('a')
    time.sleep(sleep_time)
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('s')

def backRight(sleep_time):
    pydirectinput.keyDown('s')
    pydirectinput.keyDown('d')
    time.sleep(sleep_time)
    pydirectinput.keyUp('d')
    pydirectinput.keyUp('s')


def setDash(dash_flag):
    if(dash_flag == 1):
        pydirectinput.keyDown('ctrl')
    else:
        pydirectinput.keyUp('ctrl')




def monitorPlayerMove():
    pre_dash_flag = 0

    Move_Data_File = open('python/tmp/Share_Move_Data.txt','r',encoding='UTF-8')
    move_data = Move_Data_File.read().split(',')
    pre_dash_flag = int(move_data[2])
    Move_Data_File.close

    Move_Log_File = open('python/tmp/Move_Log.txt', 'w', encoding = 'UTF-8')
    Move_Log_File.write('key,sleep_time,dash_flag\n')


    while True:
        Move_Data_File = open('python/tmp/Share_Move_Data.txt','r',encoding='UTF-8')
        
        # move_dataは('移動のkey', '実行し続ける時間(秒)', 'ダッシュするフラグ')のタプル
        
        try:
            move_data = Move_Data_File.read().split(',')
            key = move_data[0]       
            sleep_time = float(move_data[1])
            #print(sleep_time)
            dash_flag = int(move_data[2])
        except IndexError as e:
            #print(e)
            Move_Log_File.write('error\n')
            continue

        Move_Log_File.write(move_data[0] + ',' + move_data[1] + ',' + move_data[2] + '\n')

        # dash_flagが変化した場合のみctrlキーを操作する
        if(pre_dash_flag != dash_flag):
            setDash(dash_flag)
            pre_dash_flag = dash_flag
        else:
            pass

        if(key == 'F'):
            forward(sleep_time)
        elif(key == 'L'):
            left(sleep_time)
        elif(key == 'R'):
            right(sleep_time)
        elif(key == 'B'):
            back(sleep_time)
        elif(key == 'FL'):
            forwardLeft(sleep_time)
        elif(key == 'FR'):
            forwardRight(sleep_time)
        elif(key == 'BL'):
            backLeft(sleep_time)
        elif(key == 'BR'):
            backRight(sleep_time)
        elif(key == 'Finish'):
            break
        elif(key == 'Wait'):
            pass
        else:
            print('error: key = ' + key + '未設定のkeyです．プレイヤの移動の監視をエラー終了します．')
            break

        time.sleep(0)

        Move_Data_File.close()

    Move_Log_File.close()


if __name__ == '__main__':
    monitorPlayerMove()
