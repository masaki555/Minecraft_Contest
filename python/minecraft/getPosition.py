import win32gui
from PIL import ImageGrab, Image
import pytesseract
from tesseract_pack import data_here
import time
import pydirectinput
import re
import monitorPlayerMove

##################################
game_name = 'Minecraft Education'
sleep_time = 0.05
##################################

def add_to_next_element(lst, indx):
    if indx + 1 >= len(lst):
        lst.append('')
    lst[indx + 1] = str(lst[indx])[-1] + lst[indx + 1]
    lst[indx] = str(lst[indx])[:-1]
    return lst

'''
ocrで,を認識しない場合があるため、,なしで座標を整形する
x,z,yで座標は構成され、xは40未満,zは4(固定),yは40未満である
2桁ごとに値を分割し、その後にyが1桁の整数になるように調整する
'''
def format_position(pos):
    y_value = '4'

    pos.replace(',', '').replace('.', '').replace(' ','')
    pattern = r'(-?[1-9][0-9]?)'
    pos = re.findall(pattern, pos)
    if len(pos) == 2:
        pos = add_to_next_element(pos, 1)
    if pos[1] == '-':
        pos = add_to_next_element(pos, 1)
    if len(pos[1]) == 0:
        pos = add_to_next_element(pos, 0)
    if pos[1] != '4':
        pos = add_to_next_element(pos, 1)
        pos = add_to_next_element(pos, 0)
    while len(pos[1]) >= 2:
        pos = add_to_next_element(pos, 1)

    pos = list(map(int, pos))

    return pos


def getPosition():
    mcapp = win32gui.FindWindow(None,game_name)
    time.sleep(sleep_time)
    win32gui.SetForegroundWindow(mcapp)         #ウィンドウの指定
    time.sleep(sleep_time)
    pydirectinput.keyDown('esc')
    pydirectinput.keyUp('esc')
    time.sleep(sleep_time)

    hwnd = win32gui.GetForegroundWindow()
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    cordinate = (left+95, top+131, right-725, bottom-845)

    TESSERACT_EXECUTABLE = data_here + "\\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd =  TESSERACT_EXECUTABLE
    tesseract_args = '-c tessedit_char_whitelist="0123456789-,. "'

    time.sleep(1)

    # スクショと文字認識
    image = ImageGrab.grab(cordinate)
    image.save('image.png')

    text = pytesseract.image_to_string(image, config=tesseract_args)
    position = format_position(text)


    return position

if __name__ == '__main__':
    getPosition()
