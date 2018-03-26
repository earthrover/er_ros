#!/bin/sh

d=$(date)
echo "LAUNCH ROS $d"
/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh LAUNCH_EARTH_ROVER

for i in `seq 1 10`;
do
    /home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh SYSTEM_LAUNCH_$i
    sleep 1
done    

echo "Boot $d" >> /home/earth/ros_start.log
. /home/earth/.bashrc
roscore &
sleep 10

for i in `seq 1 10`;
do
    /home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh ROS_LAUNCHED_$i
    sleep 1
done

/home/earth/catkin_ws/src/earth-rover-ros/scripts/earth_launch.sh &

for i in `seq 1 10`;
do
    /home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh CONTROL_$i
    sleep 1
done

/home/earth/catkin_ws/src/earth-rover-ros/displays/display_text.sh 

/home/earth/catkin_ws/src/earth-rover-ros/scripts/launch_4ws_joy.sh 
d=$(date)

echo "End $d" >> /home/earth/ros_start.log
