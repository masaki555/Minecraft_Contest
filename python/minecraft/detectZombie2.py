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
import initCameraPos
import random


################################
game_name = 'Minecraft Education'
sleep_time = 0.05
################################


def getScreenImage():
    scale = 1.0
    srcnum = 0
    x0, y0, x1, y1 = initCameraPos.getWindowsRect()
    bbox = (x0+10, y0+100, x1-10, y1-100)

    bbox = (int(x0*scale)+10, int((y0+(y1-y0)*0.4)*scale),
            int(x1*scale)-10, int(int(y1*scale)*0.7))
    frame = cv2.cvtColor(np.asarray(ImageGrab.grab(
        bbox, all_screens=True)), cv2.COLOR_RGB2BGR)
    frame = cv2.resize(frame, dsize=None, fx=1/scale, fy=1/scale)

    tframe = frame.copy()
    ht, wt, _ = tframe.shape

    srcnum = 0

    hsv = cv2.cvtColor(tframe, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, (0, 0, 0), (40, 255, 255)) #床
    mask2 = cv2.inRange(hsv, (120, 0, 0), (180, 120, 255)) #壁
    mask3 = cv2.inRange(hsv, (90, 90, 70), (120, 180, 160)) #噴水
    mask4 = cv2.inRange(hsv, (0, 0, 80), (180, 20, 160)) #タイル
    mask5 = cv2.inRange(hsv, (90, 90, 0), (120, 180, 80)) #影
    mask = mask1 | mask2 | mask3 | mask4 | mask5
    mask = np.tile(mask[:,:,None],[1,1,3])
    tframe[mask==255] = 0

    sord = cv2.inRange(hsv, (80, 20, 0), (100, 220, 200)) #剣のマスク
    tframe[sord==255] = 0

    tframe = cv2.morphologyEx(tframe, cv2.MORPH_CLOSE,
                            np.ones((5, 5), np.uint8))
    tframe = cv2.morphologyEx(tframe, cv2.MORPH_OPEN,
                            np.ones((5, 5), np.uint8), iterations=2)

    tmp = cv2.cvtColor(tframe, cv2.COLOR_RGB2GRAY)
    contours, hierarchy = cv2.findContours(
        tmp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    srcnum: np.int16 = int('0000000000000000', 2)
    cnt = [int(wt/2), int(ht/2)]
    
    #cv2.line(tframe, (0, int(ht/2)),
    #         (wt, int(ht/2)), [255, 0, 0], 1)
    #cv2.line(tframe, (int(wt/2), 0),
    #         (int(wt/2), ht), [255, 0, 0], 1)
    #cv2.rectangle(tframe, (cnt[0]-int(trg[0]/2), cnt[1]-int(trg[1]/2)),
    #              (cnt[0]+int(trg[0]/2), cnt[1]+int(trg[1]/2)), [255, 0, 0], 1)

    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        #cv2.rectangle(tframe, (x,y), (x+w,y+h), [0,0,255], 1)
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

    #tframe = cv2.cvtColor(tframe, cv2.COLOR_RGB2GRAY)
    #cv2.imshow("tmp", tframe)

    return srcnum

def writeTxt(line):
    f = open('./python/tmp/detect_zombie2.txt', 'w', encoding='UTF-8')
    f.write(line)
    f.close()

if __name__ == '__main__':
#    import init
#    init.init()
    while True:
        # tempdetect()
        srcnum = getScreenImage()
        #print(format(srcnum, '0>16b'))
        #writeTxt(str(srcnum))
        writeTxt(str(format(srcnum, '0>15b')))
        if cv2.waitKey(1) == ord('q'):
            break
        time.sleep(sleep_time)
        
