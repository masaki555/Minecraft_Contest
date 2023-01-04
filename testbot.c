#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(char *argv){
    int han = 0 , han2 = 0 ;
    long han3 = 0; 
    int flag=0;
    init();
    setTime();
    exePython();
    setSurvival();
    while(rk){
        han = detectZombie();
        han2 = detectZombie2();
        han3 = detectMobs(1);
        
        printf("detectZombie1=\t%d\n" , han);
        printf("detectZombie2=\t%d\n" , han2);
        printf("detectMobs=\t%d\n" , han3);
        
        moveForward(1.5);

    }
    setCreative();
    setMorning();
}
