import sys
sys.path.append('.')
sys.path.append('./python/')

from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]

from PIL import ImageGrab, Image
import win32gui, time, os, logging, argparse

sys.path.append('.')
sys.path.append('./python/yolov5-master')
import detect

path_detectZombie3 = "python/tmp/detect_zombie3.txt"
path_detectMobs = "python/tmp/detect_mobs.txt"
path_creepertxt = "python/tmp/t_creeper.txt"
path_zombietxt = "python/tmp/t_zombie.txt"
path_captureImg = "python/minecraft/yoloFiles/capture.png"
path_captureTxt = "python/minecraft/yoloFiles/labels/capture.txt"

# 画像の分割数
splitNum = 6

# mobの辞書
mobsDict = {"creeper":0, "zombie":1}

# 扱うmobの種類
mobNum = len(mobsDict)

# 画面内のmob情報を格納するクラス
class mob:
    def __init__(self):
        self.type = 1
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.distance = 0

    def setData(self, result):
        data = result.split()
        self.type = int(data[0])
        self.x = float(data[1])
        self.y = float(data[2])
        self.width = float(data[3])
        self.height = float(data[4])
        self.distance = calcDistance(self.width)

    def printData(self):
        print(self.type)
        print(self.x)
        print(self.y)
        print(self.width)
        print(self.height)
        
    # フォーマット：種類(1,2) X軸位置 Y軸位置 距離
    # 全て１桁
    def outputDataAbout(self):
        path = path_zombietxt
        x_pos = calcPosition(self.x)
        y_pos = calcPosition(self.y)

        # txtに書き込む内容
        txt = "{x:01d}{y:01d}{dist:01d}".format(x=x_pos,y=y_pos,dist=self.distance)

        if(self.type == mobsDict["zombie"]):
            path = path_zombietxt
        elif(self.type == mobsDict["creeper"]):
            path = path_creepertxt
        makeTxt(txt, path)

# スクショ用関数
def captureMC(winHundle, windowSize):
    if winHundle:
        image = ImageGrab.grab(windowSize)
        image.save(path_captureImg)
    else:
        print("error: capture window")

# 大体の距離を計算
def calcDistance(width):
    # 0:近距離 1:中距離 2:遠距離
    if width > 0.1:
        distance = 0
    elif width > 0.05:
        distance = 1
    else:
        distance = 2 
    
    return distance

# 大体の位置計算
def calcPosition(posVal):
    # 画面をsplitNum等分して計算
    border = 1.0 / splitNum
    for i in range(splitNum):
        if(border * i < posVal):
            position = i

    return position

def readResult():
    result = ""
    if os.path.isfile(path_captureTxt):
        f = open(path_captureTxt, 'r')
        result = f.readlines()
        f.close()

    return result

# txt系
# txt初期化
def initTxt(fileName):
    f = open(fileName, 'w', encoding='UTF-8')
    f.write("")
    f.close()
    
def resetDetection():
    initTxt(path_captureTxt)

def resetAllTxt():
    files = [path_detectZombie3, path_detectMobs, path_creepertxt, path_zombietxt]
    for f in files:
        initTxt(f)

def makeLine(pos, txtPath):
    line = ""
    for i in range(len(pos)):
        line = line + pos[i]
        
    makeTxt(line, txtPath)

def makeTxt(line, txtPath):
    f = open(txtPath, 'a', encoding='UTF-8')
    f.write(line)
    f.close()

def setopt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default=ROOT / 'yoloFiles/best.pt', help='model path or triton URL')
    parser.add_argument('--source', type=str, default=ROOT / 'yoloFiles/capture.png')
    parser.add_argument('--save-txt', action='store_true', default=True)
    parser.add_argument('--data', type=str, default=ROOT / 'yoloFiles/mobs.yaml', help='(optional) dataset.yaml path')
    parser.add_argument('--nosave', action='store_true', default=True)
    parser.add_argument('--exist-ok', action='store_true', default=True)
    parser.add_argument('--project', default=ROOT / 'yoloFiles', help='save results to project/name')
    parser.add_argument('--name', default='', help='save results to project/name')

    opt = parser.parse_args()
    return opt

def init():
    resetAllTxt()
    resetDetection()

    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": True,
    })

def main():
    game_name = 'Minecraft Education'

    # 初期化
    init()
    opt = setopt()

    # Minecraftのウィンドウ取得
    winHundle = win32gui.FindWindow(None, game_name)

    # Minecraftのウィンドウサイズを取得
    windowSize = win32gui.GetWindowRect(winHundle)

    # スクショ➡検出のループ
    while True:
        resetDetection()
        #スクショ
        captureMC(winHundle, windowSize)

        # 検出
        # 画像が読み込めるかチェック
        # 読み込めなければ諦める
        if Image.open(path_captureImg):
            detect.run(**vars(opt))
            result = readResult()
        else:
            continue

        resetAllTxt()
        mobData = []
        zombiePos = ["0"] * splitNum
        mobsPos = ["0"] * splitNum
        for j in range(len(result)):
            mobData.append(mob())
            mobData[j].setData(result=result[j])
            p = calcPosition(mobData[j].x)

            # type: ゾンビなら
            if(mobData[j].type == mobsDict["zombie"]):
                zombiePos[p] = "1"

            mobsPos[p] = str(mobData[j].type + 1)
            
            # 配列出力
            mobData[j].outputDataAbout()

            # Mob情報を出力
            # mobData[j].printData()
        makeLine(zombiePos, path_detectZombie3)
        makeLine(mobsPos, path_detectMobs)

if __name__ == '__main__':
    main()
