stty -F /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0 19200
cat /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0 &


echo \xFE\x58 > /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0
#echo "$1" > /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0 

export IP=$(/sbin/ifconfig wlan0 | grep 'inet addr' | cut -d: -f2 | awk '{print $1}')

echo $IP
if [ -z "$1" ]
then
	echo "$IP" >> /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0 
else
	echo "$1" >> /dev/serial/by-id/usb-MO_LK202-25-USB_0df1XRw1-if00-port0
fi

