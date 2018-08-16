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
./er-record-playback
exit 1
fi

echo "Do not capture data"
