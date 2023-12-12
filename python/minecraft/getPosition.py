import os
import win32gui
from PIL import ImageGrab, Image
import numpy as np 

script_dir = os.path.dirname(os.path.abspath(__file__)) 
data_dir= script_dir + '/posdata/'

def getPosition():

    hwnd = win32gui.GetForegroundWindow()
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    
    cordinate = (left+102, top+137, right-730, bottom-849)
    
    # スクショと文字認識
    image = ImageGrab.grab(cordinate)
    
    imageGrayScale = np.array(image.convert('L'), 'f')
    imageGrayScale = (imageGrayScale < 150) * 255
    imageGrayScale = Image.fromarray(imageGrayScale)
    imageGrayScale = imageGrayScale.convert('RGBA')

    widthGrayScale = imageGrayScale.size[0]
    zahyouList=[]
    screenSize=0
    colorType=0
    flagWideth=0
    flagMinus=0
    flagLine=0
    WHITE_PIXEL="(255, 255, 255, 255)"
    BLACK_PIXEL="(0, 0, 0, 255)"
    positionValue=''    
    binary=''
    line1=''
    line2=''
    line4=''
    
    while screenSize < widthGrayScale :
        imageCrop = imageGrayScale.crop((screenSize, 0, screenSize+12,14))
        
        widthC, heightC = imageCrop.size
        imageArray = np.empty((heightC, widthC), dtype = object)
        
        for y in range(heightC):
            for x in range(widthC):
            # 順次、ピクセルの色の数値を代入している
                imageArray[y][x] = imageCrop.getpixel((x, y))
                
        with open(data_dir+'imageColorValues.txt', 'w', encoding='utf-8') as imageToHeightValue:
            for y in range(heightC):
                for x in range(widthC):
                    
                    if(flagWideth==0):
                        if(str(imageArray[y][x])==WHITE_PIXEL):
                            colorType=0
                        elif(str(imageArray[y][x])==BLACK_PIXEL):
                            colorType=1
                        else:
                            print("Error:")
                        
                        flagWideth=1
                    elif(flagWideth==1):
                        if(str(imageArray[y][x])==WHITE_PIXEL and colorType==0):
                            binary+=str(0)
                        elif(str(imageArray[y][x])==BLACK_PIXEL and colorType==1):
                            binary+=str(1)
                        else:
                            print("Error:")
                            
                        flagWideth=0
                        
                if(flagLine==0):
                    line1=binary
                    flagLine=1
                    
                elif(flagLine==1):
                    line2=binary
                    
                    if(line1==line2):
                        imageToHeightValue.write(str(line1))
                        
                    else:
                        print("error")
                    
                    flagLine=0
                
                binary=''
                
        with open(data_dir+'imageColorValues.txt', 'r', encoding='utf-8') as imageToHeightValue,open(data_dir+'imageALLColorValues.txt', 'r+', encoding='utf-8') as sampleData:           
            
            line4 = imageToHeightValue.readline()            
            sampleData.seek(0)
            
            while True:
                lineSampleBinary = sampleData.readline()
                lineSampleValue = sampleData.readline()
                lineSampleBinary = lineSampleBinary.strip()
                
                if not lineSampleBinary or not lineSampleValue:
                    break
                
                if(line4==lineSampleBinary):
                    lineSampleValue = lineSampleValue.strip()
            
                    if(lineSampleValue=='-'):
                        flagMinus=1
                        positionValue=''
                        sampleData.seek(0)
                        break
                        
                    elif(lineSampleValue==','):
                            
                        positionValue=int(positionValue)
                        if(flagMinus==1):
                            positionValue=positionValue*(-1)
                            flagMinus=0
                        
                        zahyouList.append(positionValue)
                        
                        positionValue=''
                        
                    else:  
                        positionValue += lineSampleValue 
                    
        screenSize+=12
        
    positionValue=int(positionValue)
    if(flagMinus==1):
        positionValue=positionValue*(-1)
                    
    zahyouList.append(positionValue)                   

    
    return zahyouList

if __name__ == '__main__':
    cordinate = getPosition()
    print(cordinate)
