#!/bin/sh

sleep 10
echo "RTK Launch" > /home/earth/display.txt
roslaunch earth_rover_rtk rtk.launch

echo "RTK Failed" > /home/earth/display.txt

$SHELL
