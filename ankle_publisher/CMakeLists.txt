cmake_minimum_required(VERSION 2.8.3)
project(ankle_publisher)

find_package(catkin REQUIRED 
			std_msgs
			geometry_msgs
			message_generation
			roslaunch
)

catkin_package(
  CATKIN_DEPENDS 
	std_msgs
	geometry_msgs
)

 install(PROGRAMS scripts/ankle_publisher.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
