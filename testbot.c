#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>

#include "control.h"

int main(int argc, char *argv[]){
    srand((unsigned int)time(NULL));

    init();
    exePython();
    while(rk){
        int num = rand() % 7;
        switch(num) {
            case 1:
                moveBack(1);
                break;
            case 2:
                moveForward(2);
                break;
            case 3:
                moveLeft(1);
                break;
            case 4:
                moveRight(1);
                break;
            case 5:
                attackLeft();
                break;
            case 6:
                sleep(1);
                break;
        }
    }
    return 0;
}
