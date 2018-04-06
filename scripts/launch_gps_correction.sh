#!/bin/sh

d=$(date)
echo "LAUNCH GPS $d"

sleep 15
cd /home/earth/catkin_ws/src/earth-rover-ros/
./displays/display_text.sh GPS_LAUNCH

cd ntrip
python client.py

