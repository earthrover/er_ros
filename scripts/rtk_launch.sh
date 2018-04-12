#!/bin/sh
sleep 25
roslaunch earth_rover_rtk rtk.launch
roslaunch ublox_gps ublox_device.launch node_name:=earth_gps param_file_name:=earth_rover
roslaunch earth_rover_data earth_rover_publisher.launch

$SHELL
