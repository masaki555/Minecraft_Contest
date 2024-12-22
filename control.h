extern int rk;

void init(void);
void exePython(void);
int detectPlayer1(void);
int detectPlayer2(void);

void attackLeft(void);
void attackLeft_long(void);
void attackLeft_continuous(int n);
void eat(int n);
void downKey(char* key);
void upKey(char* key);
void pushKey(char* key);
void sleep_time(double time);

void moveForward(double time);
void moveLeft(double time);
void moveRight(double time);
void moveBack(double time);
void moveForwardLeft(double time);
void moveForwardRight(double time);
void moveBackLeft(double time);
void moveBackRight(double time);
void moveJump(int times);
void moveDash(int times);
void setDash(void);
void resetDash(void);

void cameraDown(double time);
void cameraLeft(double time);
void cameraRight(double time);
void cameraUp(double time);

void setTime(void);
void setMorning(void);
void setSurvival(void);
void setCreative(void);

int detectZombie1(void);
long detectZombie2(void);

void create_python_thread(void);
void close_python_thread(void);

void create_python_thread2(void);
void close_python_thread2(void);
