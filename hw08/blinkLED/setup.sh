export TARGET=ledblink.pru0
#configure p9_31 for output gpio 
echo 110 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio110/direction
