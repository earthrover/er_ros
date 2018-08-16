#!/bin/bash

# Start ssh agent
eval SSH_AUTH_SOCK=/tmp/ssh-z0zKhqhkLVzh/agent.8920; export SSH_AUTH_SOCK;
SSH_AGENT_PID=8921; export SSH_AGENT_PID;
echo Agent pid 8921; > /dev/null

# Activate ROS workspace
source /opt/ros/kinetic/setup.bash
source /home/earth/catkin_ws/devel/setup.bash

echo -e "\e[32mEarth Rover CAMERA ROVER 002\e[0m"
hostname -I
export ROS_IP=192.168.8.10
export ROS_HOSTNAME=rover_002
export ROS_PARALLEL_JOBS=-j4
export ROS_MASTER_URI=http://rover_002:11311/
export DISPLAY=:0

cd /home/earth/Desktop/data
/opt/ros/kinetic/bin/rosbag record --duration=59s -a
#$SHELL
