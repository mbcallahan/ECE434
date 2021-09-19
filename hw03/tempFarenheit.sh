#!/bin/bash

while [ "1" = "1" ]; do
    cells1=`i2cget -y 2 0x48`
    cells2=`i2cget -y 2 0x49`

    fer1=$(( (cells1*9)/5+32))
    fer2=$(( (cells2*9)/5+32)) 


    echo "first temp sensor reads $fer1 F"
    echo "second temp sensor reads $fer2 F"
    sleep 1
done
