#!/bin/sh
echo "IMU $1 SECS WAIT"
sleep $1
while true; do
        echo "IMU PUBLISHER" > /home/earth/display.txt
        roslaunch bosch_imu_driver imu.launch
        echo "IMU RETRY" > /home/earth/display.txt
        sleep 10
done

$SHELL
