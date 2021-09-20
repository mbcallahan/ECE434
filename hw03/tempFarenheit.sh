#!/bin/bash
#run an infinite loop
while [ "1" = "1" ]; do
    #read from the integer part of the temperature value
    cells1=`i2cget -y 2 0x48`
    cells2=`i2cget -y 2 0x49`
    #convert to farenheit
    fer1=$(( (cells1*9)/5+32))
    fer2=$(( (cells2*9)/5+32)) 

    #print values with a new line each time so there is a record
    echo "first temp sensor reads $fer1 F"
    echo "second temp sensor reads $fer2 F"
    #wait a second every time
    sleep 1
done
