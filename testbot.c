#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    int head, boot;
    int flag = 0;
    int flag2 = 0;
    int flag3 = 0;
    int flag4 = 0;
    int flag5 = 0;
    int lived = 0;
    int count = 0;
    int count2 = 0;
    int cFlag = 0;

    init();          //Minecraftのゲームコントロール関数．ウィンドウサイズを設定する等を行う．
    exePython();     //画像処理プログラムを実行する関数．
    while(rk){       //無限loopする．rkはF12キーを押すと0となり，プログラムが停止します．
        /*ここからBotプログラム を書く*/
        head = detectHuman();
        printf("head=%d\n" , head);

        boot = detectHuman2();
        printf("boot=%d\n" , boot);
        /*ここまでBotプログラムを書く*/

        if((head/100000==1 || boot/100000==1) && flag == 0){ //画面左端に存在する場合、左にカメラを向ける
           printf("左端\n");
           pushKey("left"); 
           downKey("w");
           upKey("w");
           flag++;
        } else if ((head/10000==1 || boot/10000==1) && flag2 == 0){
            printf("真ん中左寄り\n");
            cameraLeft(0.1); //検知してから動作するまでがかなり遅い
            downKey("s");
            upKey("s");
            flag2++;
        } else if (head/1000==1 || boot/10000==1 || head/100==1 || boot/100==1){
            printf("真ん中左または右\n");
            downKey("w");
            attackLeft_continuous(5);
            upKey("w");
        } else if((head/10==1 || boot/10==1) && flag4==0){
            printf("真ん中右寄り\n");
            cameraRight(0.1);
            downKey("s");
            upKey("s");
            flag4++;
        } else if ((head==1 || boot==1) && flag5 == 0){
            printf("右端\n");
            pushKey("right");
            downKey("w");
            upKey("w");
            flag5++;
        } else if (head==0){
            printf("見つからない\n");
            while(rk){

                if(cFlag == 0){
                    pushKey("left");
                    downKey("s");
                    attackLeft_continuous(5);
                    upKey("s");
                    count++;
                } else {
                    pushKey("right");
                    downKey("s");
                    attackLeft_continuous(5);
                    upKey("s");
                    count2++;
                }

                if(detectHuman() != 0){
                    break;
                }

                if(count == 5 && cFlag == 0){
                    downKey("w");
                    attackLeft_continuous(5);
                    upKey("w");
                    pushKey("j");
                    count = 0;
                    cFlag = 1;
                    break;
                } else if(count2 == 5 && cFlag == 1){
                    downKey("w");
                    attackLeft_continuous(5);
                    upKey("w");
                    pushKey("h");
                    count2 = 0;
                    cFlag = 0;
                    break;
                }
            }
        }

        flag++;
        flag2++;
        flag3++;
        flag4++;
        flag5++;

        if(flag >= 2){
            flag = 0;
        } 
        if(flag2 >= 2){
            flag2 = 0;
        }
        if(flag3 >= 2){
            flag3 = 0;
        }
        if(flag4 >= 2){
            flag4 = 0;
        }
        if(flag5 >= 2){
            flag5 = 0;
        }
        sleep(1);
    }   
}