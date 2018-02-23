#### EARTH ROVER ROS ####

Notes on our ROS Earth Rover project.
This document contains general information about ROS and how we configure it for ER-UGV

# Common commands:

rosnode list
rosnode info /some_node

rostopic list
rostopic info /some_topic

rostopic echo /some_topic

# Use tab for autocompletion
rostopic pub /some_topic msg/MessageType "data: value" 

# Messages are defined by a .msg format

# Ros master
roscore or roslaunch will start both.

ROS_MASTER_URI is where the master will be.
Master only keeps track of meta information

