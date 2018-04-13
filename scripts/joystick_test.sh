#!/bin/sh

d=$(date)
echo "JOY TEST $d"

echo "JOYSTICK INIT" > /home/earth/display.txt

while true; do
	/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh JOYSTICK_ON
	jstest /dev/input/js0
	for i in `seq 1 5`;
	do
	    echo "CHECK JOYSTICK" > /home/earth/display.txt
	    sleep 10
	done
done
