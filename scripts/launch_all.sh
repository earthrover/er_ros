#!/bin/sh

d=$(date)
echo "LAUNCH ROS $d"

echo "Boot $d" >> /home/earth/ros_start.log
. /home/earth/.bashrc
roscore &
sleep 15
/home/earth/catkin_ws/src/earth-rover-ros/scripts/earth_launch.sh &
sleep 30
/home/earth/catkin_ws/src/earth-rover-ros/scripts/launch_4ws_joy.sh 
d=$(date)

echo "End $d" >> /home/earth/ros_start.log
