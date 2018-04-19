#!/bin/sh
echo "IMU 20 SECS WAIT"
sleep 20
while true; do
        echo "IMU PUBLISHER" > /home/earth/display.txt
	roslaunch bosch_imu_driver imu.launch
        echo "IMU RETRY" > /home/earth/display.txt
        sleep 10
done

$SHELL
