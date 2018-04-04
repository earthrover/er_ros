#!/bin/sh

roslaunch ublox_gps ublox_device.launch node_name:=earth_gps param_file_name:=earth_rover

$SHELL
