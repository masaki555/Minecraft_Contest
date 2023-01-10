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
path_captureImg = "python/minecraft/yoloFiles/capture.png"
path_captureTxt = "python/minecraft/yoloFiles/labels/capture.txt"

# 画像の分割数
splitNum = 6

# 画面内のmob情報を格納するクラス
# type 0:ゾンビ 1:クリーパー
class mob:
    def __init__(self):
        self.type = 1
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def setData(self, result):
        data = result.split()
        self.type = int(data[0])
        self.x = float(data[1])
        self.y = float(data[2])
        self.width = float(data[3])
        self.height = float(data[4])

    def printData(self):
        print(self.type)
        print(self.x)
        print(self.y)
        print(self.width)
        print(self.height)

# スクショ用関数
def captureMC(winHundle, windowSize):
    if winHundle:
        image = ImageGrab.grab(windowSize)
        image.save(path_captureImg)
    else:
        print("error: capture window")

# 大体の位置計算
def calcPosition(posVal):
    # 画面をsplitNum等分して計算
    border = 1.0 / splitNum
    for i in range(splitNum):
        if(border * i < posVal):
            position = i

    return position

def init():
    initTxt()
    resetDetection()

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
    if os.path.isfile(path_captureTxt):
        f = open(path_captureTxt, 'r')
        result = f.readlines()
        f.close()

    return result

# 結果の出力用
# txt初期化
def initTxt():
    f = open(path_detectZombie3, 'w', encoding='UTF-8')
    f.write("")
    f.close()
    f = open(path_detectMobs, 'w', encoding='UTF-8')
    f.write("")
    f.close()

def resetDetection():
    f = open(path_captureTxt, 'w', encoding='UTF-8')
    f.write("")
    f.close

def makeTxt(pos, txtPath):
    line = ""
    for i in range(splitNum):
        line = line + pos[i]

    f = open(txtPath, 'a', encoding='UTF-8')
    f.write(line)
    f.close()

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
        captureMC(winHundle, windowSize)

        # 検出
        # 画像が読み込めるかチェック
        # 読み込めなければ諦める
        if Image.open(path_captureImg):
            detect.run(**vars(opt))
            result = readResult()
        else:
            continue

        initTxt()
        mobData = []
        zombiePos = ["0"] * splitNum
        mobsPos = ["0"] * splitNum
        for j in range(len(result)):
            mobData.append(mob())
            mobData[j].setData(result=result[j])

            # type: ゾンビなら
            if(mobData[j].type == 1):
                p = calcPosition(mobData[j].x)
                zombiePos[p] = "1"

            p = calcPosition(mobData[j].x)
            mobsPos[p] = str(mobData[j].type + 1)

            # Mob情報を出力
            # mobData[j].printData()
        makeTxt(zombiePos, path_detectZombie3)
        makeTxt(mobsPos, path_detectMobs)

if __name__ == '__main__':
    main()
