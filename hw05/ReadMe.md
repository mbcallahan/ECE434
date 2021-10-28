I compiled the 5.10 version of the kernel and I can get it to boot up and go to standby, but it does not appear to support ethernet over USB, and I did not do much to try to debug this problem.

the makeExample folder contains all the files needed from the make-file tutorial page.

the firstModule conains the first modification to gpio_test we were to make.
the secondModule folder contains the second modification. It has a second switch that toggles two leds at once.

the led folder contains the module for blinking two leds at different rates.

The etch-a-sketch sets itself up and runs flask to control left-right and up-down and clears when you "shake" the board by flipping it over. It has the accelerometer polling loop in a seperate task.


I used the name adxl345 to hook it up. When it is connected, the following shows up in iio:device1
0 dev                          0 in_accel_z_calibbias
0 in_accel_sampling_frequency  0 in_accel_z_raw
0 in_accel_scale               0 name
0 in_accel_x_calibbias         0 power
0 in_accel_x_raw               0 sampling_frequency_available
0 in_accel_y_calibbias         0 subsystem
0 in_accel_y_raw               0 uevent

the in_accel files change when acceleration changes. 

# hw05 grading

# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  0/0 | Project 
|  2/2 | Makefile
|  6/6 | Kernel Source
|  4/4 | Etch-a-Sketch
|  8/8 | Kernel Modules: hello, ebbchar, gpio_test, led
|  4/4 | Extras - Blink at different rates
| 24/20 | **Total**

*My comments are in italics. --may*

