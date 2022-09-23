import sys
sys.path.append('.')
sys.path.append('./python/minecraft/')

import cv2
import mylibs.camera_selector2 as camera
import argparse
import numpy as np

N = 5
#HSV,RGB値の算出
def wrightTxt(line):
    f = open('tmp.txt', 'w', encoding='UTF-8')
    f.write(line)
    f.close()

def color(box):
    threshold = 0
    box_hsv = cv2.cvtColor(box, cv2.COLOR_RGB2HSV)
    blist = sorted(box.T[0].flatten(),reverse=True)
    for i in blist:
        if(i<100):
            threshold = i
            break
    h_max = box_hsv.T[0].flatten().max()
    s_max = box_hsv.T[1].flatten().max()
    v_max = box_hsv.T[2].flatten().max()
    return (h_max,s_max,v_max,threshold)

def punch_check(frame):
    img_width, img_height = frame.shape[1], frame.shape[0]
    low = (0,176,39)
    high = (9,277,60)
    flag = False
    cnt = 0
    # HSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2値化
    zebra = cv2.inRange(hsv, low, high)
    zebra = cv2.bitwise_not(zebra)
    # 輪郭の検出
    cons = cv2.findContours(zebra, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[0]

    # 輪郭の描画
    for con in cons:
        # 面積が閾値を超えない場合，輪郭としない
        if cv2.contourArea(con) < 100:
            continue
        # 描画処理
        cv2.polylines(frame, con, True, (0,255,0),5)
        points = con.squeeze(axis=1)
        for point in points:
            if 30<=point[0]<=img_width-20 and 300<=point[1]<=img_height-140:
                cnt += 1
    if cnt >=30:
        flag = True
    return flag

#ゾンビの検出
def check(counts,params):
    flag = []
    for i in range(len(counts)):
        if i==5:
            if counts[i] >= N:
                flag.append(True)
            else :
                flag.append(False)
        #スポナー（火）がある場合
        elif 177<=params[i][0]<=179 and params[i][1]==255 and params[i][2]==255:
            #ゾンビがいる
            if counts[i] >= N:
                flag.append(True)
            else :
                flag.append(False)
        #スポナー(火なし)がある場合
        elif params[i][0]==179 and params[i][2]<=74 and params[i][2]==params[i][3]:
            if counts[i] >= N:
                flag.append(True)
            else :
                flag.append(False)
        elif (params[i][0]>=90 and params[i][3]>=35) or counts[i]>=N:
            flag.append(True)
        else:
            flag.append(False)
    return flag

def gamma_correction(img, gamma):
    table = (np.arange(256) / 255) ** gamma * 255
    table = np.clip(table, 0, 255).astype(np.uint8)
    return cv2.LUT(img, table)


def levelingBrightness(img, target, gamma):
    x = int(img.shape[1]/2)
    y = int(img.shape[0]/2)
    brightness = np.sum(img)/(255*x*y)
    if brightness < target:
        gamma -= 0.03*abs(brightness - target)
    else:
        gamma += 0.03*abs(brightness - target)
    return gamma

def extractionZombie(img, gamma):
    g = 167*gamma
    gLow = np.clip(g-30, 64, 29).astype(np.uint8)
    gUp = np.clip(g+60, 255, 255).astype(np.uint8)
    lower = np.array([gLow, gLow, 0])
    upper = np.array([gUp, gUp, 0])
    img = cv2.inRange(img, lower, upper)
    return img

#True，FalseはC言語では使いにくいので0,1の文字列に変換
def printByte(array):
    data = ""
    for i in array:
        if(i == True):
            data += '1'
        else:
            data += '0'
    return data

def trackZombie(cap):
    gamma = 1.0
    
    # l(40,80,15),h(110,255,255) time set 18000で草と空とゾンビの区別成功
    # 村人ゾンビの識別は不安定

    ret, fnum, [frame, _, _] = cap.read()
    if not ret:
        #continue
        return
    img_width, img_height = frame.shape[1], frame.shape[0]
    area = []
    params = []
    counts = [0] * 6
    area.clear()
    top = img_height//2-10
    end = img_height-140
    mid = top + (end-top)//2

    #HSV値によるゾンビの検出
    area1 = frame[top:mid, 0:img_width//3]
    params.append(color(area1))

    area2 = frame[top:mid, img_width//3:img_width*2//3]
    params.append(color(area2))

    area3 = frame[top:mid, img_width*2//3:img_width]
    params.append(color(area3))

    area4 = frame[mid:end, 0:img_width//3]
    params.append(color(area4))

    area5 = frame[mid:end, img_width//3:img_width*2//3]
    params.append(color(area5))

    area6 = frame[mid:end, img_width*2//3:img_width]
    params.append(color(area6))

    #輪郭抽出によるゾンビの検出
    #ガンマ値の設定
    dst = gamma_correction(frame, gamma)
    gamma = levelingBrightness(dst, 3, gamma)
    mask = extractionZombie(dst, gamma)
    # 輪郭の検出
    cons = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[0]

    # 輪郭の描画
    for con in cons:
        # 面積が閾値を超えない場合，輪郭としない
        if cv2.contourArea(con) < 800:
            continue
        # 描画処理
        cv2.polylines(frame, con, True, (255, 0, 0),5)
        points = con.squeeze(axis=1)
        for point in points:
            if 10 <= point[0]<=img_width//3 and top<=point[1]<=mid:
                counts[0] += 1
            elif img_width//3 <= point[0] <=img_width*2//3 and top<=point[1]<=mid:
                counts[1] += 1
            elif img_width*2//3 <= point[0] <=img_width-10 and top<=point[1]<=mid:
                counts[2] += 1
            elif 10 <= point[0]<=img_width//3 and mid<=point[1]<=end:
                counts[3] += 1
            elif img_width//3 <= point[0] <=img_width*2//3 and mid<=point[1]<=end:
                counts[4] += 1
            elif img_width*2//3 <= point[0] <=img_width-10 and mid<=point[1]<=end:
                counts[5] += 1

    area = check(counts, params)
    #自身の攻撃検出
    area.append(punch_check(frame))
    #print(area)
    wrightTxt(printByte(area))

def main():
    #cap = camera.CameraSelector(args.device, args.fps, args.size, args.box)
    box = [20, 20, 900 , 1000] 
    cap = camera.CameraSelector(99, None, None, box)
    # 映像の読込
    cap.isOpened()
#    trackZombie(cap)
    wrightTxt("0000000")

    while cap.isOpened():
        ret, fnum, [frame, _, _] = cap.read()
        img_width, img_height = frame.shape[1], frame.shape[0]
        top = img_height//2-10
        end = img_height-140
        mid = top + (end-top)//2
        trackZombie(cap)
#        frame = cv2.line(frame, (img_width//3, top),(img_width//3,img_height),(0,0,255),5)
#        frame = cv2.line(frame, (img_width*2//3, top),(img_width*2//3,img_height),(0,0,255),5)
#        frame = cv2.line(frame, (0, top),(img_width,top),(0,0,255),5)
#        frame = cv2.line(frame, (0, mid),(img_width,mid),(0,0,255),5)
#        frame = cv2.line(frame, (0, end),(img_width,end),(0,0,255),5)
#        cv2.imshow('tracking', frame)
#        if cv2.waitKey(1) & 0xFF == 27:
#            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
#    parser = argparse.ArgumentParser(description="--device \'camera_num\' or \'-1(realsense)\' \n--fps num")
#    parser.add_argument('--device', default=99, type=int, help="--device \'camera_num\' or \'-1(realsense)\'" )
#    parser.add_argument('--fps', type=int)
#    stype = lambda ssize:list(map(int, ssize.split(',')))
#    parser.add_argument('--size', type=stype, help="width,height")
#    parser.add_argument('--box',default=(20,20,900,1080), type=stype, help="x,y,width,height")
#    parser.add_argument('--mask', action='store_true', help="--maskを付けるとマスク対応")
#    parser.add_argument('--pose', action='store_true', help="--poseを付けるとポーズ対応")
#    args = parser.parse_args()
#    main(args)
    main()
