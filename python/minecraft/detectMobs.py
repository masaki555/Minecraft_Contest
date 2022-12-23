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

# 画面内のmob情報を格納するクラス
# type 0:ゾンビ 1:クリーパー
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
        self.distance = calcDistance(self.x)

    def printData(self):
        print(self.type)
        print(self.x)
        print(self.y)
        print(self.width)
        print(self.height)
         

    # 配列出力用
    # フォーマット：種類(1,2) X Y width height 距離
    # 種類以外0埋め三桁表示
    # def outputDataDetail(self):
    #     i_x = (int)(self.x * 1000)
    #     i_y = (int)(self.y * 1000)
    #     i_width = (int)(self.width * 1000)
    #     i_height = (int)(self.height * 1000)

    #     # txtに書き込む内容
    #     txt = "{x:03.0f}{y:03.0f}{w:03.0f}{h:03.0f}{dist:03d}".format(x=i_x,y=i_y,w=i_width,h=i_height,dist=self.distance)

    #     writeTxt(txt, self.type)

    # # フォーマット：種類(1,2) X軸位置 Y軸位置 距離
    # # 全て１桁
    # def outputDataAbout(self):
    #     x_pos = calcPosition(self.x)
    #     y_pos = calcPosition(self.y)

    #     # txtに書き込む内容
    #     txt = "{x:01d}{y:01d}{dist:01d}".format(x=x_pos,y=y_pos,dist=self.distance)

    #     if(self.type == 1):
    #         txtName = "t_zombie.txt"
    #     else:
    #         txtName = "t_creeper.txt"
    #     writeTxt(txt, txtName)
        

# スクショ用関数
def captureMC(winHundle, windowSize):
    # 保存先
    path = "./python/minecraft/yoloFiles/capture.png"
    
    if winHundle:
        image = ImageGrab.grab(windowSize)
        image.save(path)
    else:
        print("error: capture window")
        
    return path

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
    # 画面を大体１０等分して計算
    for i in range(10):
        if(i < posVal*10):
            position = i

    return position

def check(simplePos, pos):
    for i in range(len(simplePos)):
        simplePos[i] = "0"
    
    simplePos[calcPosition(pos)] = "1"
    
def makeSimpleTxt(simpleCreeperPos, simpleZombiePos):
    txtName = "t_simple.txt"
    line = ""
    for i in range(10):
        line = line + simpleCreeperPos[i]
    line = line + "2"
    for i in range(10):
        line = line + simpleZombiePos[i]
    
    writeTxt(line, txtName)
    
    
def init():
    initTxt()
    
    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": True,
    })

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
    
def readResult():
    result = ""
    txtPath = 'python/minecraft/yoloFiles/labels/capture.txt'
    if os.path.isfile(txtPath):
        f = open(txtPath, 'r')
        result = f.readlines()
        f.close()
    
    return result
    

# 結果の出力用
# txt初期化
def initTxt():
    # f = open('t_zombie.txt', 'w', encoding='UTF-8')
    # f.write("1")
    # f.close()
    # f = open('t_creeper.txt', 'w', encoding='UTF-8')
    # f.write("2")
    # f.close()
    f = open('t_simple.txt', 'w', encoding='UTF-8')
    f.write("1")
    f.close()
    
def resetDetection():
    path = 'python/minecraft/yoloFiles/labels/capture.txt'
    f = open(path, 'w', encoding='UTF-8')
    f.write("")
    f.close
        
# txt書き込み
def writeTxt(line, txtName):
    f = open(txtName, 'a', encoding='UTF-8')
    f.write(line)
    f.close()
    print(line)

def main():
    # 初期化
    init()
    opt = setopt()

    # Minecraftのウィンドウ取得
    winHundle = win32gui.FindWindow(None, "Minecraft: Education Edition")

    # Minecraftのウィンドウサイズを取得
    windowSize = win32gui.GetWindowRect(winHundle)

    # スクショ➡検出のループ
    while True:
        resetDetection()
        #スクショ
        path = captureMC(winHundle, windowSize)

        # 検出
        # 画像が読み込めるかチェック
        # 読み込めなければ諦める
        if Image.open(path):
            detect.run(**vars(opt))
            result = readResult()
        else:
            continue
        
        initTxt()
        mobData = []
        zombiePos = ["0"] * 10
        creeperPos = ["0"] * 10
        for j in range(len(result)):
            mobData.append(mob())
            mobData[j].setData(result=result[j])
            if(mobData[j].type == 1):
                check(creeperPos, mobData[j].x)
            else: 
                check(zombiePos, mobData[j].x)
            # 配列出力用
            # mobData[j].outputDataAbout()
            # mobData[j].outputDataDetail()
            
            # MOB情報を出力
            # mobData[j].printData()
        makeSimpleTxt(zombiePos, creeperPos)

if __name__ == '__main__':
    main()