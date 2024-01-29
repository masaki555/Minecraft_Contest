import sys
sys.path.append('.')

from python.minecraft import command

################################
cmd = "/gamemode c"
################################

# ゲームモードをクリエイティブに設定する
def setCreativeMode():
    command.run(cmd)

if __name__ == '__main__':
    setCreativeMode()