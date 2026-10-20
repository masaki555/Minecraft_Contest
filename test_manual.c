#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    printf("1. 初期化コマンド送信\n");
    init();
    exePython();

    // Python側のウィンドウフォーカス処理完了を待つ (2秒)
    sleep_time(2.0);

    printf("2. Wキー押下 (前進開始)\n");
    downKey("w");

    // 3秒間 前進し続ける
    sleep_time(3.0);

    printf("3. Wキー離す (停止)\n");
    upKey("w");

    return 0;
}