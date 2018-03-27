Build instructions:

Ubuntu:
1. make ( your cp210x driver )
2. cp cp210x.ko to /lib/modules/<kernel-version>/kernel/drivers/usb/serial
3. insmod /lib/modules/<kernel-version/kernel/drivers/usb/serial/usbserial.ko
4. insmod cp210x.ko