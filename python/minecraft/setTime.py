import sys
sys.path.append('.')

from python.minecraft import command

################################
cmd = "/time set 17000"
################################

#　ゲーム内時間を夜に設定する
def setTime():
    command.run(cmd)

if __name__ == '__main__':
    setTime()