#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>
#include "control.h"

int main(char *argv){

    init();
    pid_t c_pid = fork();
    
    if (c_pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (c_pid == 0) {
        MonitorMoveData();
        exit(EXIT_SUCCESS);
    } else {
        moveForward(2);
        moveForward(2);
        moveLeft(2);
        moveBack(2);
        moveRight(2);

        moveForwardLeft(2);
        moveForwardRight(2);
        moveBackLeft(2);
        moveBackRight(2);

        moveJump(3);
        moveDash(5);
      
        finishMonitor();
        wait(NULL);
    }

    return 0;
}
