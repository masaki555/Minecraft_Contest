import cv2
from skimage.metrics import structural_similarity as ssim
import sys
import os
sys.path.append('.')
from python.minecraft import getScreenshot2
import time
import pydirectinput

def calculate_image_similarity(image_path1, image_path2, threshold):

    img1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        print("imread is failed, please check file path again.")
        return False

    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    similarity_index = ssim(img1, img2)

    return threshold <= similarity_index


if __name__ == "__main__":
    if getScreenshot2.take_screenshot("Minecraft Education")==0:
        # 比較したい画像のパスと閾値を渡す
        result=calculate_image_similarity("./python/minecraft/picture/esc.png", "./python/minecraft/picture/screenshot2.png", 0.8)
        print("esc:",result)
        if result == True:
            pydirectinput.keyDown('esc')
            time.sleep(0.05)
            pydirectinput.keyUp('esc')
        os.remove("./python/minecraft/picture/screenshot2.png")
