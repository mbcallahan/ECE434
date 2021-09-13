#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
#use same pin as shell
togglepin="P9_12"

    

#setup LEDs
GPIO.setup(togglepin, GPIO.OUT)
#first attemput will use a variable. will try using magic constants to see if that is faster
try:
    while True:
        GPIO.output(togglepin,0)
        GPIO.output(togglepin,1)
        
except KeyboardInterrupt:
    print("\nExiting")
    GPIO.cleanup()
finally:
    GPIO.cleanup()
    
