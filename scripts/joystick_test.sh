#!/bin/sh

d=$(date)
echo "JOY TEST $d"
/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh JOYSTICK_TEST

while true; do
	/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh JOYSTICK_ON
	jstest /dev/input/js0
	for i in `seq 1 5`;
	do
	    /home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh JOYSTICK_$i
	    sleep 1
	done
done
