#!/bin/sh

d=$(date)
echo "LAUNCH SEGMENTATION $d"

sleep $1

. ~/.bashrc

cd /home/earth/catkin_ws/src/earth-rover-ros-vision/segmentation

while true; do
        echo "EARTH SEG" > /home/earth/display.txt
	python3 segmentation.py
        echo "EARTH SEG RETRY" > /home/earth/display.txt
        sleep 1
done

$SHELL

