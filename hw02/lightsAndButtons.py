#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import time

button0="P9_11"
button1="P9_12"
button2="P9_13"
button3="P9_14"

led0="P9_15"
led1="P9_16"
led2="P9_17"
led3="P9_18"

button2led= {button0:led0,button1:led1,button2:led2,button3:led3}
def updateLeds(channel):
    #print("channel ",channel)
    #tests confirm that the channel variable stores exactly the name
    state=not GPIO.input(channel)#since LEDs are active low, they need to be set to oposite state of buttons
    GPIO.output(button2led[channel],state)

    

#setup LEDs
GPIO.setup(led0, GPIO.OUT)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

#flash the leds for a second
GPIO.output(led0,0)
GPIO.output(led1,0)
GPIO.output(led2,0)
GPIO.output(led3,0)
time.sleep(1)

GPIO.output(led0,1)
GPIO.output(led1,1)
GPIO.output(led2,1)
GPIO.output(led3,1)

GPIO.setup(button0, GPIO.IN, GPIO.PUD_DOWN)#buttons pull high so need pull-down resistors
GPIO.setup(button1, GPIO.IN, GPIO.PUD_DOWN)#buttons pull high so need pull-down resistors
GPIO.setup(button2, GPIO.IN, GPIO.PUD_DOWN)#buttons pull high so need pull-down resistors
GPIO.setup(button3, GPIO.IN, GPIO.PUD_DOWN)#buttons pull high so need pull-down resistors

#set event handlers for every button
GPIO.add_event_detect(button0, GPIO.BOTH, callback=updateLeds)
GPIO.add_event_detect(button1, GPIO.BOTH, callback=updateLeds)
GPIO.add_event_detect(button2, GPIO.BOTH, callback=updateLeds)
GPIO.add_event_detect(button3, GPIO.BOTH, callback=updateLeds)

try:
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print("\nExiting")
    GPIO.cleanup()
finally:
    GPIO.cleanup()
    
