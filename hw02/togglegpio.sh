#!/bin/sh

GPIO=$1
PERIOD=$2

cleanup() { # Set the GPIO port to 0
  echo 0 > /sys/class/gpio/gpio${GPIO}/value
  echo "Cleaning up"
  echo ""
  exit
}
if [ ! -e /sys/class/gpio/gpio$GPIO ]; then
    echo "$GPIO" > /sys/class/gpio/export
fi
echo "out" > /sys/class/gpio/gpio${GPIO}/direction

trap cleanup SIGINT # call cleanup on Ctrl-C

THIS_VALUE=0
NEWLINE=0

# Read forever

while [ "1" = "1" ]; do
  if [ "1" = "$THIS_VALUE" ]; then
    THIS_VALUE=0
   else
     THIS_VALUE=1
  fi
  echo $THIS_VALUE > /sys/class/gpio/gpio${GPIO}/value
  sleep $PERIOD
done
cleanup # call the cleanup routine

