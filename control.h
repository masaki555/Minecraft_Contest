extern int rk;

void attackLeft(void);
void attackLeft_long(void);
void attackRight(void);

void moveDataToFile(char* key);
void initMoveDataFile(void);
void* monitorMoveData(void *arg);
void moveForward(double time);
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
void moveDash(int times);

void init(void);
void setTime(void);
void setMorning(void);
void setSurvival(void);
void setCreative(void);

void cameraCenter(void);
void cameraDown(double time);
void cameraLeft(double time);
void cameraRight(double time);
void cameraUp(double time);
void pushKey(char* key);

int kbhit(void);
void *isInterrupt(void *args);
void *exeDetectZombie(void *args);
void *exeDetectMobs();
void killPython(void);

int detectZombie1(void);
long detectZombie2(void);
int detectZombie3(void);
int detectMobsArray(int mode , int ibuf[]);
int detectMobs(void);
void exePython(void);
