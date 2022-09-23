import detect
from PIL import ImageGrab
import win32gui, time

# 画面内のmob情報を格納するクラス
class mob:
    def __init__(self):
        #type 0:クリーパー, 1:ゾンビ　（嘘ついてるかも）
        self.type = 0
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

    def printData(self):
        print(self.type)
        print(self.x)
        print(self.y)
        print(self.width)
        print(self.height)

    def calcDistance(self):
        # 0:近距離 1:中距離 2:遠距離
        if self.width > 0.1:
            self.distance = 0
        elif self.width > 0.05:
            self.distance = 1
        else:
            self.distance = 2

    # x,yを返さず、大体の位置を返せばいいかも？
    #def calcPosition(self):

# スクショ用関数
def captureMC(winHundle, windowSize):
    if winHundle:
        image = ImageGrab.grab(windowSize)
        image.save("capture.png")
    else:
        print("error!!")

# 結果の出力用
def outputData(num, data):
    ret = [[0 for i in range(6)] for j in range(num)]
    for i in range(num):
        ret[i][0] = data[i].type
        ret[i][1] = data[i].x
        ret[i][2] = data[i].y
        ret[i][3] = data[i].width
        ret[i][4] = data[i].height
        ret[i][5] = data[i].distance
    return num, ret

def main():
    # Minecraftを最前面に
    winHundle = win32gui.FindWindow(None, "Minecraft: Education Edition")
    win32gui.SetForegroundWindow(winHundle)
    time.sleep(1)

    # Minecraftのウィンドウサイズを取得
    windowSize = win32gui.GetWindowRect(winHundle)

    # スクショ➡検出のループ（現状10回に設定)
    for i in range(10):
        #スクショ
        captureMC(winHundle, windowSize)

        # 検出
        result = detect.run()
        mobData = []
        for i in range(len(result)):
            mobData.append(mob())
            mobData[i].setData(result=result[i])
            # mobData[i].printData()
            mobData[i].calcDistance()

        outputData(len(result), mobData)

if __name__ == '__main__':
    main()
