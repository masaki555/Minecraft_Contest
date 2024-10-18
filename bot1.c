#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    init();          //Minecraftのゲームコントロール関数．ウィンドウサイズを設定する等を行う．
    create_python_thread();
    exePython();     //画像処理プログラムを実行する関数．
    while(rk){       //無限loopする．rkはF12キーを押すと0となり，プログラムが停止します．
        /*ここからBotプログラム を書く*/
        downKey("w");
        sleep(3);
        upKey("w");
        /*ここまでBotプログラムを書く*/
        sleep(0.1);
    }
    close_python_thread();
}