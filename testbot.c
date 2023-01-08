#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(char *argv){
    int han;
    init();
    exePython();
    while(rk){
        moveForward(1);
        han = detectZombie();
        printf("%d\n" , han );
        if(han == 0){
            cameraRight(1);
        }else{
            while (han != 0)
            {
                printf("%d\n" , han);
                switch (han / 2)
                {
                case 32:
                    moveForwardLeft(1);
                break;
                case 16:
                    moveForward(1);
                    break;
                case 8:
                    moveForwardRight(1);
                    break;
                case 4:
                    moveBackLeft(1);
                    break;
                case 2:
                    break;
                case 1:
                    moveBackRight(1);
                    break;
                default:
                    break;
                }
                moveBack(1);
                attackLeft();
                han = detectZombie();
            }
        }
    }
    setCreative();
    setMorning();
}
