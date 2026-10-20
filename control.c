#include "control.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <windows.h>
#include <pthread.h>

// --------------------------------------------------
// グローバル変数 (control.h に対応)
// --------------------------------------------------
int rk = 1;

// --------------------------------------------------
// 内部ヘルパー関数 (UDP通信用)
// --------------------------------------------------
static void send_udp(const char *msg) {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) return;

    SOCKET sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock != INVALID_SOCKET) {
        struct sockaddr_in addr;
        addr.sin_family = AF_INET;
        addr.sin_port = htons(8888); // 操作コマンド用ポート
        addr.sin_addr.s_addr = inet_addr("127.0.0.1");

        sendto(sock, msg, (int)strlen(msg), 0, (struct sockaddr *)&addr, sizeof(addr));
        closesocket(sock);
    }
    WSACleanup();
}

static int query_udp_int(const char *req) {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) return 0;

    SOCKET sock = socket(AF_INET, SOCK_DGRAM, 0);
    int result = 0;

    if (sock != INVALID_SOCKET) {
        struct sockaddr_in addr;
        addr.sin_family = AF_INET;
        addr.sin_port = htons(8889); // 認識結果問い合わせ用ポート
        addr.sin_addr.s_addr = inet_addr("127.0.0.1");

        // 1秒の受信タイムアウト設定
        DWORD timeout = 1000;
        setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, (const char*)&timeout, sizeof(timeout));

        sendto(sock, req, (int)strlen(req), 0, (struct sockaddr *)&addr, sizeof(addr));

        char buf[32] = {0};
        int addr_len = sizeof(addr);
        if (recvfrom(sock, buf, sizeof(buf) - 1, 0, (struct sockaddr *)&addr, &addr_len) > 0) {
            result = atoi(buf);
        }
        closesocket(sock);
    }
    WSACleanup();
    return result;
}

// F12キーによる緊急停止監視スレッド
static void *isInterrupt(void *args) {
    while (rk) {
        if (GetKeyState(VK_F12) < 0) {
            fprintf(stderr, "F12検知: 終了コード送信\n");
            rk = 0;
        }
        Sleep(100);
    }
    return args;
}

// --------------------------------------------------
// control.h 宣言関数の全実装
// --------------------------------------------------

// --------------------------------------------------
// control2.c の init() 実装（MSYS2 ポータブル環境用）
// --------------------------------------------------
void init(void) {
    STARTUPINFOA si;
    PROCESS_INFORMATION pi;
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));

    // MSYS2のパス変換を回避し、相対パスでPythonデーモンを直接起動
    // CREATE_NO_WINDOW により黒いコンソール画面を出さずにバックグラウンド実行
    char cmd[] = "python .\\python\\minecraft\\server_daemon.py";

    if (CreateProcessA(NULL, cmd, NULL, NULL, FALSE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi)) {
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
    } else {
        // 'python' コマンドで起動できない場合は 'py' ランチャーで試行
        char cmd_py[] = "py .\\python\\minecraft\\server_daemon.py";
        if (CreateProcessA(NULL, cmd_py, NULL, NULL, FALSE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi)) {
            CloseHandle(pi.hProcess);
            CloseHandle(pi.hThread);
        }
    }

    // Python デーモンの UDP ソケット受信用スレッド立ち上がりを待機 (1.5秒)
    Sleep(1000);

    // マイクラウィンドウのアクティブ化・画面初期化要求を送信
    send_udp("init");
}

void exePython(void) {
    pthread_t key;
    if (pthread_create(&key, NULL, &isInterrupt, NULL) != 0) {
        fprintf(stderr, "終了監視スレッド作成失敗\n");
        exit(1);
    }
}

// --- 認識系関数 ---
int detectPlayer1(void) { return query_udp_int("detectPlayer1"); }
int detectPlayer2(void) { return query_udp_int("detectPlayer2"); }
int detectZombie1(void) { return query_udp_int("detectZombie1"); }
long detectZombie2(void) { return (long)query_udp_int("detectZombie2"); }

// --- 攻撃・操作系関数 ---
void attackLeft(void) { send_udp("attackLeft"); }
void attackLeft_long(void) { send_udp("attackLeft_long"); }

void attackLeft_continuous(int n) {
    char buf[64];
    snprintf(buf, sizeof(buf), "attackLeft_continuous:%d", n);
    send_udp(buf);
}

void eat(int n) {
    char buf[64];
    snprintf(buf, sizeof(buf), "eat:%d", n);
    send_udp(buf);
}

void downKey(char* key) {
    char buf[64];
    snprintf(buf, sizeof(buf), "downKey:%s", key);
    send_udp(buf);
}

void upKey(char* key) {
    char buf[64];
    snprintf(buf, sizeof(buf), "upKey:%s", key);
    send_udp(buf);
}

void pushKey(char* key) {
    char buf[64];
    snprintf(buf, sizeof(buf), "pushKey:%s", key);
    send_udp(buf);
}

void sleep_time(double time) {
    if (time < 0) time = -time;
    Sleep((DWORD)(time * 1000));
}

// --- 移動系関数 ---
void moveForward(double time) { char buf[64]; snprintf(buf, sizeof(buf), "moveForward:%f", time); send_udp(buf); sleep_time(time); }
void moveLeft(double time) { char buf[64]; snprintf(buf, sizeof(buf), "moveLeft:%f", time); send_udp(buf); sleep_time(time); }
void moveRight(double time) { char buf[64]; snprintf(buf, sizeof(buf), "moveRight:%f", time); send_udp(buf); sleep_time(time); }
void moveBack(double time) { char buf[64]; snprintf(buf, sizeof(buf), "moveBack:%f", time); send_udp(buf); sleep_time(time); }
void moveForwardLeft(double time) { char buf[64]; snprintf(buf, sizeof(buf), "moveForwardLeft:%f", time); send_udp(buf); sleep_time(time); }
void moveForwardRight(double time) { char buf[64]; snprintf(buf, sizeof(buf), "moveForwardRight:%f", time); send_udp(buf); sleep_time(time); }
void moveBackLeft(double time) { char buf[64]; snprintf(buf, sizeof(buf), "moveBackLeft:%f", time); send_udp(buf); sleep_time(time); }
void moveBackRight(double time) { char buf[64]; snprintf(buf, sizeof(buf), "moveBackRight:%f", time); send_udp(buf); sleep_time(time); }
void moveJump(int times) { char buf[64]; snprintf(buf, sizeof(buf), "moveJump:%d", times); send_udp(buf); }
void moveDash(int times) { char buf[64]; snprintf(buf, sizeof(buf), "moveDash:%d", times); send_udp(buf); }
void setDash(void) { send_udp("setDash"); }
void resetDash(void) { send_udp("resetDash"); }

// --- カメラ系関数 ---
void cameraDown(double time) { char buf[64]; snprintf(buf, sizeof(buf), "cameraDown:%f", time); send_udp(buf); sleep_time(time); }
void cameraLeft(double time) { char buf[64]; snprintf(buf, sizeof(buf), "cameraLeft:%f", time); send_udp(buf); sleep_time(time); }
void cameraRight(double time) { char buf[64]; snprintf(buf, sizeof(buf), "cameraRight:%f", time); send_udp(buf); sleep_time(time); }
void cameraUp(double time) { char buf[64]; snprintf(buf, sizeof(buf), "cameraUp:%f", time); send_udp(buf); sleep_time(time); }

// --- 環境・ゲームモード設定系関数 ---
void setTime(void) { send_udp("setTime"); }
void setMorning(void) { send_udp("setMorning"); }
void setSurvival(void) { send_udp("setSurvival"); }
void setCreative(void) { send_udp("setCreative"); }
