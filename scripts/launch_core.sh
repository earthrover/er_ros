#!/bin/sh

d=$(date)
echo "LAUNCH ROSCORE $d"
echo "LAUNCH CORE" > /home/earth/display.txt
rm /home/earth/.ros/log/* -rfv

while true; do
        echo "EARTH CORE" > /home/earth/display.txt
	roscore
        echo "CORE RETRY" > /home/earth/display.txt
        sleep 1
done

$SHELL

