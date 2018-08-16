#!/bin/bash

FILE=~/capture_video.txt

if [ -f $FILE ]
then

echo "DELETE RECORDING"
rm $FILE
killall -9 er-record-playback
else

echo "RECORD"
touch $FILE
cd ~/Desktop
./launch_recording.sh

fi

