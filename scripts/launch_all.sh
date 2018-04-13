#!/bin/sh

d=$(date)
echo "LAUNCH ROS $d"
echo "LAUNCH EARTH ROVER" > /home/earth/display.txt

sleep 5

while true; do
        echo "EARTH ROS" > /home/earth/display.txt
	roslaunch earth_rover earth_rover_joypad_control.launch
        echo "EARTH RETRY" > /home/earth/display.txt
        sleep 1
done

$SHELL

