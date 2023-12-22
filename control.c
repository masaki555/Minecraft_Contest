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

#define PRINT_HERE \
   fprintf(stderr, "File:%s Line:%d\t", __FILE__, __LINE__)

pid_t Detect1_pid;
pid_t Detect2_pid;
pid_t Detect3_pid;
pid_t Move_pid;
pid_t Camera_pid;
int rk=1;

void attackLeft(void){
    char com[128] = "python/python.exe python/minecraft/clickLeft.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:attackLeft\n");
        exit(1);
    }
}
void attackLeft_long(void){
    char com[128] = "python/python.exe python/minecraft/clickLeft_long.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:attackLefy_long\n");
        exit(1);
    }
}

void moveDataToFile(char* key){
    FILE *fp;
    char pass[64] = "python/tmp/Share_Move_Data.txt";
    char buf[32]="";
    const char* const sep = ",";
    char *data;
    
    // Share_Move_Data.txtの内容をbufに保存する

    if((fp=fopen(pass, "r"))==NULL){
        printf("error：moveDataToFile\nShare_Move_Data.txtをrモードで開けませんでした．\n");
        exit(1);
    }else{
        fgets(buf, 31, fp);
    }
    fclose(fp);

    // bufの内容に変更を加えてShare_Move_Data.txtを上書きする

    if((fp=fopen(pass, "w"))==NULL){
        printf("error：Share_Move_Data.txtをwモードで開けませんでした．\n");
        exit(1);
    }else{
        data = strtok(buf, sep);
        data = strtok(NULL, sep);
        if(data != NULL){
            fprintf(fp, "%s,%s", key, data);
        }else{
            fprintf(fp, "%s,%s", key, "0");
            //printf("error:moveDataToFile\n");
        }
    }
    fclose(fp);
}

void cameraDataToFile(char* key, double sleep_time){
    FILE *fp;
    char pass[64] = "python/tmp/Share_Camera_Data.txt";
    char buf[32]="";
    char *data;
    
    if((fp=fopen(pass, "r"))==NULL){
        printf("error：Share_Camera_Data.txtをrモードで開けませんでした．\n");
        exit(1);
    }else{
        fgets(buf, 31, fp);
    }
    fclose(fp);

    if((fp=fopen(pass, "w"))==NULL){
        printf("error：Share_Camera_Data.txtをwモードで開けませんでした．\n");
        exit(1);
    }else{
        fprintf(fp, "%s,%f", key, (float)sleep_time);
    }
    fclose(fp);
}


void initMoveDataFile(void){
    moveDataToFile("Wait");
}


void moveForward(double sleep_time){
    char key[32]  ="F";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();  
    //usleep(0.15*1000000);  
}

void moveLeft(double sleep_time){
    char key[32]  ="L";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();  
    //usleep(0.15*1000000);
}

void moveRight(double sleep_time){
    char key[32]  ="R";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile(); 
    //usleep(0.15*1000000);  
}

void moveBack(double sleep_time){
    char key[32]  ="B";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile(); 
    //usleep(0.15*1000000);
}

void moveForwardLeft(double sleep_time){
    char key[32]  ="FL";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    //usleep(0.37*1000000);
}

void moveForwardRight(double sleep_time){
    char key[32]  ="FR";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    //usleep(0.37*1000000);
}

void moveBackLeft(double sleep_time){
    char key[32]  ="BL";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    //usleep(0.37*1000000);
}

void moveBackRight(double sleep_time){
    char key[32]  ="BR";
    moveDataToFile(key);
    Sleep(sleep_time * 1000);
    initMoveDataFile();
    //usleep(0.37*1000000);
}

void moveJump(int times){
    char str[128] = "python/python.exe python/minecraft/moveCharacterJump.py";
    char com[256];
    sprintf(com, "%s %d", str, times);
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:moveJump\n");
        exit(1);
    }
}


void moveDash(int times){
    char str[128] = "python/python.exe python/minecraft/moveCharacterJumpDash.py";
    char com[256];
    sprintf(com, "%s %d", str, times);
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:moveJump\n");
        exit(1);
    }
}


void setDashFlag(int flag){
    FILE *fp;
    char pass[64] = "python/tmp/Share_Move_Data.txt";
    char buf[32] = "";
    const char* const sep = ",";
    char *data;

    // Share_Move_Data.txtの内容をbufに保存する

    if((fp=fopen(pass, "r"))==NULL){
        printf("error：moveDataToFile\nShare_Move_Data.txtをrモードで開けませんでした．\n");
        exit(1);
    }else{
        fgets(buf, 31, fp);
    }
    fclose(fp);

    // bufの内容に変更を加えてShare_Move_Data.txtを上書きする

    if((fp=fopen(pass, "w"))==NULL){
        printf("error：Share_Move_Data.txtをwモードで開けませんでした．\n");
        exit(1);
    }else{
        data = strtok(buf, sep);
        
        fprintf(fp, "%s,", data);
        fprintf(fp, "%d", flag);
    }
    fclose(fp);
}

void setDash(void){
    setDashFlag(1);
}

void resetDash(void){
    setDashFlag(0);
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

void initCameraDataFile(void){
    cameraDataToFile("Wait", 0);
}

void cameraCenter(void){
    char key[32]  ="C";
    cameraDataToFile(key ,0);
    Sleep(100);
    initCameraDataFile();
}

void cameraDown(double time){
    char key[32]  ="D";
    cameraDataToFile(key ,time);
    Sleep(time * 1000);
    initCameraDataFile();
}

void cameraLeft(double time){
    char key[32]  ="L";
    cameraDataToFile(key ,time);
    Sleep(time * 1000);
    initCameraDataFile();
}

void cameraRight(double time){
    char key[32]  ="R";
    cameraDataToFile(key ,time);
    Sleep(time * 1000);
    initCameraDataFile();
}

void cameraUp(double time){
    char key[32]  ="U";
    cameraDataToFile(key ,time);
    Sleep(time * 1000);
    initCameraDataFile();
}

void init(void){
    char com[128] = "python/python.exe python/minecraft/init.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:init\n");
        exit(1);
    }
    initMoveDataFile();
    initCameraDataFile();
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

int detectZombie1(void){
    FILE	*fp;
	char	fname[] = "./python/tmp/detect_zombie1.txt";
    int i,ibuf=0,t=1;

	if ( (fp=fopen(fname,"r")) ==NULL) {
		printf("error:detectZombie\n");
		exit(1);
	}
	char buf[256];
	fgets(buf, sizeof(buf), fp);
	(void) fclose(fp);

    ibuf = atoi(buf);
    /*
    for(i=0;i<7;i++){
        ibuf = ibuf + ((buf[6-i] - '0') * t );
        t = t * 10;
    }
    */

    return ibuf;
}

long detectZombie2(void){
    FILE	*fp;
	char	fname[] = "./python/tmp/detect_zombie2.txt";
    int i,t=1;
    long ibuf=0;

	if ( (fp=fopen(fname,"r")) ==NULL) {
		printf("error:detectZombie\n");
		exit(1);
	}
	char buf[256];
	fgets(buf, sizeof(buf), fp);
	(void) fclose(fp);

    ibuf = atol(buf);

    return ibuf;
}

int detectZombie3(void) {
    FILE	*fp;
	char	fname[] = "python/tmp/detect_zombie3.txt";
    int i, t=1;
    int zbuf=0;

	if ( (fp=fopen(fname,"r")) ==NULL) {
		printf("error:detectZombie3\n");
        killPython();
		exit(1);
	}
	char buf[256];
	fgets(buf, sizeof(buf), fp);
	(void) fclose(fp);
    
    for(i=0;i<6;i++){
        zbuf = zbuf + ((buf[5 - i] - '0') * t);
        t = t * 10;
    }

    if(zbuf < 0) {
        return 0;
    }

    return zbuf;
}

int detectMobsArray(int mode , int ibuf[]) {
    FILE	*fp; 
    char	*fname;
    int     i;

    if(mode == 1) {
	    fname = "./python/tmp/t_creeper.txt";
    }else if(mode == 2){
	    fname = "./python/tmp/t_zombie.txt";
    }else {
        printf("error:detectMobs\n");
        printf("Non accepted mode value\n");
		exit(1);
    }

    if ( (fp=fopen(fname,"r")) == NULL) {
		printf("error:detectMobs\n");
		exit(1);
	}

	char buf[256];
	fgets(buf, sizeof(buf), fp);
	(void) fclose(fp);
    int bufLength = strlen(buf);
    
    for(i=0; i<256; i++){
        ibuf[i] = 0;
    }

    for(i=0;i<bufLength;i++){
        ibuf[i] = buf[i] - '0';
    }
    
    return bufLength;
}

int detectMobs(void) {
    FILE	*fp;
	char	fname[] = "./python/tmp/detect_mobs.txt";
    int i, t=1;
    int obuf = 0;

    if ( (fp=fopen(fname,"r")) == NULL) {
		printf("error:detectMobs\n");
		exit(1);
	}
	char buf[256];
	fgets(buf, sizeof(buf), fp);
	(void) fclose(fp);
    
    for(i=0;i<6;i++){
        obuf = obuf + ((buf[5 - i] - '0') * t);
        t = t * 10;
    }

    return obuf;
}

void killPython(void){
    int ret1,ret2,ret3,ret4,ret5;
    initMoveDataFile();
    initCameraDataFile();

    ret1 = kill(Detect1_pid, SIGKILL);
    ret2 = kill(Detect2_pid, SIGKILL);
    ret3 = kill(Detect3_pid, SIGKILL);
    ret4 = kill(Move_pid, SIGKILL);
    ret5 = kill(Camera_pid, SIGKILL);
    
    if (ret1 == -1 || ret2 == -1 || ret3 == -1 || ret4 == -1 || ret5 == -1) {
        perror("error:kill");
        printf("error:kill");
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
    pthread_t key;
    int kill_p ;
    
    Detect1_pid = fork ();
    if (-1 == Detect1_pid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Detect1_pid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/detectZombie1.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:detectZombie1.py\n");
            exit(1);
        }
    }
    Sleep(100);
    
    Detect2_pid = fork ();
    if (-1 == Detect2_pid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Detect2_pid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/detectZombie2.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:detectZombie2.py\n");
            exit(1);
        }
    }
    Sleep(100);

    Detect3_pid = fork ();
    if (-1 == Detect3_pid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Detect3_pid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/detectMobs.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:detectMobs.py\n");
            exit(1);
        }
    }
    Sleep(100);

    Move_pid = fork();
    if (-1 == Move_pid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Move_pid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/monitorPlayerMove.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:monitorPlayerMove.py\n");
            exit(1);
        }
    }
    
     Sleep(100);

    Camera_pid = fork();
    if (-1 == Camera_pid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Camera_pid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/monitorPlayerCamera.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:monitorPlayerCamera.py\n");
            exit(1);
        }
    }

     Sleep(100);

    if ((kill_p = pthread_create(&key, NULL, &isInterrupt , NULL)) != 0) {
        fprintf(stderr, "終了監視スレッド作成失敗");
        exit(1);
    }

     Sleep(100);
}
