#!/bin/sh

d=$(date)
echo "STEERING LOCAL $d WAIT $1"
echo "STEERING LOCAL" > /home/earth/display.txt

sleep $1

while true; do
        echo "STEERING LOCAL" > /home/earth/display.txt
	    roslaunch earth_steering earth_steering.launch
        echo "STEERING LOCAL RETRY" > /home/earth/display.txt
        sleep 1
done

$SHELL
