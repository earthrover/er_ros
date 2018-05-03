#!/bin/sh

d=$(date)
echo "BATTERY $d WAIT $1 SECS"
echo "BATTERY" > /home/earth/display.txt

sleep $1

while true; do
        echo "BATTERY" > /home/earth/display.txt
        #roslaunch earth_rover earth_rover_robot_launch.launch

	screen /dev/serial/by-id/usb-Arduino__www.arduino.cc__Arduino_Mega_2560_740343130393511152C0-if00 57600
        echo "BATTERY RETRY" > /home/earth/display.txt
        sleep 10
done

$SHELL

