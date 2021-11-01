for the hello.pru0.c code, the command to start the program is:
make TARGET=hello.pru0

the code stops after ten(10) blinks automatically.
however, it can be stopped early with:
make TARGET=hello.pru0 stop

the blinkLED folder contains the setup and make files for section 2.6
everything needs to be run as root and the setup file needs to be sourced. 
when delay_cycles is called with zero, I get a square wave missing many harmonics with a consistent period of 80ns with standard deviation on the order of 200 ps. These measurements are shone in the scope_0 images in the blinkLED folder.

By setting the display to infinite persistence, it seems to show the system to have low jitter except for occasional failures. these are recorded in scope_1

##PWM
The voltage togling with PRU registers is done in the PWM folder. I wrote the code to have symmetric period, but the device does not quite produce that as shown in the scope measurements in that folder. The standard deviation is about .15%, and the jitter is low.


The pins used to do the multi-channel PWM are pins P9_31, P9_29, P8_45 and P8_46. 


