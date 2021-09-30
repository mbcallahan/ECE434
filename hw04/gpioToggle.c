// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Be sure to set -O3 when compiling.
// Modified by Matthew Callahan  26-Sept-2021
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 

#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/

int main(int argc, char *argv[]) {
    volatile void *gpio_addr;
    volatile unsigned int *gpio_oe_addr;
    volatile unsigned int *gpio_setdataout_addr;
    volatile unsigned int *gpio_cleardataout_addr;
    unsigned int reg;
    

	int fd = open("/dev/mem", O_RDWR);//open memory device to let mmap look

    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);

    gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);//find the gpio1 registers in virtual memory

    gpio_oe_addr           = gpio_addr + GPIO_OE;//output enable register
    gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;

    if(gpio_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO mapped to %p\n", gpio_addr);
    printf("GPIO OE mapped to %p\n", gpio_oe_addr);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr);

    // Set P9_15 to be an output pin
    reg = *gpio_oe_addr;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~P9_15;       // Set P9_15 bit to 0 for output
    *gpio_oe_addr = reg;
    printf("GPIO1 configuration: %X\n", reg);

    printf("Start toggling P9_15 as fast as possible\n");
    while(keepgoing) {
        // printf("ON\n");
        *gpio_setdataout_addr = P9_15;
        //usleep(250000);
        // printf("OFF\n");
        *gpio_cleardataout_addr = P9_15;
        //usleep(250000);
    }
    //yeilds 2.94MHz

    munmap((void *)gpio_addr, GPIO1_SIZE);
    close(fd);
    return 0;
}
