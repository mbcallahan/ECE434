#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import time

button0="P9_9"
button1="P9_10"
button2="P9_11"
button3="P9_12"

led0="P9_13"
led1="P9_14"
led2="P9_15"
led3="P9_16"

def updateLeds(channel):
    print("channel ",channel)
    

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
