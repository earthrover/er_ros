#!/bin/sh

d=$(date)
echo "LAUNCH ROS $d"
/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh LAUNCH_EARTH_ROVER
sleep 60

echo "Boot $d" >> /home/earth/ros_start.log
. /home/earth/.bashrc
roscore &
sleep 10

/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh ROS_LAUNCHED 

/home/earth/catkin_ws/src/earth-rover-ros/scripts/earth_launch.sh &
sleep 20 

/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh JOY_CONTROL

/home/earth/catkin_ws/src/earth-rover-ros/scripts/launch_4ws_joy.sh 
d=$(date)

echo "End $d" >> /home/earth/ros_start.log
