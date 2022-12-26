#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include "control.h"

int main(int argc, char *argv)
{
    int buf;
    int bufLen;

    int flag = 0;
    init();
    exePython();
    // setTime();
    // setSurvival();

    while (rk)
    {
        buf = detectZombie3();

        printf("\n");
        printf("%6d\n", buf);
        printf("\n");
        // 実際に動かすときにはsleepは不要
        // 現状何もしていないため検出より早く出力してしまう
        sleep(1);
    }
}
