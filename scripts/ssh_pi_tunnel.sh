#!/bin/sh

d=$(date)
echo "SSH $d WAIT $1"

sleep $1

	echo "TUNNEL ROS SERVER     into ENGINEER.BLUE 12311"	
	autossh -M 0 -fTNv -R 12311:localhost:11311 earth_rover@engineer.blue 
	sleep 1
	echo "TUNNEL HTTP 80        into ENGINEER.BLUE 12380"
	autossh -M 0 -fTNv -R 12380:localhost:80 earth_rover@engineer.blue
	sleep 1
	echo "TUNNEL SSH 22         into ENGINEER.BLUE 12322"
	autossh -M 0 -fTNv -R 12322:localhost:22 earth_rover@engineer.blue 

	echo "TUNNEL OUR VNC SERVER into JETSON 15900"
	autossh -M 0 -fTNv -R 15900:localhost:5900 earth@192.168.0.25

	echo "TUNNEL OUR SSH     22 into JETSON 122"
	autossh -M 0 -fTNv -R 122:localhost:22 earth@192.168.0.25

$SHELL

