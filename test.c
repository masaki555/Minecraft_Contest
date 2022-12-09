#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include<time.h>
#include "control.h"

int main(int argc, char *argv){
    int ibuf[256];
    long cbuf, zbuf;
    int bufLen;
    /*
    int flag=0;
    init();
    setTime();
    exePython();
    setSurvival();*/
    init();
    exePython();

    while(rk){
        bufLen = detectMobsAbout(1, ibuf);
        cbuf = detectMobsSimple(1);
        zbuf = detectMobsSimple(2);

        printf("\n");
        printf("\n");
        printf("%d\n", zbuf);
        printf("%d\n", cbuf);
        for(int i=0; i < bufLen; i++) {
            printf("%d", ibuf[i]);
        }
        printf("\n");
        sleep(1);
    }
}
