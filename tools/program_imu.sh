#!/bin/bash
sudo ./cp210x-program/cp210x-program --read-cp210x
sudo ./cp210x-program/cp210x-program --write-cp210x -m 10C4:EA60 --set-product-string="Earth Rover IMU"

sudo ./cp210x-program/cp210x-program --read-cp210x

