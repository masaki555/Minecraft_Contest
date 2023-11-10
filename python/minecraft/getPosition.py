import win32gui
from PIL import ImageGrab, Image
import pytesseract
from tesseract_pack import data_here
import time
import pydirectinput

##################################
game_name = 'Minecraft Education'
sleep_time = 0.05
##################################

def main():
    mcapp = win32gui.FindWindow(None,game_name)
    time.sleep(sleep_time)
    win32gui.SetForegroundWindow(mcapp)         #ウィンドウの指定
    time.sleep(sleep_time)
    pydirectinput.keyDown('esc')
    pydirectinput.keyUp('esc')
    time.sleep(sleep_time)

    hwnd = win32gui.GetForegroundWindow()
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bottom)
    cordinate = (left, top+130, right-780, bottom-845)

    TESSERACT_EXECUTABLE = data_here + "\\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd =  TESSERACT_EXECUTABLE

    image = ImageGrab.grab(cordinate)
    image.save('image.png')
    image.show()
    text = pytesseract.image_to_string(image)

    print(text)


if __name__ == "__main__":
    main()
