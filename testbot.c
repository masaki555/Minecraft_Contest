#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(char *argv){
    int han1 , han3;
    long han2;
    int flag=0;
    init();
    setTime();
    exePython();
    setSurvival();
    while(rk){
        han1 = detectZombie1();
        han2 = detectZombie2();
        han3 = detectZombie3();
        printf("han1=%d\n" , han1);
        printf("han2=%ld\n" , han2);
        printf("han3=%d\n" , han3);
        if(flag==0){
            if( (han1/1000000)==1 && ((han1/100000)%10)==1 && ((han1/10000)%10)==1 ){
                moveBack(0.5);
            }else{
                if( ((han1/100000)%10)==1 && ((han1/100)%10)==1 ){
                    attackLeft();
                    han1 = detectZombie1();
                    flag=1;
                }else if((han1/1000000)==1){
                    cameraLeft(0.3);
                }else if(((han1/10000)%10)==1){
                    cameraRight(0.3);
                }else if(((han1/1000)%10)==1){
                    cameraLeft(1);
                }else if(((han1/10)%10)==1){
                    cameraRight(0.5);
                }else{
                    cameraRight(0.5);
                    moveBack(0.5);
                    sleep(0.05);
                }
            }
        }
        if(flag==1){
            if((han1%10)==1){
                    moveForward(1);
            }
            flag=0;
        }
        attackLeft();
        sleep(0.1);
    }
    setCreative();
    setMorning();
}
