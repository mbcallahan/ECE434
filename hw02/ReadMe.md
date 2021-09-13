#Measuring a gpio pin on an Oscilloscope

1.using the togglegpio.sh script, I get a minimum voltage of -70mV and a maximum of 3.37V
2. the frequency with default settings is 4.15 Hz, giving a period of 241ms. this is because the sleep time is for a half period. there is extra delay becaus efile writes take time.about 20% in this case
3. the script is using 19% cpu
4. with a wait time of 0.01, I get 22.7Hz with period 44.1 ms. This uses 96% cpu
5. the period jumped to 46ms when emacs was fully opened. it jumped  alot higher during oppening
6. taking out the debugging features and comments, I get to to 48Hz
7. sh is a little bit faster, it gets 63Hz or 16ms
##python
1. the fastest I can get is 6.4kHz, a period of 155us
2. this uses 100%cpu

##C
1. without modification I can get it to go at 3.2kHz, 310us.
2. with modifications of adding lseek, I can get 195us. This was because I was running X window.
3. turning xwindow off and removing lseek because it is unesscesary, I get 175us. I think this is beacuse it is actually calling sleep while my python is not.
##GPIOD
I get 3.5us period and 289kHz
