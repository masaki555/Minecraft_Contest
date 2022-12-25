#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include<time.h>
#include "control.h"

int main(int argc, char *argv){
    init();

    moveForward(3);
    moveLeft(3);
    moveBack(3);
    moveRight(3);
    moveForwardLeft(3);
    moveBackLeft(3);
    moveBackRight(3);
    moveForwardRight(3);
    setDash();
    moveForward(5);
    resetDash();

    finishMonitor();
}
