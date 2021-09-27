#!/bin/bash
#setup the two sensors
echo tmp101 0x4a > /sys/class/i2c-adapter/i2c-2/new_device
echo tmp101 0x49 > /sys/class/i2c-adapter/i2c-2/new_device
#run an infinite loop
while [ "1" = "1" ]; do
    #read temperature probes in centidegrees C
    temp1=`cat /sys/class/i2c-adapter/i2c-2/2-004a/hwmon/hwmon1/temp1_input`
    temp2=`cat /sys/class/i2c-adapter/i2c-2/2-0049/hwmon/hwmon2/temp1_input`

    #use bc to calculate floating point numbers to four places
    temp1=$(echo "scale=4; 1.0*$temp1 / 1000.0"|bc)
    temp2=$(echo "scale=4; 1.0*$temp2 / 1000.0"|bc)

    echo "first temp sensor reads $temp1 C"
    echo "second temp sensor reads $temp2 C"
   
    #wait a second every time
    sleep 1
done
