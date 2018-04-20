#!/bin/sh

d=$(date)
echo "LAUNCH ROS $d WAIT $1 "
echo "LAUNCH EARTH ROVER" > /home/earth/display.txt

sleep $1

while true; do
        echo "EARTH ROS" > /home/earth/display.txt
        roslaunch earth_rover earth_rover_joypad_control.launch
        echo "EARTH RETRY" > /home/earth/display.txt
        sleep 1
done

$SHELL

