#!/bin/sh
echo "PLANNER $1 SECS WAIT"
sleep $1
while true; do
        echo "PLANNER PUBLISHER" > /home/earth/display.txt
        roslaunch earth_rover earth_rover_planner.launch
        echo "PLANNER RETRY" > /home/earth/display.txt
        sleep 10
done

$SHELL
