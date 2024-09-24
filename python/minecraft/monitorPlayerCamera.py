import pydirectinput
import time

def left(sleep_time):
    pydirectinput.keyDown('left')
    #time.sleep(sleep_time)
    #pydirectinput.keyUp('left')

def right(sleep_time):
    pydirectinput.keyDown('right')
    #time.sleep(sleep_time)
    #pydirectinput.keyUp('right')

def up(sleep_time):
    pydirectinput.keyDown('up')
    #time.sleep(sleep_time)
    #pydirectinput.keyUp('up')

def down(sleep_time):
    pydirectinput.keyDown('down')
    #time.sleep(sleep_time)
    #pydirectinput.keyUp('down')

def center():
    pydirectinput.keyDown('End')
    time.sleep(0.1)
    pydirectinput.keyUp('End')

def keyRelese():
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('right')
    pydirectinput.keyUp('up')
    pydirectinput.keyUp('down')
    pydirectinput.keyUp('End')


def monitorPlayerCamera():
    while True:
        Camera_Data_File = open('python/tmp/Share_Camera_Data.txt','r',encoding='UTF-8')
        
        # move_dataは('移動のkey', '実行し続ける時間(秒)', 'ダッシュするフラグ')のタプル
        try:
            move_data = Camera_Data_File.read().split(',')
            key = move_data[0]       
            sleep_time = float(move_data[1])
        except IndexError as e:
            #print(e)
            continue

        if(key == 'L'):
            left(sleep_time)
        elif(key == 'R'):
            right(sleep_time)
        elif(key == 'U'):
            up(sleep_time)
        elif(key == 'D'):
            down(sleep_time)
        elif(key == 'C'):
            center()
        elif(key == 'Wait'):
            keyRelese()
        else:
            print('error: key = ' + key + '未設定のkeyです.プレイヤのカメラの監視をエラー終了します．')
            break

        time.sleep(0)
        Camera_Data_File.close()

if __name__ == '__main__':
    monitorPlayerCamera()
