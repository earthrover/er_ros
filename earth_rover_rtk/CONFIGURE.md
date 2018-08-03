Configure ublox 
===============

## Windows setup
(Install U-center for windows:)[https://www.u-blox.com/en/product/u-center-windows]

The ROS node should configure the ublox ok without manually setting anything if not check the rtk input settings this this:

Plug the ublox board directly into pc via usb.
With ublox software configure the incoming RTK. Set the UBX-CFG-PRT message to:
Target: 1-UART1
Protocol In: 5-RTMC3
Protocol out: none 
Baud rate: 115200

## Usb > serial

Change the name of the usb to serial adapter to “Earth Rover GPS”

Use utility from here https://github.com/VCTLabs/cp210x-program 

First read info for the device

cp210x-program --read-cp210x

copy the vendor and product ids it will be something like this:

10C4:EA60


Use them to write a new name to the device

cp210x-program --write-cp210x -m 10C4:EA60 --set-product-string="Earth Rover GPS"

## Configure ublox

The name of the node in the earth_rover.yaml needs to be checked against the actual device name it will be something like

device: /dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_GNSS_receiver-if00

I think that’s all
