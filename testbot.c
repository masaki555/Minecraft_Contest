#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    int han1 , han2;
    int flag = 0;
    int cnt = 0;
    init();
    exePython();
    while(rk){
        flag=0;
        han1 = detectPlayer1();
        han2 = detectPlayer2();
        printf("han1=%06d\n" , han1);
        printf("han2=%06d\n" , han2);
        if((han1/1000%10==1||han2/1000%10==1)&&(han1/100%10==1||han2/100%10==1)){
        }
        else if(han1/1000%10==1||han2/1000%10==1){
            pushKey("left");
        }
        else if(han1/100%10==1||han2/100%10==1){
            pushKey("right");
        }

        else if(han1/10000%10==1||han2/10000%10==1){
            cameraLeft(0.3);
        }
        
        else if(han1/10%10==1||han2/10%10==1){
            cameraRight(0.3);
        }

        else if(han1/100000==1||han2/100000==1){
            cameraLeft(0.5);
        }
        else if(han1/1%10==1||han2/1%10==1){
            cameraRight(0.5);
        }
        else{
            cameraRight(0.5);
            flag=1;
            cnt++;
            if(cnt>=10){
                flag=0;
                cnt=0;
            }
        }

        if(flag==0){
            cnt=0;
            attackLeft();
            downKey("ctrl");
            downKey("w");
            attackLeft_continuous(5);
            upKey("ctrl");
            upKey("w");
        }

        sleep_time(1);
    }
}