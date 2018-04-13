#!/bin/sh

d=$(date)

FILE=/home/earth/display.txt
text="System Boot"

while true; do
	if [ -f $FILE ]; then
		text=$( cat /home/earth/display.txt )
		rm $FILE
	fi

	ti=$(date +'%H:%M')
		
	#for i in `seq 1 5`;
	#do
		stty -F /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0 19200
		echo \xFE\x58 > /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0
		export IP=$(/sbin/ifconfig wlan0 | grep 'inet addr' | cut -d: -f2 | awk '{print $1}')

		printf "$text \n$ti $IP" > /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0
		echo "$text $ti $IP"
		sleep 1
	#done
done
