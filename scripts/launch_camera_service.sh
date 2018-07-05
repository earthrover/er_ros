#!/bin/sh
echo "CAMERA SERVICES $1 SECS WAIT"
sleep $1

while true; do
	roslaunch ipc_gps_server gps_listener.launch
	sleep 60
done
$SHELL
