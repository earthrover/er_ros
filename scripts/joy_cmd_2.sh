#!/bin/bash

IR_FILE=~/ir.txt
DEPTH_FILE=~/depth.txt
COLOR_FILE=~/color.txt

if [ -f $IR_FILE ]; then
    rm $IR_FILE
    touch $DEPTH_FILE
    echo "SHOW DEPTH" 
    exit 1
fi


if [ -f $DEPTH_FILE ]; then
    rm $DEPTH_FILE
    touch $COLOR_FILE
    echo "SHOW COLOR"
    exit 1
fi


if [ -f $COLOR_FILE ]; then
    rm $COLOR_FILE
    touch $IR_FILE
    echo "SHOW IR"
    exit 1
fi

touch $DEPTH_FILE
