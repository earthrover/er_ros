#!/bin/sh

d=$(date)
echo "SSH $d WAIT $1"

sleep $1

	echo "TUNNEL ROS CORE into ENGINEER.BLUE 11311"	
	autossh -M 0 -fTNv -R 11311:localhost:11311 earth_rover@engineer.blue 
	sleep 1

	echo "TUNNEL HTTP 80  into ENGINEER.BLUE 11380"	
	autossh -M 0 -fTNv -R 11380:localhost:80 earth_rover@engineer.blue
	sleep 1

	echo "TUNNEL SSH 22   into ENGINEER.BLUE 11322"	
	autossh -M 0 -fTNv -R 11322:localhost:22 earth_rover@engineer.blue 

$SHELL



