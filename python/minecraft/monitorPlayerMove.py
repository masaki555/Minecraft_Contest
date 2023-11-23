import pydirectinput
import threading
import sys
import time

def forward(updown_flag):
    if(updown_flag == 1):
        pydirectinput.keyDown('w')
    else:
        pydirectinput.keyUp('w')

def left(updown_flag):
    if(updown_flag == 1):
        pydirectinput.keyDown('a')
    else:
        pydirectinput.keyUp('a')

def right(updown_flag):
    if(updown_flag == 1):
        pydirectinput.keyDown('d')
    else:
        pydirectinput.keyUp('d')

def back(updown_flag):
    if(updown_flag == 1):
        pydirectinput.keyDown('s')
    else:
        pydirectinput.keyUp('s')

def forwardLeft(updown_flag):
    if(updown_flag == 1):
        pydirectinput.keyDown('w')
        pydirectinput.keyDown('a')
    else:
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('a')

def forwardRight(updown_flag):
    if(updown_flag == 1):
        pydirectinput.keyDown('w')
        pydirectinput.keyDown('d')
    else:
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('d')

def backLeft(updown_flag):
    if(updown_flag == 1):
        pydirectinput.keyDown('s')
        pydirectinput.keyDown('a')
    else:
        pydirectinput.keyUp('s')
        pydirectinput.keyUp('a')

def backRight(updown_flag):
    if(updown_flag == 1):
        pydirectinput.keyDown('s')
        pydirectinput.keyDown('d')
    else:
        pydirectinput.keyUp('s')
        pydirectinput.keyUp('d')

def setMove(move_key, updown_flag):
    if(move_key == 'F'):
        forward(updown_flag)
        return 1
    elif(move_key == 'L'):
        left(updown_flag)
        return 1
    elif(move_key == 'R'):
        right(updown_flag)
        return 1
    elif(move_key == 'B'):
        back(updown_flag)
        return 1
    elif(move_key == 'FL'):
        forwardLeft(updown_flag)
        return 2
    elif(move_key == 'FR'):
        forwardRight(updown_flag)
        return 2
    elif(move_key == 'BL'):
        backLeft(updown_flag)
        return 2
    elif(move_key == 'BR'):
        backRight(updown_flag)
        return 2
    elif(move_key == 'Wait'):
        return 3   
    elif(move_key == 'Finish'):
        return 0
    else:
        print('error: move_key = ' + move_key + '未設定のkeyです．プレイヤの移動の監視をエラー終了します．')
        return -1

def setDash(dash_flag):
    if(dash_flag == '1'):
        pydirectinput.keyDown('ctrl')
    else:
        pydirectinput.keyUp('ctrl')


        

def monitorPlayerMove():
    loop_flag = 3

    Move_Data_File = open('python/tmp/Share_Move_Data.txt','r',encoding='UTF-8')
    
    # move_dataは('移動のkey','ダッシュするフラグ')のタプル
    pre_move_key, pre_dash_flag = Move_Data_File.read().split(',')

    Move_Log_File = open('python/tmp/Move_Log.txt', 'w', encoding = 'UTF-8')
    Move_Log_File.write('key,dash_flag\n')
    Move_Log_File.close()

    while 0 < loop_flag:
        Move_Data_File = open('python/tmp/Share_Move_Data.txt','r',encoding='UTF-8')
        
        try:
            move_key, dash_flag = Move_Data_File.read().split(',')
        except IndexError as e:
            print('error')
        
        if(pre_move_key != move_key):
            Move_Log_File = open('python/tmp/Move_Log.txt', 'a', encoding = 'UTF-8')
            Move_Log_File.write(move_key + ',' + dash_flag+'\n')
            Move_Log_File.close()

            if(loop_flag != 3): #   キャラが立ち止まっていない(loop_flag != 3)ならキーを離す
                setMove(pre_move_key, 0)

            #   立ち止まるときは3，斜め移動の時は2，前後左右の時は1，終了時は0，エラー時は-1を代入
            loop_flag = setMove(move_key, 1)
            pre_move_key = move_key
            
        elif(pre_dash_flag != dash_flag):
            Move_Log_File = open('python/tmp/Move_Log.txt', 'a', encoding = 'UTF-8')
            Move_Log_File.write(move_key + ',' + dash_flag+'\n')
            Move_Log_File.close()

            setDash(dash_flag)
            pre_dash_flag = dash_flag
        else:
            pass

        time.sleep(0.1)
        Move_Data_File.close()

 
    print('pythonプログラムによる監視を終了しました')


if __name__ == '__main__':
    monitorPlayerMove()
