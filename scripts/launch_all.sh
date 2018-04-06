#!/bin/sh

sleep 5
d=$(date)
echo "LAUNCH ROS $d"
/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh LAUNCH_EARTH_ROVER

roslaunch earth_rover earth_rover_joypad_control.launch
#roslaunch earth_rover earth_rover.launch

/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh REBOOT 

$SHELL

