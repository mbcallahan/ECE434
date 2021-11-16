for the hello.pru0.c code, the command to start the program is:
make TARGET=hello.pru0

the code stops after ten(10) blinks automatically.
however, it can be stopped early with:
make TARGET=hello.pru0 stop

the blinkLED folder contains the setup and make files for section 2.6
everything needs to be run as root and the setup file needs to be sourced. 
when delay_cycles is called with zero, I get a square wave missing many harmonics with a consistent period of 80ns with standard deviation on the order of 200 ps. These measurements are shone in the scope_0 images in the blinkLED folder.

By setting the display to infinite persistence, it seems to show the system to have low jitter except for occasional failures. these are recorded in scope_1

## PWM
The voltage togling with PRU registers is done in the PWM folder. I wrote the code to have symmetric period, but the device does not quite produce that as shown in the scope_2 measurements in that folder. The standard deviation is about .15%, and the jitter is low.

When running the multi-channel scripts, I can get the arm code to change the common memory and get a maximum period of 5.28Mhz when running on both PRUs and using Dr. Yoder's code with a single modification. 

I compile the arm code with gcc pwm7-test.c -o pwm7-test.

The output when I give it a 50% duty cycle is not a stable picture, so scope4 is a single period with the scope set to hold. 

## IO
When an input was directed to control the output and a 300KHz signal was applied, the delay between input and output was about 35ns, or seven cycles. as scope_3 shows



The pins used to do the multi-channel PWM are pins P9_31, P9_29, P8_45 and P8_46. 


# hw08 grading

| Points      | Description |
| ----------- | ----------- |
| 13/14 | PRU
|  2/2 | Controlling the PWM Frequency - optional
|  2/2 | Reading an Input at Regular Intervals - optional
|  2/2 | Analog Wave Generator - optional
| 19/20 | **Total**

*My comments are in italics. --may*


*Your PWM code never turns the pin off.*
