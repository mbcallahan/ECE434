I compiled the 5.10 version of the kernel, but it does not appear to support ethernet over USB, and I did not do much to try to debug this problem.

the makeExample folder contains all the files needed from the make-file tutorial page.

the firstModule conains the first modification to gpio_test we were to make.
the secondModule folder contains the second modification. It has a second switch that toggles two leds at once.

the led folder contains the module for blinking two leds at different rates.

I did not do the etch-a-sketch because figuring out how to read a file from python seemed less interesting than the kernel modules. 