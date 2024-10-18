import sys
import time
sys.path.append('.')
from python.minecraft import command

################################
cmd = "/time set 2000"
################################

#ゲーム内時間を朝に設定する
def setMorning():
    time.sleep(1)
    command.run(cmd)

if __name__ == '__main__':
    setMorning()