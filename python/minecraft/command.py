import time
import sys
sys.path.append('.')
from python.minecraft import pushKey

# ゲーム内でコマンドを実行する
def run(command):
    # コマンド入力欄を開く
    pushKey.push('enter')
    # コマンドを入力する
    time.sleep(0.5)
    for i in command:
        pushKey.push(i)
    pushKey.push("enter")