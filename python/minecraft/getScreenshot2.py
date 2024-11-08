import pyautogui
import pygetwindow as gw
import time

def take_screenshot(app_title):
    try:
        # 指定したアプリのウィンドウを取得
        window = gw.getWindowsWithTitle(app_title)[0]
        
        # ウィンドウがアクティブでない場合、アクティブにする
        if not window.isActive:
            window.activate()
            time.sleep(1)  # アクティブになるのを待つ

        # ウィンドウの位置とサイズを取得
        x, y, width, height = window.left, window.top, window.width, window.height
        
        # スクリーンショットを取得
        screenshot = pyautogui.screenshot(region=(x+70, y+88, 345, 68)) #微調整する
        
        # スクリーンショットを保存
        screenshot.save("./python/minecraft/picture/screenshot2.png")
        return 0

    except IndexError:
        print(f"アプリケーション '{app_title}' が見つかりませんでした。")
        return -1
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return -1

if __name__ == "__main__":
    take_screenshot("Minecraft Education")  # アプリケーションのタイトルを指定