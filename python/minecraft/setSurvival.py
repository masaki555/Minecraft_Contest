import sys
sys.path.append('.')

from python.minecraft import command

################################
cmd = "/gamemode s"
################################

# # ゲームモードをサバイバルに設定する
def setSurvivalMode():
    command.run(cmd)

if __name__ == '__main__':
    setSurvivalMode()