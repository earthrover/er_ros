#!/bin/sh

d=$(date)
echo "NAVIGATION $d"
echo "NAVIGATION" > /home/earth/display.txt

sleep $1

while true; do
        echo "NAVIGATION" > /home/earth/display.txt
        roslaunch earth_rover earth_rover_navigation.launch
        echo "RETRY NAVIGATION" > /home/earth/display.txt
        sleep 1
done

$SHELL
