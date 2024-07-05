#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]) {
    init();
    exePython();
    while(rk){
        upKey("Shift");
        attackLeft_long();
        attackLeft_long();
        attackLeft_long();
        attackLeft_long();
        downKey("Shift");
    }
    return 0;
}
