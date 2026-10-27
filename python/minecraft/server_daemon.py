import traceback

try:
    import os

    # server_daemon.py の場所
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # ポータブル環境内に作る
    PORTABLE_TMP = os.path.join(BASE_DIR, "tmp")
    GEN_PY_DIR = os.path.join(PORTABLE_TMP, "gen_py")

    os.makedirs(GEN_PY_DIR, exist_ok=True)

    # TEMP/TMP をポータブル環境へ
    os.environ["TEMP"] = PORTABLE_TMP
    os.environ["TMP"] = PORTABLE_TMP

    import win32com

    # COMキャッシュ保存先
    win32com.__gen_path__ = GEN_PY_DIR

    import time
    import socket
    import threading
    import win32gui
    import win32con
    import win32com.client
    import pythoncom
    import pydirectinput

except Exception:
    traceback.print_exc()

    with open("daemon_error.log", "w", encoding="utf-8") as f:
        traceback.print_exc(file=f)

    input("ERROR>")
    raise

SLEEP_TIME = 0.05
pydirectinput.FAILSAFE = False



# --------------------------------------------------
# 1. ウィンドウ検索関数（部分一致）
# --------------------------------------------------
def find_minecraft_hwnd(search_name="Minecraft Education"):
    found_hwnd = []
    
    def enum_windows_callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if search_name.lower() in title.lower():
                found_hwnd.append((hwnd, title))

    win32gui.EnumWindows(enum_windows_callback, None)
    return found_hwnd[0] if found_hwnd else (None, None)

# --------------------------------------------------
# 2. ウィンドウアクティブ化・画面初期化関数
# --------------------------------------------------
def setup_minecraft_window():
    # サブスレッドで win32com を使用するための COM 初期化
    pythoncom.CoInitialize()
    
    try:
        print("[init] ウィンドウ検索中...")
        hwnd, title = find_minecraft_hwnd("Minecraft Education")
        
        if not hwnd:
            print("[エラー] 'Minecraft' を含むウィンドウが見つかりませんでした。")
            return

        print(f"[成功] 対象ウィンドウを発見しました: '{title}' (HWND: {hwnd})")

        # 最小化解除
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        time.sleep(SLEEP_TIME)

        # ALTキー送信でフォーカス制限解除 ＆ 前面化
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        time.sleep(SLEEP_TIME)

        win32gui.SetForegroundWindow(hwnd)
        time.sleep(SLEEP_TIME)

        # ウィンドウ移動 & リサイズ
        win32gui.MoveWindow(hwnd, 0, -10, 940, 1000, True)
        time.sleep(SLEEP_TIME)

        # ポーズ画面解除 (Esc押下)
        pydirectinput.press('esc')
        time.sleep(0.2)

        # マウスカーソル中央移動
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        init_x = int((left + right) / 2)
        init_y = int((top + bottom) / 2)
        pydirectinput.moveTo(init_x, init_y)
        time.sleep(SLEEP_TIME)

        print("[完了] ウィンドウのアクティブ化と初期位置設定が完了しました。")

    except Exception as e:
        print(f"[エラー] ウィンドウアクティブ化失敗: {e}")
    finally:
        # COM 解放
        pythoncom.CoUninitialize()

# --------------------------------------------------
# 3. 操作受信用スレッド (Port 8888)
# --------------------------------------------------
def control_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 8888))
    print("[Control Daemon] Port 8888 でコマンド受付中...")

    while True:
        data, _ = sock.recvfrom(1024)
        msg = data.decode("utf-8").strip()
        print(f"[受信] {msg}")
        
        parts = msg.split(":")
        cmd = parts[0]

        if cmd == "init":
            setup_minecraft_window()
        elif cmd == "downKey" and len(parts) > 1:
            pydirectinput.keyDown(parts[1])
        elif cmd == "upKey" and len(parts) > 1:
            pydirectinput.keyUp(parts[1])
        elif cmd == "pushKey" and len(parts) > 1:
            pydirectinput.press(parts[1])

# --------------------------------------------------
# 4. 問い合わせ受信用スレッド (Port 8889)
# --------------------------------------------------
def query_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 8889))
    print("[Query Daemon] Port 8889 で問い合わせ受付中...")

    while True:
        data, addr = sock.recvfrom(1024)
        req = data.decode("utf-8").strip()
        
        res = "0"
        sock.sendto(res.encode("utf-8"), addr)

if __name__ == "__main__":
    t1 = threading.Thread(target=control_listener, daemon=True)
    t2 = threading.Thread(target=query_listener, daemon=True)
    t1.start()
    t2.start()

    print("Minecraft Server Daemon Ready.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Daemon Stopping...")