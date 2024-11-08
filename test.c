#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    init();
    exePython();
    create_python_thread();
    while(rk){
        
    }
    close_python_thread();
}