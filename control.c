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
pid_t Mpid;
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

void moveDataToFile(char* key, int sleep_time){
    FILE *fp;

    if((fp=fopen("python/movedata/share_MoveData.txt", "w"))==NULL){
        printf("error：moveDataToFile\nshare_MoveData.txtを開けませんでした．\n");
        exit(1);
    }else{
        fprintf(fp, "%s\n", key);
        fprintf(fp,"%d\n", sleep_time);
    }

    fclose(fp);
}

void initMoveDataFile(void){
    FILE *fp;

    if((fp=fopen("python/movedata/share_MoveData.txt", "w"))==NULL){
        printf("error：initMoveDataFile\n");
        printf("       share_MoveData.txtを開けませんでした．\n");
        exit(1);
    }else{
    fprintf(fp,"Wait\n");
    fprintf(fp,"0\n");
    }
  
    fclose(fp);
}

void MonitorMoveData(void){
    initMoveDataFile();
    FILE *fp;
    char com[128] = "python/python.exe python/minecraft/monitorPlayerMove.py";
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:MonitorMoveData\n");
        exit(1);
    }
}

void finishMonitor(void){
    printf("プレイヤの移動の監視を終了します．\n");
    moveDataToFile("Finish",0);
}

void moveForward(int sleep_time){
    char key[32]  ="F";
    moveDataToFile(key ,sleep_time);
    sleep(sleep_time);
    initMoveDataFile();    
}

void moveLeft(double sleep_time){
    char key[32]  ="L";
    moveDataToFile(key ,sleep_time);
    sleep(sleep_time);
    initMoveDataFile();  
}

void moveRight(double sleep_time){
    char key[32]  ="R";
    moveDataToFile(key ,sleep_time);
    sleep(sleep_time);
    initMoveDataFile();   
}

void moveBack(double sleep_time){
    char key[32]  ="B";
    moveDataToFile(key ,sleep_time);
    sleep(sleep_time);
    initMoveDataFile(); 
}

void moveForwardLeft(double sleep_time){
    char key[32]  ="FL";
    moveDataToFile(key ,sleep_time);
    sleep(sleep_time);
    initMoveDataFile();
}

void moveForwardRight(double sleep_time){
    char key[32]  ="FR";
    moveDataToFile(key ,sleep_time);
    sleep(sleep_time);
    initMoveDataFile();
}

void moveBackLeft(double sleep_time){
    char key[32]  ="BL";
    moveDataToFile(key,sleep_time);
    sleep(sleep_time);
    initMoveDataFile();
}

void moveBackRight(double sleep_time){
    char key[32]  ="BR";
    moveDataToFile(key ,sleep_time);
    sleep(sleep_time);
    initMoveDataFile();
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

void moveDash(double sleep_time){
    char str[128] = "python/python.exe python/minecraft/moveCharacterDash.py";
    char com[256];
    sprintf(com, "%s %lf", str, sleep_time);
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:moveDash\n");
        exit(1);
    }
}

void moveJumpDash(int times){
    char str[128] = "python/python.exe python/minecraft/moveCharacterJumpDash.py";
    char com[256];
    sprintf(com, "%s %d", str, times);
    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:moveJumpDash\n");
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

int detectMobsDetail(int mode, int ibuf[]) {
    FILE	*fp; 
    char	*fname;
    int     i;

    if(mode == 1) {
	    fname = "t_creeper.txt";
    }else if(mode == 2){
	    fname = "t_zombie.txt";
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

int detectMobsAbout(int mode, int ibuf[]) {
    FILE	*fp; 
    char	*fname;
    int     i;

    if(mode == 1) {
	    fname = "t_creeper.txt";
    }else if(mode == 2){
	    fname = "t_zombie.txt";
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

long detectMobsSimple(int mode) {
    FILE	*fp;
	char	fname[] = "t_simple.txt";
    int i, t=1;
    // クリーパーの情報
    long cbuf=0;
    // ゾンビの情報
    long zbuf=0;

	if ( (fp=fopen(fname,"r")) ==NULL) {
		printf("error:detectMobs\n");
		exit(1);
	}
	char buf[256];
	fgets(buf, sizeof(buf), fp);
	(void) fclose(fp);
    
    for(i=0;i<10;i++){
        cbuf = cbuf + ((buf[10 - i] - '0') * t);
        zbuf = zbuf + ((buf[21 - i] - '0') * t);
        t = t * 10;
    }

    if(mode == 1){
        return cbuf;
    }else {
        return zbuf;
    }
}

void killPython(void){
    int ret1,ret2,ret3;
    // ret1 = kill(Ppid, SIGKILL);
    // ret2 = kill(Kpid, SIGKILL);
    ret3 = kill(Mpid, SIGKILL);
    if (ret1 == -1 || ret2 == -1 || ret3 == -1) {
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

void *exeDetectMobs(){
    char com[128] = "python/python.exe python/minecraft/detectMobs.py";

    int f = system(com);
    if(f != 0 && WEXITSTATUS(f) != 0 ){
        printf("error:detectMobs\n");
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

    Mpid = fork ();
    if (-1 == Mpid){
        err (EXIT_FAILURE, "can not fork");
        exit(-1);
    }else if (0 == Mpid){
        int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/detectMobs.py" , NULL);
        if(f != 0 && WEXITSTATUS(f) != 0 ){
            printf("error:exePython\n");
            exit(1);
        }
    }
    Sleep(100);
    // Ppid = fork ();
    // if (-1 == Ppid){
    //     err (EXIT_FAILURE, "can not fork");
    //     exit(-1);
    // }else if (0 == Ppid){
    //     int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/detectZombie.py" , NULL);
    //     if(f != 0 && WEXITSTATUS(f) != 0 ){
    //         printf("error:exePython\n");
    //         exit(1);
    //     }
    // }
    // Sleep(100);
    // Kpid = fork ();
    // if (-1 == Kpid){
    //     err (EXIT_FAILURE, "can not fork");
    //     exit(-1);
    // }else if (0 == Kpid){
    //     int f = execl("python/python.exe" , "python/python.exe" ,"python/minecraft/detectZombie2.py" , NULL);
    //     if(f != 0 && WEXITSTATUS(f) != 0 ){
    //         printf("error:exePython\n");
    //         exit(1);
    //     }
    // }

    
   
    if ((ret = pthread_create(&key, NULL, &isInterrupt , NULL)) != 0) {
        fprintf(stderr, "スレッド作成失敗");
        exit(1);
    }
}
