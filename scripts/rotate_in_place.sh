#!/bin/bash

FILE=~/rotate.txt

if [ -f $FILE ]; then
	echo "DELETE ROTATE"
	rm $FILE
else
	echo "ROTATE!"
	touch $FILE
fi

