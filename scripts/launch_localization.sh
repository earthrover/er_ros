#!/bin/sh
echo "Localization $1 SECS WAIT"
sleep $1
while true; do
        echo "Localization" > /home/earth/display.txt
        roslaunch earth_rover_description earth_rover_localization.launch
        echo "Localization RETRY" > /home/earth/display.txt
        sleep 10
done

$SHELL
