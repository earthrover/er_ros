#!/bin/sh

d=$(date)
echo "LAUNCH ROBOT $d WAIT $1 SECS"
echo "LAUNCH ROBOT" > /home/earth/display.txt

sleep $1

while true; do
        echo "EARTH ROBOT" > /home/earth/display.txt
	roslaunch earth_rover earth_rover_robot_launch.launch
        echo "ROBOT RETRY" > /home/earth/display.txt
        sleep 1
done

$SHELL

