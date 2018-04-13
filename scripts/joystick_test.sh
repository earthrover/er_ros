#!/bin/sh

d=$(date)
echo "JOY TEST $d WAIT 10 SECS"

echo "JOYSTICK INIT" > /home/earth/display.txt
sleep 10

file=/dev/input/js0
while true; do
	if [ -e "$file" ]; then
		echo "JOYSTICK OK"
		echo "JOYSTICK OK" > /home/earth/display.txt
		jstest /dev/input/js0
	else
	    echo "CHECK JOYSTICK" > /home/earth/display.txt		
	    echo "CHECK JOYSTICK"
	    sleep 10
	fi
done
