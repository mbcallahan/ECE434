#!/usr/bin/python3
#this is supposed to read the temp sensors, configure an intterupt, and resond to the interrupt.

import smbus
import Adafruit_BBIO.GPIO as GPIO
import time

bus=smbus.SMBus(2)#pull from ic2 bus 2
address0=0x48
address1=0x49
intPin='P9_12'
def cToF(temp):
    return 5*temp/9+32
def tempInt(temp):
    print("\t\tTemperature Intterupt!!!!!!!!!!!")

#configyre high and low temp ranges for intterupt. make them acheivable
bus.write_byte_data(address0, 2,20)
bus.write_byte_data(address0, 3,24)

bus.write_byte_data(address1, 2,20)
bus.write_byte_data(address1, 3,24)
GPIO.setup(intPin,GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(intPin, GPIO.FALLING, callback=tempInt)#use falling edge becase intterupt is active low


while True:
    print("probe 1 reads %f F, probe 2 reads %f F" % (cToF(bus.read_byte_data(address0,0)),cToF(bus.read_byte_data(address1,0))))
    time.sleep(2)
