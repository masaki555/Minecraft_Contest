#include "control.h"

#include <err.h>
#include <fcntl.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <termios.h>
#include <unistd.h>
#include <windows.h>

#define PRINT_HERE fprintf(stderr, "File:%s Line:%d\t", __FILE__, __LINE__)

pid_t Detect_pid;
pid_t Move_pid;
pid_t Camera_pid;
int rk = 1;

// キーを1つ遅延なしで入力する関数
void sendChar(WORD vkKey) {
    INPUT input = {0};

    // キー押下
    input.type = INPUT_KEYBOARD;
    input.ki.wVk = vkKey;
    SendInput(1, &input, sizeof(INPUT));

    // キーリリース
    input.ki.dwFlags = KEYEVENTF_KEYUP;
    SendInput(1, &input, sizeof(INPUT));
}

// 文字列を入力する
void sendCommand(const char *str) {
    // コマンド入力欄を開く
    sendChar(VK_RETURN);

    for (size_t i = 0; i < strlen(str); i++) {
        char ch = str[i];

        // 大文字と小文字の処理
        int shiftRequired = 0;
        WORD vkKey = 0;

        if (ch >= 'A' && ch <= 'Z') {
            vkKey = ch;  // 大文字 (そのまま)
            shiftRequired = 1;
        } else if (ch >= 'a' && ch <= 'z') {
            vkKey = ch - 32;  // 小文字 (大文字に変換)
            shiftRequired = 0;
        } else if (ch >= '0' && ch <= '9') {
            vkKey = ch;  // 数字 (そのまま)
        } else {
            // 特殊文字の処理 (ここではスペースだけ対応)
            if (ch == ' ') {
                vkKey = VK_SPACE;
            } else if (ch == '/') {
                vkKey = VK_OEM_2;  // スラッシュ
            } else {
                printf("未対応の文字: %c\n", ch);
                continue;  // 未対応の文字はスキップ
            }
        }

        // Shiftキーの押下が必要な場合
        if (shiftRequired) {
            INPUT shiftDown = {0};
            shiftDown.type = INPUT_KEYBOARD;
            shiftDown.ki.wVk = VK_SHIFT;
            SendInput(1, &shiftDown, sizeof(INPUT));
        }

        // キーを送信
        sendChar(vkKey);

        // Shiftキーをリリース
        if (shiftRequired) {
            INPUT shiftUp = {0};
            shiftUp.type = INPUT_KEYBOARD;
            shiftUp.ki.wVk = VK_SHIFT;
            shiftUp.ki.dwFlags = KEYEVENTF_KEYUP;
            SendInput(1, &shiftUp, sizeof(INPUT));
        }
    }

    // コマンドを実行して閉じる
    sendChar(VK_RETURN);
    sendChar(VK_ESCAPE);
}

void equipment(void) {
    sendChar(VK_SPACE);
    Sleep(1000);
    sendChar('2');
    sendChar('E');
    sendChar('3');
    sendChar('E');
    sendChar('1');
}

void attackLeft(void) { sendChar('Q'); }

void attackLeft_continuous(int n) {
    char com[128] =
        "python/python.exe python/minecraft/clickLeft_Continuous.py ";
    char buf[12];
    snprintf(buf, 12, "%d", n);
    strcat(com, buf);
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:attackLeft_continuous\n");
        exit(1);
    }
}

void eat(int n) {
    char com[128] = "python/python.exe python/minecraft/eat.py ";
    char buf[12];
    snprintf(buf, 12, "%d", n);
    strcat(com, buf);
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:eat\n");
        exit(1);
    }
}

void center(void) {
    char com[128] = "python/python.exe python/minecraft/center.py";
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:center\n");
        exit(1);
    }
}

void upKey(char *key) {
    char com[128] = "python/python.exe python/minecraft/upKey.py ";
    strcat(com, key);
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:upKey\n");
        exit(1);
    }
}

void downKey(char *key) {
    char com[128] = "python/python.exe python/minecraft/downKey.py ";
    strcat(com, key);
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:downKey\n");
        exit(1);
    }
}

void moveDataToFile(char *key) {
    FILE *fp;
    char pass[64] = "python/tmp/Share_Move_Data.txt";
    char buf[32] = "";
    const char *const sep = ",";
    char *data;

    // Share_Move_Data.txtの内容をbufに保存する

    if ((fp = fopen(pass, "r")) == NULL) {
        printf(
            "error：moveDataToFile\nShare_Move_Data."
            "txtをrモードで開けませんでした．\n");
        exit(1);
    } else {
        fgets(buf, 31, fp);
    }
    fclose(fp);

    // bufの内容に変更を加えてShare_Move_Data.txtを上書きする

    if ((fp = fopen(pass, "w")) == NULL) {
        printf("error：Share_Move_Data.txtをwモードで開けませんでした．\n");
        exit(1);
    } else {
        data = strtok(buf, sep);
        data = strtok(NULL, sep);
        if (data != NULL) {
            fprintf(fp, "%s,%s", key, data);
        } else {
            fprintf(fp, "%s,%s", key, "0");
            // printf("error:moveDataToFile\n");
        }
    }
    fclose(fp);
}

void cameraDataToFile(char *key, double sleep_time) {
    FILE *fp;
    char pass[64] = "python/tmp/Share_Camera_Data.txt";
    char buf[32] = "";
    // char *data;

    if ((fp = fopen(pass, "r")) == NULL) {
        printf("error：Share_Camera_Data.txtをrモードで開けませんでした．\n");
        exit(1);
    } else {
        fgets(buf, 31, fp);
    }
    fclose(fp);

    if ((fp = fopen(pass, "w")) == NULL) {
        printf("error：Share_Camera_Data.txtをwモードで開けませんでした．\n");
        exit(1);
    } else {
        fprintf(fp, "%s,%f", key, (float)sleep_time);
    }
    fclose(fp);
}

void initMoveDataFile(void) { moveDataToFile("Wait"); }

void moveForward(double sleep_time) {
    char key[32] = "F";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    // usleep(0.15*1000000);
}

void moveLeft(double sleep_time) {
    char key[32] = "L";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    // usleep(0.15*1000000);
}

void moveRight(double sleep_time) {
    char key[32] = "R";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    // usleep(0.15*1000000);
}

void moveBack(double sleep_time) {
    char key[32] = "B";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    // usleep(0.15*1000000);
}

void moveForwardLeft(double sleep_time) {
    char key[32] = "FL";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    // usleep(0.37*1000000);
}

void moveForwardRight(double sleep_time) {
    char key[32] = "FR";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    // usleep(0.37*1000000);
}

void moveBackLeft(double sleep_time) {
    char key[32] = "BL";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    // usleep(0.37*1000000);
}

void moveBackRight(double sleep_time) {
    char key[32] = "BR";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    // usleep(0.37*1000000);
}

void moveJump(int times) {
    char str[128] = "python/python.exe python/minecraft/moveCharacterJump.py";
    char com[256];
    sprintf(com, "%s %d", str, times);
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:moveJump\n");
        exit(1);
    }
}

void moveDash(int times) {
    char str[128] =
        "python/python.exe python/minecraft/moveCharacterJumpDash.py";
    char com[256];
    sprintf(com, "%s %d", str, times);
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:moveJump\n");
        exit(1);
    }
}

void setDashFlag(int flag) {
    FILE *fp;
    char pass[64] = "python/tmp/Share_Move_Data.txt";
    char buf[32] = "";
    const char *const sep = ",";
    char *data;

    // Share_Move_Data.txtの内容をbufに保存する

    if ((fp = fopen(pass, "r")) == NULL) {
        printf(
            "error：moveDataToFile\nShare_Move_Data."
            "txtをrモードで開けませんでした．\n");
        exit(1);
    } else {
        fgets(buf, 31, fp);
    }
    fclose(fp);

    // bufの内容に変更を加えてShare_Move_Data.txtを上書きする

    if ((fp = fopen(pass, "w")) == NULL) {
        printf("error：Share_Move_Data.txtをwモードで開けませんでした．\n");
        exit(1);
    } else {
        data = strtok(buf, sep);

        fprintf(fp, "%s,", data);
        fprintf(fp, "%d", flag);
    }
    fclose(fp);
}

void setDash(void) { setDashFlag(1); }

void resetDash(void) { setDashFlag(0); }

void setTime(void) {
    char com[128] = "python/python.exe python/minecraft/setTime.py";
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:init\n");
        exit(1);
    }
}

void setMorning(void) {
    char com[128] = "python/python.exe python/minecraft/setMorning.py";
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:init\n");
        exit(1);
    }
}

void setSurvival(void) {
    char com[128] = "python/python.exe python/minecraft/setSurvival.py";
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:init\n");
        exit(1);
    }
}

void setCreative(void) {
    char com[128] = "python/python.exe python/minecraft/setCreative.py";
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:init\n");
        exit(1);
    }
}

void initCameraDataFile(void) { cameraDataToFile("Wait", 0); }

void cameraCenter(void) {
    char key[32] = "C";
    cameraDataToFile(key, 0);
    Sleep(100);
    initCameraDataFile();
}

void cameraDown(double time) {
    char key[32] = "D";
    cameraDataToFile(key, time);
    Sleep(time * 1000);
    initCameraDataFile();
}

void cameraLeft(double time) {
    char key[32] = "L";
    cameraDataToFile(key, time);
    Sleep(time * 1000);
    initCameraDataFile();
}

void cameraRight(double time) {
    char key[32] = "R";
    cameraDataToFile(key, time);
    Sleep(time * 1000);
    initCameraDataFile();
}

void cameraUp(double time) {
    char key[32] = "U";
    cameraDataToFile(key, time);
    Sleep(time * 1000);
    initCameraDataFile();
}

void init(void) {
    char com[128] = "python/python.exe python/minecraft/init.py";
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:init\n");
        exit(1);
    }
    initMoveDataFile();
    initCameraDataFile();
}

void pushKey(char *key) {
    char com[128] = "python/python.exe python/minecraft/pushKey.py ";
    strcat(com, key);
    int f = system(com);
    if (f != 0 && WEXITSTATUS(f) != 0) {
        printf("error:pushKey\n");
        exit(1);
    }
}

int kbhit(void) {
    struct termios oldt, newt;
    int ch;
    int oldf;

    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
    fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);

    ch = getchar();

    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    fcntl(STDIN_FILENO, F_SETFL, oldf);

    if (ch != EOF) {
        ungetc(ch, stdin);
        return 1;
    }

    return 0;
}

void killPython(void) {
    int ret1, ret2, ret3;
    initMoveDataFile();
    initCameraDataFile();

    ret1 = kill(Detect_pid, SIGKILL);
    ret2 = kill(Move_pid, SIGKILL);
    ret3 = kill(Camera_pid, SIGKILL);

    if (ret1 == -1 || ret2 == -1 || ret3 == -1) {
        perror("error:kill");
        printf("error:kill");
        exit(1);
    }
}

int detectPlayer1(void) {
    FILE *fp;
    char fname[] = "python/minecraft/yoloFiles/labels/capture.txt";
    int i, t = 1;
    int zbuf = 0;

    if ((fp = fopen(fname, "r")) == NULL) {
        printf("error:detectPlayer1\n");

        killPython();
        exit(1);
    }
    char buf[256];
    fgets(buf, sizeof(buf), fp);
    (void)fclose(fp);

    for (i = 0; i < 6; i++) {
        zbuf = zbuf + ((buf[5 - i] - '0') * t);
        t = t * 10;
    }

    if (zbuf < 0) {
        return 0;
    }

    return zbuf;
}

int detectPlayer2(void) {
    FILE *fp;
    char fname[] = "python/minecraft/yoloFiles/labels/capture.txt";
    int i, t = 1;
    int zbuf = 0;

    if ((fp = fopen(fname, "r")) == NULL) {
        printf("error:detectPlayer2\n");
        killPython();
        exit(1);
    }
    char buf[256];
    fgets(buf, sizeof(buf), fp);  // 1行目を読み飛ばす
    fgets(buf, sizeof(buf), fp);  // 2行目を読み込む
    (void)fclose(fp);

    for (i = 0; i < 6; i++) {
        zbuf = zbuf + ((buf[5 - i] - '0') * t);
        t = t * 10;
    }

    if (zbuf < 0) {
        return 0;
    }

    return zbuf;
}

void *isInterrupt(void *args) {
    while (rk) {
        if (GetKeyState(VK_F12) < 0) {
            fprintf(stderr, "終了コード送信\n");
            killPython();
            rk = 0;
        }
        Sleep(100);
    }
    rk = 0;
    return args;
}

pthread_t python_thread;

void *respawn(void *arg) {
    char com[128] = "python/python.exe python/minecraft/ssim.py";
    while (rk) {
        int f = system(com);
        if (f != 0 && WEXITSTATUS(f) != 0) {
            printf("error:ssim\n");
            exit(1);
        }
        sleep(1);
    }
    return arg;
}

void *pushesc(void *arg) {
    char com[128] = "python/python.exe python/minecraft/ssim2.py";
    while (rk) {
        int f = system(com);
        if (f != 0 && WEXITSTATUS(f) != 0) {
            printf("error:ssim2\n");
            exit(1);
        }
        sleep(1);
    }
    return arg;
}

void create_python_thread() {
    if (pthread_create(&python_thread, NULL, pushesc, NULL) != 0) {
        fprintf(stderr, "Error creating Python thread.\n");
        exit(1);
    }
}

void close_python_thread() { pthread_join(python_thread, NULL); }

void exePython(void) {
    pthread_t key;
    int kill_p;

    Detect_pid = fork();
    if (-1 == Detect_pid) {
        err(EXIT_FAILURE, "can not fork");
        exit(-1);
    } else if (0 == Detect_pid) {
        int f = execl("python/python.exe", "python/python.exe",
                      "python/minecraft/detectMobs.py", NULL);
        if (f != 0 && WEXITSTATUS(f) != 0) {
            printf("error:detectMobs.py\n");
            exit(1);
        }
    }
    Sleep(100);

    Move_pid = fork();
    if (-1 == Move_pid) {
        err(EXIT_FAILURE, "can not fork");
        exit(-1);
    } else if (0 == Move_pid) {
        int f = execl("python/python.exe", "python/python.exe",
                      "python/minecraft/monitorPlayerMove.py", NULL);
        if (f != 0 && WEXITSTATUS(f) != 0) {
            printf("error:monitorPlayerMove.py\n");
            exit(1);
        }
    }

    Sleep(100);

    Camera_pid = fork();
    if (-1 == Camera_pid) {
        err(EXIT_FAILURE, "can not fork");
        exit(-1);
    } else if (0 == Camera_pid) {
        int f = execl("python/python.exe", "python/python.exe",
                      "python/minecraft/monitorPlayerCamera.py", NULL);
        if (f != 0 && WEXITSTATUS(f) != 0) {
            printf("error:monitorPlayerCamera.py\n");
            exit(1);
        }
    }

    Sleep(100);

    if ((kill_p = pthread_create(&key, NULL, &isInterrupt, NULL)) != 0) {
        fprintf(stderr, "終了監視スレッド作成失敗");
        exit(1);
    }

    Sleep(100);
}

void sleep_time(double time) {
    int t;
    t = time * 1000;
    if (t < 0) {
        t = t * (-1);
    }
    Sleep(t);
}
