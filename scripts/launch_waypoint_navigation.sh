#!/bin/sh

d=$(date)
echo "LAUNCH ROS $d"

#roslaunch earth_rover earth_rover_joypad_control.launch
roslaunch earth_rover earth_rover.launch

$SHELL

