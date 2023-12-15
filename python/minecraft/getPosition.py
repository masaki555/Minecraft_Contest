import os
import win32gui
from PIL import ImageGrab, Image
import numpy as np 

script_dir = os.path.dirname(os.path.abspath(__file__)) 
data_dir= script_dir + '/posdata/'
#画像からバイナリデータを取得       
def getBinaryData(heightCrop, widthCrop,imageCrop):
    flagWideth=0
    flagLine=0
    colorType=0
    WHITE_PIXEL="(255, 255, 255, 255)"
    BLACK_PIXEL="(0, 0, 0, 255)"
    binary=''
    line1=''
    line2=''
    positionData=""
    
    imageArray = np.empty((heightCrop, widthCrop), dtype = object)
    
    for y in range(heightCrop):
            for x in range(widthCrop):
                imageArray[y][x] = imageCrop.getpixel((x, y))
                
    
    for y in range(heightCrop):
        for x in range(widthCrop):
            
            if(flagWideth==0):
                if(str(imageArray[y][x])==WHITE_PIXEL):
                    colorType=0
                elif(str(imageArray[y][x])==BLACK_PIXEL):
                    colorType=1
                else:
                    print("Error:1")
                
                flagWideth=1
            elif(flagWideth==1):
                if(str(imageArray[y][x])==WHITE_PIXEL and colorType==0):
                    binary+=str(0)
                elif(str(imageArray[y][x])==BLACK_PIXEL and colorType==1):
                    binary+=str(1)
                else:
                    print("Error:2")
                    
                flagWideth=0
                
        if(flagLine==0):
            line1=binary
            flagLine=1
            
        elif(flagLine==1):
            line2=binary
            
            if(line1==line2):
                positionData+=str(line1)
                
            else:
                print("Error:3")
            
            flagLine=0
        
        binary=''
    return positionData
#　バイナリデータからサンプルデータを参照して対応する数値を返却
def matchValue(positionData):
    positionValue='' 
    flagMinus=0
    positionList=[]

    for binaryData in positionData:
        with open(data_dir+'imageALLColorValues.txt', 'r+', encoding='utf-8') as sampleData:           
                        
            sampleData.seek(0)
            
            while True:
                
                lineSampleBinary = sampleData.readline()
                lineSampleValue = sampleData.readline()
                
                lineSampleBinary = lineSampleBinary.strip()
  
                if not lineSampleBinary or not lineSampleValue:
                    break
                
                if(binaryData==lineSampleBinary):
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
                        
                        positionList.append(positionValue)
                        
                        positionValue=''
                        
                    else:  
                        positionValue += lineSampleValue 
            
    positionValue=int(positionValue)
    if(flagMinus==1):
        positionValue=positionValue*(-1)
        
    positionList.append(positionValue)                  
    
    return positionList
                                        

# 　座標を取得する関数    
def getPosition():
    hwnd = win32gui.GetForegroundWindow()
    left, top, right, bottom = win32gui.GetWindowRect(hwnd) 
    cordinate = (left+102, top+137, right-730, bottom-849)
    
    # スクリーンショットと文字認識
    image = ImageGrab.grab(cordinate)
    
    imageGrayScale = np.array(image.convert('L'), 'f')
    imageGrayScale = (imageGrayScale < 150) * 255
    imageGrayScale = Image.fromarray(imageGrayScale)
    imageGrayScale = imageGrayScale.convert('RGBA')
        
    widthGrayScale = imageGrayScale.size[0]
    
    screenSize=0
    positionData=[]
    
    # 画面全体を12ピクセルごとに切り取り、バイナリデータを取得                          
    while screenSize < widthGrayScale :
        imageCrop = imageGrayScale.crop((screenSize, 0, screenSize+12,14))
        
        widthCrop, heightCrop = imageCrop.size
        positionData.append(getBinaryData(heightCrop,widthCrop,imageCrop))                       
        screenSize+=12
    
    return matchValue(positionData)

if __name__ == '__main__':
    cordinate = getPosition()
    print(cordinate)
