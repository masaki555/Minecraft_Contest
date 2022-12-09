extern pid_t pid;
extern int rk;

void attackLeft(void);
void attackRight(void);

void moveForward(double time);
void moveLeft(double time);
void moveRight(double time);
void moveBack(double time);
void moveForwardLeft(double time);
void moveForwardRight(double time);
void moveBackLeft(double time);
void moveBackRight(double time);
void moveSneakForward(double time);
void moveSneakLeft(double time);
void moveSneakRight(double time);
void moveSneakBack(double time);
void moveSneakForwardLeft(double time);
void moveSneakForwardRight(double time);
void moveSneakBackLeft(double time);
void moveSneakBackRight(double time);
void moveSneak(double time);
void moveJump(int times);
void moveDash(double time);
void moveJumpDash(int times);


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
