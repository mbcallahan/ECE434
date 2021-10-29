for the hello.pru0.c code, the command to start the program is:
make TARGET=hello.pru0

the code stops after ten(10) blinks automatically.
however, it can be stopped early with:
make TARGET=hello.pru0 stop

the blinkLED folder contains the setup and make files for section 2.6
everything needs to be run as root.
when delay_cycles is called with zero, I get a square wave missing many harmonics with a consistent period of 80ns with standard deviation on the order of 200 ps. These measurements are shone in the scope_0 images in the blinkLED folder.

By setting the display to infinite persistence, it seems to show the system to have low jitter except for occasional failures. these are recorded in scope_1
