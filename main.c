#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]) {
    init();
    setTime();
    exePython();
    setSurvival();
    while(rk){
        downKey("shift");
        attackLeft_continuous(10);
        eat(2);
        upKey("shift");
    }
    setCreative();
    setMorning();
    return 0;
}
