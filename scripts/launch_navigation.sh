#!/bin/sh

d=$(date)
echo "NAVIGATION $d"
echo "NAVIGATION" > /home/earth/display.txt

sleep 60

while true; do
        echo "NAVIGATION" > /home/earth/display.txt
	    roslaunch earth_rover earth_rover_planner.launch
	    rosrun earth_rover_navigation earth_rover_nav
        echo "RETRY NAVIGATION" > /home/earth/display.txt
        sleep 1
done

$SHELL