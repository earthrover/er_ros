#!/bin/sh

echo "GPS CORRECTION $1 SECS"
sleep $1
=$(date)
echo "LAUNCH RTK" > /home/earth/display.txt

while true; do
	echo "RTK Launch" > /home/earth/display.txt
	roslaunch earth_rover_rtk rtk.launch

	echo "RTK Failed" > /home/earth/display.txt
        sleep 1
done

$SHELL


$SHELL
