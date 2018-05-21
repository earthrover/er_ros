#!/bin/sh

cd ~/catkin_ws/src
make
cd -

cd ~/catkin_ws
catkin_make
cd -

