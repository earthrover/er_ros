stty -F /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0 19200
cat /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0 &


echo \xFE\x58 > /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0
echo "$1" > /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0 


