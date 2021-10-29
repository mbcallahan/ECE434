export TARGET=ledblink.pru0
#configure p9_31 for output gpio 
sudo echo 110 > /sys/class/gpio/export
sudo echo out > /sys/class/gpio/gpio110/direction
