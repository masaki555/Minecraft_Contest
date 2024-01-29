import pydirectinput
import time

# ゲーム内でコマンドを実行する
def run(command):
    # コマンド入力欄を開く
    pydirectinput.press('enter')
    time.sleep(0.1)

    # コマンドを入力する
    [pydirectinput.press(c) for c in command]
    pydirectinput.press('enter')