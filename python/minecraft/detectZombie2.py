from asyncore import write
import sys
sys.path.append('.')
sys.path.append('./python/minecraft/')

from collections import deque
from typing import Collection
import win32gui
from PIL import ImageGrab
import numpy as np
import cv2
import time
from collections import deque
from minecraft import initCameraPos
import random


################################
game_name = 'Minecraft: Education Edition'
sleep_time = 0.05
################################


def getScreenImage():
    scale = 1.0
    srcnum = 0
    x0, y0, x1, y1 = initCameraPos.getWindowsRect()
    frames = deque(maxlen=3)
    # for i in range(3):
    bbox = (int(x0*scale)+10, int((y0+(y1-y0)*0.4)*scale),
            int(x1*scale)-10, int(int(y1*scale)*0.7))
    frame = cv2.cvtColor(np.asarray(ImageGrab.grab(
        bbox, all_screens=True)), cv2.COLOR_RGB2BGR)
    frame = cv2.resize(frame, dsize=None, fx=1/scale, fy=1/scale)

    tframe = frame.copy()
    ht, wt, _ = tframe.shape
    cnt = [int(wt/2), int(ht/2)]
    trg = [int(wt/3), int(ht/3)]
    
    cv2.line(tframe, (0, int(ht/2)),
             (wt, int(ht/2)), [255, 0, 0], 1)
    cv2.line(tframe, (int(wt/2), 0),
             (int(wt/2), ht), [255, 0, 0], 1)
    cv2.rectangle(tframe, (cnt[0]-int(trg[0]/2), cnt[1]-int(trg[1]/2)),
                  (cnt[0]+int(trg[0]/2), cnt[1]+int(trg[1]/2)), [255, 0, 0], 1)
    

    band = np.zeros((frame.copy().shape), dtype=np.uint8)
    tmp = np.zeros((frame.copy().shape), dtype=np.uint8)
    frame[frame[:, :, :] > [60, 60, 80]] = 0  # カーソルの削除
    frame[:, int(wt*0.8):, :] = 0  # 剣の領域をマスク
    tmp[frame[:, :, :] > [20, 25, 20]
        ] = frame[frame[:, :, :] > [20, 25, 20]]  # 芝抽出
    tmp[tmp[:, :, :] > [30, 40, 30]] = 0  # 芝抽出
    band[tmp == 0] = frame[tmp == 0]
    #cv2.imshow("tmp", band)
    band[band[:, :, :] < [20, 15, 10]] = 0
    fore = cv2.threshold(
        cv2.cvtColor(band, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY)[1]
    fore = cv2.morphologyEx(fore, cv2.MORPH_CLOSE,
                            np.ones((5, 5), np.uint8))
    fore = cv2.morphologyEx(fore, cv2.MORPH_OPEN,
                            np.ones((5, 5), np.uint8), iterations=2)

    back = cv2.threshold(
        cv2.cvtColor(band, cv2.COLOR_BGR2GRAY), 5, 255, cv2.THRESH_BINARY)[1]
    back = cv2.morphologyEx(back, cv2.MORPH_OPEN,
                            np.ones((5, 5), np.uint8), iterations=2)
    back = cv2.dilate(back, np.ones(
        (15, 15), np.uint8), iterations=2)

    #cv2.imshow("back", back)
    #cv2.imshow("fore", fore)
    #cv2.imshow("sample", band)
    # frames.append(band.copy())

    marker = np.zeros((fore.shape), dtype=np.int32)
    marker[back == 0] = 1
    marker[fore > 0] = 2
    segments = cv2.watershed(frame, marker)
    sudoColor = cv2.applyColorMap(
        np.uint8(segments*85), cv2.COLORMAP_JET)
    #cv2.imshow("maker", sudoColor)

    fore[:, :] = 0
    fore[segments == 2] = 255
    #cv2.imshow("fore", fore)

    srcnum: np.int16 = int('0000000000000000', 2)
    contours, hierarchy = cv2.findContours(
        fore, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        if h > ht/8:  # and h/w > 1.2:
            gx = int(x + w/2)
            gy = int(y + h/2)
            # cv2.rectangle(tframe, (x, y),
            #              (x + w, y + h), (255, 255, 0), 2)
            if x <= cnt[0] and cnt[0] <= x+w and y <= cnt[1] and cnt[1] <= y + h:  # 中心
                if ht*0.8 <= h:
                    # print("atack!")
                    srcnum = srcnum | (int('001', 2) << (3*0))
                elif ht*0.6 <= h:
                    # print("far")
                    srcnum = srcnum | (int('010', 2) << (3*0))
                else:
                    #print("so far")
                    srcnum = srcnum | (int('100', 2) << (3*0))
            elif gx <= cnt[0]:
                if gy <= cnt[1]:  # 左上
                    if ht*0.8 <= h:
                        # print("near")
                        srcnum = srcnum | (int('001', 2) << (3*1))
                    elif ht*0.6 <= h:
                        # print("far")
                        srcnum = srcnum | (int('010', 2) << (3*1))
                    else:
                        #print("so far")
                        srcnum = srcnum | (int('100', 2) << (3*1))
                elif cnt[1] < gy:  # 左下
                    if ht*0.8 <= h:
                        # print("near")
                        srcnum = srcnum | (int('001', 2) << (3*3))
                    elif ht*0.6 <= h:
                        # print("far")
                        srcnum = srcnum | (int('010', 2) << (3*3))
                    else:
                        #print("so far")
                        srcnum = srcnum | (int('100', 2) << (3*3))
            else:
                if gy <= cnt[1]:  # 右上
                    if ht*0.8 <= h:
                        # print("near")
                        srcnum = srcnum | (int('001', 2) << (3*2))
                    elif ht*0.6 <= h:
                        # print("far")
                        srcnum = srcnum | (int('010', 2) << (3*2))
                    else:
                        #print("so far")
                        srcnum = srcnum | (int('100', 2) << (3*2))
                elif cnt[1] < gy:  # 右下
                    if ht*0.8 <= h:
                        # print("near")
                        srcnum = srcnum | (int('001', 2) << (3*4))
                    elif ht*0.6 <= h:
                        # print("far")
                        srcnum = srcnum | (int('010', 2) << (3*4))
                    else:
                        #print("so far")
                        srcnum = srcnum | (int('100', 2) << (3*4))

    # print(srcnum)

    cv2.imshow("detect", tframe)

    #cv2.waitKey(10)

    return srcnum

def writeTxt(line):
    f = open('tmp2.txt', 'w', encoding='UTF-8')
    f.write(line)
    f.close()

if __name__ == '__main__':
    import init
    init.init()
    while True:
        # tempdetect()
        srcnum = getScreenImage()
        print(format(srcnum, '0>16b'))
        writeTxt(str(srcnum))
        if cv2.waitKey(1) == ord('q'):
            break
