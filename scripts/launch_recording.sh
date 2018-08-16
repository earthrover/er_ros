#!/bin/sh
export DISPLAY=:0
cd /home/earth/Desktop

FILE=~/capture_video.txt

ps cax | grep er-record-playb > /dev/null

if [ $? -eq 0 ]
then
echo "Already capturing"
exit 1
fi

if [ -f $FILE ]
then
echo "Capture data"
sudo su - earth -c "screen -dmS cap -c /home/earth/catkin_ws/src/earth-rover-ros/scripts/.ros.capture.launch.rc"

# cd /home/earth/Desktop/data
# rosbag record --duration=59s -a > /home/earth/Desktop/data/rosbag.log &

#cd /home/earth/Desktop
#./er-record-playback
exit 1
fi

echo "Do not capture data"
