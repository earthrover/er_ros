#!/bin/sh

d=$(date)
echo "SSH $d WAIT $1"

sleep $1

	echo "CONNECTING SSH"	
	autossh -M 0 -fTNv -R 11311:localhost:11311 earth_rover@engineer.blue 
	sleep 1
	echo "SSH 2"
	autossh -M 0 -fTNv -R 11380:localhost:80 earth_rover@engineer.blue
	sleep 1
	echo "SSH 3"
	autossh -M 0 -fTNv -R 11322:localhost:22 earth_rover@engineer.blue 

$SHELL



