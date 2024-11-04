#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    init();          //Minecraftのゲームコントロール関数．ウィンドウサイズを設定する等を行う．
    exePython();     //画像処理プログラムを実行する関数
    while(rk){       //無限loopする．rkはF12キーを押すと0となり，プログラムが停止します．
        /*ここからBotプログラム を書く*/
        printf("detectPlayer1:%06d\n",detectPlayer1());
        printf("detectPlayer2:%06d\n",detectPlayer2());
        /*ここまでBotプログラム を書く*/
        sleep_time(1);
    }
}