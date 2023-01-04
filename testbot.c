#include <stdio.h>
#include <unistd.h>
#include "control.h"

int printBinary(int value){
    int binary = 0;
    int base = 1;

    while(value>0){
        binary = binary + ( value % 2 ) * base;
        value = value / 2;
        base = base * 10;
    }
    return binary;
}

int main(char *argv){
    int han = 0 , han2 = 0 , han3 = 0;
    int flag=0;
    init();
    //setTime();
    exePython();
    //setSurvival();
    while(rk){
        han = printBinary(detectZombie());
        han2 = printBinary(detectZombie2());
        han3 = printBinary(detectMobs(1));
        /*
        han = detectZombie();
        han2 = detectZombie2();
        han3 = detectMobs(1);
        */
        printf("detectZombie1=\t%d\n" , han);
        printf("detectZombie2=\t%d\n" , han2);
        printf("detectMobs=\t%d\n" , han3);
        
        moveForward(1.5);
        //cameraRight(2.0);

    }
    //setCreative();
    //setMorning();
}
