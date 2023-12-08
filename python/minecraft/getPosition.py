import os
import win32gui
from PIL import ImageGrab, Image
import re
import numpy as np 
import init


script_dir = os.path.dirname(os.path.abspath(__file__)) 
data_dir= script_dir + '/posdata/'


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
    pattern = r'(-?[0-9][0-9]?)'
    pos = re.findall(pattern, pos)
    if len(pos) == 2:
        pos = add_to_next_element(pos, 1)
    if pos[1] == '-':
        pos = add_to_next_element(pos, 1)
    if len(pos[1]) == 0:
        pos = add_to_next_element(pos, 0)
    if pos[1] != y_value:
        pos = add_to_next_element(pos, 1)
        pos = add_to_next_element(pos, 0)
    while len(pos[1]) >= 2:
        pos = add_to_next_element(pos, 1)

    pos = list(map(int, pos))

    return pos


def getPosition():
    

    hwnd = win32gui.GetForegroundWindow()
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    
    cordinate = (left+102, top+137, right-730, bottom-849)

    
    # スクショと文字認識
    image = ImageGrab.grab(cordinate)
    image.save('image.png')
    
    imageGrayScale = np.array(image.convert('L'), 'f')
    imageGrayScale = (imageGrayScale < 150) * 255
    imageGrayScale = Image.fromarray(imageGrayScale)
    imageGrayScale = imageGrayScale.convert('RGBA')
    
    
    
    

    widthGrayScale = imageGrayScale.size[0]
    
    screenSize=0
    colorType=0
    flagWideth=0
    line3=''
    flagHeight=0
    zahyouList=[]
    positionValue=''
    flag=0
    flagMinus=0
    
    
    
    
    while screenSize < widthGrayScale :
        imageCrop = imageGrayScale.crop((screenSize, 0, screenSize+12,14))
        imageCrop.save("imageC.png")
        
        
        widthC, heightC = imageCrop.size
        imageArray = np.empty((heightC, widthC), dtype = object)
        
        for y in range(heightC):
            for x in range(widthC):
            # 順次、ピクセルの色の数値を代入している
                imageArray[y][x] = imageCrop.getpixel((x, y))
                
        with open(data_dir+'imageColorValues.txt', mode='w') as imageToWidethValue:
            for y in range(heightC):
                for x in range(widthC):
                    
                    if(flagWideth==0):
                        if(str(imageArray[y][x])==("(255, 255, 255, 255)")):
                            colorType=0
                        elif(str(imageArray[y][x])==("(0, 0, 0, 255)")):
                            colorType=1
                        else:
                            colorType=2
                        
                        flagWideth=1
                    elif(flagWideth==1):
                        if(str(imageArray[y][x])==("(255, 255, 255, 255)")and colorType==0):
                            imageToWidethValue.write(str(0))
                        elif(str(imageArray[y][x])==("(0, 0, 0, 255)")and colorType==1):
                            imageToWidethValue.write(str(1))
                        else:
                            imageToWidethValue.write(str(2))
                        
                        flagWideth=0
                    
                                        
                
                imageToWidethValue.write('\n')
                
                    
                
                    
                        
                        
            
            
                        
                   
        screenSize+=12
       
    
        
        with open(data_dir+'imageColorValues.txt', 'r', encoding='utf-8') as imageToWidethValue,  open(data_dir+'imageColorValues2.txt', 'w', encoding='utf-8') as imageToHeightValue:
             
                
            while True:
                if(flagHeight<7):
                    line1 = imageToWidethValue.readline()
                    line2 = imageToWidethValue.readline()
                    if not line1 or not line2:
                        break
                    
                    if(line1==line2):
                        line3+=(str(line1))
                    else:
                        line3+=str(2)
                    
                    
                    flagHeight+=1
                    
                if(flagHeight>=7):
                    line3 = line3.replace(',', '').replace('\n', '')
                    imageToHeightValue.write(str(line3))
                    imageToHeightValue.write('\n')
                    line3=''
                    flagHeight=0
        
        with open(data_dir+'imageColorValues2.txt', 'r', encoding='utf-8') as imageToHeightValue,open(data_dir+'imageALLColorValues.txt', 'r+', encoding='utf-8') as sampleData:           
            while True: 
                
                line4 = imageToHeightValue.readline()
                
                if not line4:
                    
                    
                    flag+=1
                    break
                
                
                sampleData.seek(0)
                
                while True:
                    
                    lineSampleBinary = sampleData.readline()
                    lineSampleValue = sampleData.readline()
                    
                    
                    
                    
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
                        
                        
                        
                if(flag==8):
                    positionValue=int(positionValue)
                    if(flagMinus==1):
                        positionValue=positionValue*(-1)
                        flagMinus=0
                            
                            
                    zahyouList.append(positionValue)
                   
                            
                    positionValue=''
                            

    imageGrayScale = imageGrayScale.convert('RGBA')
    imageGrayScale.save('imageG.png')
    
    return zahyouList

if __name__ == '__main__':
    init.init()
    cordinate = getPosition()
    print(cordinate)
