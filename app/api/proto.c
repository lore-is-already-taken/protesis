#include <stdio.h>
#include <pigpio.h>

int main(int argc, char *argv[]){
    // verify correct number of inputs (12)
    if (argc != 13){
        printf("Wrong format while calling the program\n");
        return 1;
    }

    //very correct initialization
    if(gpioInitialise()<0){
        printf("Error while initializating the board\n");
        return 1;
    }

    // SETS PIN TO OUTPUT MODE
    gpioSetMode(*argv[0],PI_OUTPUT);
    gpioSetMode(*argv[2],PI_OUTPUT);
    gpioSetMode(*argv[4],PI_OUTPUT);
    gpioSetMode(*argv[6],PI_OUTPUT);
    gpioSetMode(*argv[8],PI_OUTPUT);
    gpioSetMode(*argv[10],PI_OUTPUT);
    printf("All pins defined\n");

    printf("Initiating motions\n");
    gpioPWM(*argv[0],*argv[1]);
    gpioPWM(*argv[2],*argv[3]);
    gpioPWM(*argv[4],*argv[5]);
    gpioPWM(*argv[6],*argv[7]);
    gpioPWM(*argv[8],*argv[9]);
    gpioPWM(*argv[10],*argv[11]);

    printf("Done!\n");
    return 0;
}
