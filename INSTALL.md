INSTALL
===============

Documentation to install and run earth rover UGV

### Build Status

### Ros modules to install

sudo apt-get -y install ros-kinetic-ros-control ros-kinetic-ros-controllers
sudo apt-get -y install ros-kinetic-joint-state-controller 
sudo apt-get -y install ros-kinetic-effort-controllers 
sudo apt-get -y install ros-kinetic-position-controllers
sudo apt-get -y install ros-kinetic-control-toolbox
sudo apt-get -y install ros-kinetic-velocity-controllers

* ros-kinetic-robot-controllers
See [ros_control](http://wiki.ros.org/ros_control) and [ros_controllers](http://wiki.ros.org/ros_controllers) documentation on ros.org
**"ros_control: A generic and simple control framework for ROS"**,
The Journal of Open Source Software, 2017. ([PDF](http://www.theoj.org/joss-papers/joss.00456/10.21105.joss.00456.pdf))

### Playstation 3 Controller for teleop

At syslog there might be:

bluetoothd[487]: Authentication attempt without agent
bluetoothd[487]: Access denied: org.bluez.Error.Rejected
 profiles/input/device.c:ctrl_watch_cb() Device E0:AE:5E:3C:47:2D disconnected

https://wiki.archlinux.org/index.php/Bluetooth_headset

Use 
bluetoothctl
with trust E0:AE:5E:3C:47:2D

### Navigation Stack
[Tutorial](https://www.youtube.com/watch?v=HIK1KBw-Jn4)

* Creating the map

* Saving the map

### Overloop control
[Tutorial] (https://www.youtube.com/watch?v=c-Uy4Kup9RE)


