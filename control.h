extern pid_t pid;
extern int rk;

void attackLeft(void);
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

int detectZombie(void);
int detectZombie2(void);
/*int detectMobs(int mode, int ibuf[]);*/
int detectMobsArray(int mode , int ibuf[]);
long detectMobs(int mode);
void exePython(void);
