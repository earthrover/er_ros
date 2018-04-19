#!/bin/sh

d=$(date)
echo "STEERING LOCAL $d"
echo "STEERING LOCAL" > /home/earth/display.txt

sleep 30

while true; do
        echo "STEERING LOCAL" > /home/earth/display.txt
	    roslaunch earth_steering earth_steering.launch
	    roslaunch earth_rover earth_rover_localization.launch
        echo "STEERING LOCAL RETRY" > /home/earth/display.txt
        sleep 1
done

$SHELL