#include <stdio.h>
#include <pigpio.h>

int move(int pin[], int angle[]){
    if(gpioInitialise()<0){
        return 1;
    }

    gpioSetMode(pin[0],PI_OUTPUT);
    gpioSetMode(pin[1],PI_OUTPUT);
    gpioSetMode(pin[2],PI_OUTPUT);
    gpioSetMode(pin[3],PI_OUTPUT);
    gpioSetMode(pin[4],PI_OUTPUT);
    gpioSetMode(pin[5],PI_OUTPUT);

    gpioSetPWMrange(pin[0],180);
    gpioSetPWMrange(pin[1],180);
    gpioSetPWMrange(pin[2],180);
    gpioSetPWMrange(pin[3],180);
    gpioSetPWMrange(pin[4],180);
    gpioSetPWMrange(pin[5],180);

    if(gpioPWM(pin[0],angle[0])!=0){return 1;}
    if(gpioPWM(pin[1],angle[1])!=0){return 1;}
    if(gpioPWM(pin[2],angle[2])!=0){return 1;}
    if(gpioPWM(pin[3],angle[3])!=0){return 1;}
    if(gpioPWM(pin[4],angle[4])!=0){return 1;}
    if(gpioPWM(pin[5],angle[5])!=0){return 1;}

    return 0;
}

float percentage(int angle){
    return (angle/180) + 1;
}
