#!/bin/sh
echo "RTK 60 SECS WAIT"
sleep 60

while true; do
	echo "UBLOX" > /home/earth/display.txt
	roslaunch ublox_gps ublox_device.launch node_name:=earth_gps param_file_name:=earth_rover
	echo "!UBLOX FAILED" > /home/earth/display.txt
	sleep 60
done
$SHELL
