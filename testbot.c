#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    init();          //Minecraftのゲームコントロール関数．ウィンドウサイズを設定する等を行う．
    exePython();     //画像処理プログラムを実行する関数．
    setSurvival();   //サバイバルモードにする．
    while(rk){       //無限loopする．rkはF12キーを押すと0となり，プログラムが停止します．
        /*ここからBotプログラムを書く*/
        printf("ゾンビ:%d\n",detectZombie3());

        /*ここまでBotプログラムを書く*/
        sleep(1);
    }
}