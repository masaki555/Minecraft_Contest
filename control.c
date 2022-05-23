#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <err.h>
#include <termios.h>
#include <fcntl.h>
#include <windows.h>
#include "control.h"
#include <pthread.h>

pid_t Ppid;
pid_t Kpid;
int rk=1;

void attackLeft(void){
    char com[128] = "python/python.exe python/minecraft/clickLeft.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:attackLeft\n");
        exit(1);
    }
}
void attackRight(void){
    char com[128] = "python/python.exe python/minecraft/clickRight.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:attackRight\n");
        exit(1);
    }
}
void moveForward(void){
    char com[128] = "python/python.exe python/minecraft/moveCharacterFowerd.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:moveForward\n");
        exit(1);
    }
}
void moveLeft(void){
    char com[128] = "python/python.exe python/minecraft/moveCharacterLeft.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:moveLeft\n");
        exit(1);
    }
}
void moveRight(void){
    char com[128] = "python/python.exe python/minecraft/moveCharacterRight.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:moveRight\n");
        exit(1);
    }
}
void moveBack(void){
    char com[128] = "python/python.exe python/minecraft/moveCharacterBack.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:moveBack\n");
        exit(1);
    }
}


void init(void){
    char com[128] = "python/python.exe python/minecraft/init.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void setTime(void){
    char com[128] = "python/python.exe python/minecraft/setTime.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void setMorning(void){
    char com[128] = "python/python.exe python/minecraft/setMorning.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void setSurvival(void){
    char com[128] = "python/python.exe python/minecraft/setSurvival.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void setCreative(void){
    char com[128] = "python/python.exe python/minecraft/setCreative.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
}

void cameraPos(void){
    char com[128] = "python/python.exe python/minecraft/initCameraPos.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:cameraPos\n");
        exit(1);
    }
}

void cameraDown(void){
    char com[128] = "python/python.exe python/minecraft/moveCameraDown.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:cameraDown\n");
        exit(1);
    }
}
void cameraLeft(void){
    char com[128] = "python/python.exe python/minecraft/moveCameraLeft.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:cameraLeft\n");
        exit(1);
    }
}
void cameraRight(void){
    char com[128] = "python/python.exe python/minecraft/moveCameraRight.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:cameraRight\n");
        exit(1);
    }
}
void cameraUp(void){
    char com[128] = "python/python.exe python/minecraft/moveCameraUp.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:cameraUp\n");
        exit(1);
    }
}

void pushKey(char* key){
    char com[128] = "python/python.exe python/minecraft/pushKey.py ";
    strcat(com, key);
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:pushKey\n");
        exit(1);
    }
}


int kbhit(void){
    struct termios oldt, newt;
    int ch;
    int oldf;

    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
    fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);

    ch = getchar();

    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    fcntl(STDIN_FILENO, F_SETFL, oldf);

    if (ch != EOF){
        ungetc(ch, stdin);
        return 1;
    }

    return 0;
}

int detectZombie(void){
    FILE	*fp;
	char	fname[] = "tmp.txt";
    int i,ibuf=0,t=1;

	if ( (fp=fopen(fname,"r")) ==NULL) {
		printf("error:detectZombie\n");
		exit(1);
	}
	char buf[256];
	fgets(buf, sizeof(buf), fp);
	(void) fclose(fp);

    for(i=0;i<7;i++){
        ibuf = ibuf + ((buf[6-i] - '0') * t );
        t = t * 10;
    }

    return ibuf;
}

int detectZombie2(void){
    FILE	*fp;
	char	fname[] = "tmp2.txt";
    int i,ibuf=0,t=1;

	if ( (fp=fopen(fname,"r")) ==NULL) {
		printf("error:detectZombie\n");
		exit(1);
	}
	char buf[256];
	fgets(buf, sizeof(buf), fp);
	(void) fclose(fp);

    ibuf = atoi(buf);

    return ibuf;
}


void killPython(void){
    int ret1,ret2;
    ret1 = kill(Ppid, SIGKILL);
    ret2 = kill(Kpid, SIGKILL);
    if (ret1 == -1 || ret2 == -1) {
        perror("error:kill");
        exit(1);
    }
}

void *exeDetectZombie(void *args){
    char com[128] = "python/python.exe python/minecraft/detectZombie.py";
    
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:pushKey\n");
        exit(1);
    }
}

void *isInterrupt(void *args){
    while(rk){
        if (GetKeyState(VK_F12) < 0 ){
            fprintf(stderr , "終了コード送信\n" );
            killPython();
            rk=0;
        }
        Sleep(100);
    }
    rk=0;
}

void exePython(void){
    char com[128] = "python/python.exe python/minecraft/detectZombie.py";

    pthread_t key;
    int ret;

    Ppid = fork ();
    if (-1 == Ppid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Ppid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/detectZombie.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:exePython\n");
            exit(1);
        }
    }
    Sleep(100);
    Kpid = fork ();
    if (-1 == Kpid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Kpid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/detectZombie2.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:exePython\n");
            exit(1);
        }
    }
   
    if ((ret = pthread_create(&key, NULL, &isInterrupt , NULL)) != 0) {
        fprintf(stderr, "スレッド作成失敗");
        exit(1);
    }
}
