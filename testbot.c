#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    int han1 , han3;
    init();          //Minecraftのゲームコントロール関数．ウィンドウサイズを設定する等を行う．
    exePython();     //画像処理プログラムを実行する関数．
    while(rk){       //無限loopする．rkはF12キーを押すと0となり，プログラムが停止します．
        /*ここからBotプログラム を書く*/
        han3 = detectHuman();
        sleep(1);
        printf("han3=%d\n" , han3);

        han1 = detectHuman2();
        sleep(1);
        printf("han1=%d\n" , han1);
        /*ここまでBotプログラムを書く*/
    }
}