#File structure
ligtsAndButtons.py uses interrupts to turn on four leds based on the value of four buttons.

sketch.py is the etch-a-sketch, this time using buttons to control the device


#Measuring a gpio pin on an Oscilloscope

1.using the togglegpio.sh script, I get a minimum voltage of -70mV and a maximum of 3.37V
2. the frequency with default settings is 4.15 Hz, giving a period of 241ms. this is because the sleep time is for a half period. there is extra delay becaus efile writes take time.about 20% in this case
3. the script is using 19% cpu
4. with a wait time of 0.01, I get 22.7Hz with period 44.1 ms. This uses 96% cpu
5. the period jumped to 46ms when emacs was fully opened. it jumped  alot higher during oppening
6. taking out the debugging features and comments, I get to to 48Hz. 
7. sh is a little bit faster, it gets 63Hz or 16ms
Matt Hummel found that the shell script runs faster when the comments are removed
##python
1. the fastest I can get is 6.4kHz, a period of 155us
2. this uses 100%cpu, and throttles when oppening an x window

##C
1. without modification I can get it to go at 3.2kHz, 310us.
2. with modifications of adding lseek, I can get 195us. This was because I was running X window.
3. turning xwindow off and removing lseek because it is unesscesary, I get 175us. I think this is beacuse it is actually calling sleep while my python is not.
##GPIOD
I get 3.5us period and 289kHz

##summerizing table
**Script option**|Default shell|fast bash|optomised bash|optomised sh|python|C sysfs unmodified|C lseek|Csysfs fast|GPIOD
------------
**frequency**|4.15Hz|22.7Hz|48Hz|63Hz|6.4kHz|3.2kHz|5.13kHz|5.71kHz|289kHz
---------
**CPU Usage**|19%|96%|100%|100%|100%|98%|100%|100%|not measured



You will have to trust me about the fail2ban. the rest of the demo is in demoVideo.mkv