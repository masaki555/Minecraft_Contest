#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    int helmet , boots;
    int flag = 0;
    int cnt = 0;
    init();
    exePython();
    while(rk){
        flag = 0;
        helmet = detectPlayer1();
        boots = detectPlayer2();
        printf("helmet=%06d\n" , helmet);
        printf("boots=%06d\n" , boots);
        
        if((helmet/1000%10==1||boots/1000%10==1)&&(helmet/100%10==1||boots/100%10==1)){
        }
        else if(helmet/1000%10==1||boots/1000%10==1){
            pushKey("left");
        }
        else if(helmet/100%10==1||boots/100%10==1){
            pushKey("right");
        }
        else if(helmet/10000%10==1||boots/10000%10==1){
            cameraLeft(0.3);
        }
        else if(helmet/10%10==1||boots/10%10==1){
            cameraRight(0.3);
        }
        else if(helmet/100000==1||boots/100000==1){
            cameraLeft(0.5);
        }
        else if(helmet/1%10==1||boots/1%10==1){
            cameraRight(0.5);
        }
        else{
            cameraRight(0.5);
            flag = 1;
            cnt++;
            if(cnt>=10){
                flag = 0;
                cnt = 0;
            }
        }

        if(flag==0){
            cnt = 0;
            attackLeft();
            downKey("ctrl");
            downKey("w");
            attackLeft_continuous(5);
            upKey("ctrl");
            upKey("w");
        }
        
        sleep_time(0.8);
    }
}
