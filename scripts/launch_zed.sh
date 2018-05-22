#!/bin/sh
echo "ZED $1 SECS WAIT"
sleep $1
while true; do
        echo "ZED CAM" > /home/earth/display.txt
        roslaunch zed_wrapper zed.launch
        echo "ZED RETRY" > /home/earth/display.txt
        sleep 10
done

$SHELL
