#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include "control.h"

int main(int argc, char *argv)
{
    int ibuf[256];
    int cbuf, zbuf;
    int bufLen;

    int flag = 0;
    init();
    exePython();
    // setTime();
    // setSurvival();

    while (rk)
    {
        cbuf = detectMobsSimple(1);
        zbuf = detectMobsSimple(2);

        printf("\n");
        printf("%010d\n", zbuf);
        printf("%010d\n", cbuf);
        for (int i = 0; i < bufLen; i++)
        {
            printf("%d", ibuf[i]);
        }
        printf("\n");
        // 実際に動かすときにはsleepは不要
        // 現状何もしていないため検出より早く出力してしまう
        sleep(1);
    }
}
