extern pid_t pid;
extern int rk;

void attackLeft(void);
void attackRight(void);

void moveDataToFile(char* key, int sleep_time);
void initMoveDataFile(void);
void* monitorMoveData(void *arg);
void finishMonitor(void);
void moveForward(int time);
void moveLeft(double time);
void moveRight(double time);
void moveBack(double time);
void moveForwardLeft(double time);
void moveForwardRight(double time);
void moveBackLeft(double time);
void moveBackRight(double time);
void moveJump(int times);
void setDashFlag(int flag);
void setDash(void);
void resetDash(void);

void init(void);
void setTime(void);
void setMorning(void);
void setSurvival(void);
void setCreative(void);
void cameraPos(void);

void cameraDown(void);
void cameraLeft(void);
void cameraRight(void);
void cameraUp(void);
void pushKey(char* key);

int kbhit(void);
void *isInterrupt(void *args);
void *exeDetectZombie(void *args);
void *exeDetectMobs();
void killPython(void);

int detectZombie(void);
int detectZombie2(void);
int detectMobsDetail(int mode, int ibuf[]);
int detectMobsAbout(int mode, int ibuf[]);
long detectMobsSimple(int mode);
void exePython(void);
