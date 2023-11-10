import win32gui
from PIL import ImageGrab, Image
import pytesseract
from tesseract_pack import data_here

def main():
    hwnd = win32gui.GetForegroundWindow()
    rect = win32gui.GetWindowRect(hwnd)
    print(rect) 

    TESSERACT_EXECUTABLE = data_here + "\\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd =  TESSERACT_EXECUTABLE

    print(pytesseract.pytesseract.tesseract_cmd)

    image = ImageGrab.grab(rect)
    image.show()
    text = pytesseract.image_to_string(image)

    print(text)


if __name__ == "__main__":
    main()
