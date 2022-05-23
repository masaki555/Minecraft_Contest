#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(char *argv){
    int han , han2;
    int flag=0;
    init();
    setTime();
    exePython();
    setSurvival();
    while(rk){
        printf("%d\n" , han );
        han = detectZombie();
        han2 = detectZombie2();
        printf("%d\n" , han2);
        if(flag==0){
            if( (han/1000000)==1 && ((han/100000)%10)==1 && ((han/10000)%10)==1 ){
                moveBack();
                moveBack();
            }else{
                if( ((han/100000)%10)==1 && ((han/100)%10)==1 ){
                    attackLeft();
                    han = detectZombie();
                    flag=1;
                }else if((han/1000000)==1){
                    cameraLeft();
                }else if(((han/10000)%10)==1){
                    cameraRight();
                }else if(((han/1000)%10)==1){
                    cameraLeft();
                }else if(((han/10)%10)==1){
                    cameraRight();
                }else{
                    cameraRight();
                    moveBack();
                    sleep(0.05);
                }
            }
        }
        if(flag==1){
            if((han%10)==1){
                    moveForward();
            }
            flag=0;
        }
        attackLeft();
        sleep(0.1);
    }
    setCreative();
    setMorning();
}
