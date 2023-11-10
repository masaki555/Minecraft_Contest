import cv2
import time
import mylibs.camera_selector2 as camera
import argparse
import numpy as np

def color(box):
    threshold = 0
    box_hsv = cv2.cvtColor(box, cv2.COLOR_RGB2HSV)
    
    b = box.T[0].flatten().mean()
    blist = sorted(box.T[0].flatten(),reverse=True)
    for i in blist:
        if(i<100):
            threshold = i
            break
    g = box.T[1].flatten().mean()
    r = box.T[2].flatten().mean()

    h_max = box_hsv.T[0].flatten().max()
    s_max = box_hsv.T[1].flatten().max()
    v_max = box_hsv.T[2].flatten().max()
    return (h_max,s_max,v_max,b,threshold,r)

def check(params):
    #スポナー（火）がある場合
    if 177<=params[0]<=179 and params[1]==255 and params[2]==255:
        #ゾンビがいる
        if params[3]>23.6 and params[5]<24.85:
            return True
        else :
            return False
    #スポナー(火なし)がある場合
    elif params[0]==179 and params[2]<=74 and params[2]==params[4]:
        if params[3]>23.75:
            return True
        else:
            return False
    elif params[0]>=90 and params[4]>=35:
        return True
    return False

def main(args):
    cap = camera.CameraSelector(args.device, args.fps, args.size, args.box)
    fps = 30
    before = None
    
    while cap.isOpened():
        # 画像を取得
        ret, fnum, [frame, _, _] = cap.read()
        if not ret: 
            continue
        img_width, img_height = frame.shape[1], frame.shape[0]
        area = []
        area.clear()
        top = img_height//2-10
        end = img_height-140
        mid = top + (end-top)//2

        area1 = frame[top:mid,0:img_width//3]
        area.append(check(color(area1)))

        area2 = frame[top:mid,img_width//3:img_width*2//3]
        area.append(check(color(area2)))

        area3 = frame[top:mid,img_width*2//3:img_width]     
        area.append(check(color(area3))) 

        area4 = frame[mid:end,0:img_width//3]
        area.append(check(color(area4)))

        area5 = frame[mid:end,img_width//3:img_width*2//3]
        area.append(check(color(area5)))
        
        area6 = frame[mid:end,img_width*2//3:img_width]
        area.append(check(color(area6)))
        #print(color(area2))
        print(area)

        time.sleep(1/fps)
        
        frame = cv2.line(frame,(img_width//3,top),(img_width//3,img_height),(255,0,0),5)
        frame = cv2.line(frame,(img_width*2//3,top),(img_width*2//3,img_height),(255,0,0),5)
        
        frame = cv2.line(frame,(0,top),(img_width,top),(255,0,0),5)
        frame = cv2.line(frame,(0,mid),(img_width,mid),(255,0,0),5)
        frame = cv2.line(frame,(0,end),(img_width,end),(255,0,0),5)
        cv2.imshow('tracking', frame)
        #cv2.imshow('tracking', cv2.cvtColor(frame, cv2.COLOR_RGB2HSV))
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="--device \'camera_num\' or \'-1(realsense)\' \n--fps num")
    parser.add_argument('--device', default=99, type=int, help="--device \'camera_num\' or \'-1(realsense)\'" )
    parser.add_argument('--fps', type=int)
    stype = lambda ssize:list(map(int, ssize.split(',')))
    parser.add_argument('--size', type=stype, help="width,height")
    parser.add_argument('--box',default=(20,20,900,1080), type=stype, help="x,y,width,height")
    parser.add_argument('--mask', action='store_true', help="--maskを付けるとマスク対応")
    parser.add_argument('--pose', action='store_true', help="--poseを付けるとポーズ対応")
    args = parser.parse_args()
    main(args)
