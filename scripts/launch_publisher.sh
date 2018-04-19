#!/bin/sh
echo "GPS PUBLISHER 30 SECS WAIT"
sleep 30
while true; do
        echo "GPS PUBLISHER" > /home/earth/display.txt
	    roslaunch earth_rover_data earth_rover_publisher.launch
        echo "PUBLISHER RETRY" > /home/earth/display.txt
        sleep 10
done

$SHELL
