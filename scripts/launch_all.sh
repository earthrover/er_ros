#!/bin/sh

sleep 5
d=$(date)
echo "LAUNCH ROS $d"
echo "LAUNCH EARTH ROVER" > /home/earth/display.txt

roslaunch earth_rover earth_rover_joypad_control.launch
#roslaunch earth_rover earth_rover.launch

echo "ROS RELAUNCH" > /home/earth/display.txt
$SHELL

