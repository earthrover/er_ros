INSTALL
===============

Documentation to install and run earth rover UGV

### RASPBERRY PI - EARTH ROVER - ROS ###

Failed to load Kernel modules
```
https://askubuntu.com/questions/779251/what-to-do-after-failed-to-start-load-kernel-modules
```

######################## SYSTEM UBUNTU MATE 16.04 LTS ######################

# Create user 'earth'

# Install SSH Server
```
sudo apt-get -y install openssh-server

sudo systemctl enable ssh
sudo service ssh start

sudo service ssh status
```

# Remove Splash from grub 
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

Remove all libre office

sudo apt-get -y remove --purge libreoffice*
sudo apt-get -y purge --auto-remove scratch

sudo apt-get clean
sudo apt-get autoremove

################################# ROS ###################################
### Install ROS and Build tools
# http://wiki.ros.org/kinetic/Installation/Ubuntu

# Install Joystick 
```
sudo apt-get -y install jstest-gtk
```

sudo apt-get -y install git

# http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

sudo apt-get update
sudo apt-get upgrade

# Install Build essentials
sudo apt-get install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake
sudo rosdep init
rosdep update

# Install Ros modules and tools
sudo apt-get -y install ros-kinetic-desktop-full

# To compile our controllers we need the controller interface
```
sudo apt-get -y install ros-kinetic-controller-interface ros-kinetic-four-wheel-steering-msgs ros-kinetic-controller-manager
sudo apt-get -y install ros-kinetic-teleop-twist-joy ros-kinetic-jsk-teleop-joy ros-kinetic-joy-teleop
sudo apt-get -y install ros-kinetic-realtime-tools
sudo apt-get -y install ros-kinetic-urdf-geometry-parser

sudo apt-get -y install ros-kinetic-ros-control ros-kinetic-ros-controllers ros-kinetic-control-toolbox ros-kinetic-velocity-controllers
sudo apt-get -y install ros-kinetic-joint-state-controller ros-kinetic-effort-controllers ros-kinetic-position-controllers
```

echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc

* ros-kinetic-robot-controllers
See [ros_control](http://wiki.ros.org/ros_control) and [ros_controllers](http://wiki.ros.org/ros_controllers) documentation on ros.org
**"ros_control: A generic and simple control framework for ROS"**,
The Journal of Open Source Software, 2017. ([PDF](http://www.theoj.org/joss-papers/joss.00456/10.21105.joss.00456.pdf))

# Controllers

Four wheel controller requirements
```
sudo apt-get -y install libevent-pthreads-2.0-5
sudo apt-get -y install python-pthreading
```

###########################################################
### Development tools ###

# Install editors
```
sudo apt-get -y install vim astyle
```

# Install Samba
```
sudo apt-get -y install samba
```

Edit
sudo vim /etc/samba/smb.conf
```
[homes]
   follow symlinks = yes
   wide links = yes
   browseable = yes
   read only = no
   create mask = 0775
   directory mask = 0775
   valid users = %S
```

sudo /etc/init.d/samba restart
sudo smbpasswd -a earth

### Sudoers
Sudo without password for earth user

sudo vim /etc/sudoers

Add at the bottom
```
%earth ALL=(ALL) NOPASSWD:ALL
```

################################# VNC ###################################
# Install Vnc and GNOME minimal
sudo apt-get -y install vnc4server
sudo apt-get -y install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal gnome-themes-ubuntu

/etc/init.d/vncserver
```
#!/bin/sh -e
### BEGIN INIT INFO
# Provides:          vncserver
# Required-Start:    networking
# Required-Stop:
# Default-Start:     3 4 5
# Default-Stop:      0 6
### END INIT INFO
PATH="$PATH:/usr/X11R6/bin/"

# The Username:Group that will run VNC
export USER="nvidia"
#${RUNAS}

# The display that VNC will use
DISPLAY="1"

# Color depth (between 8 and 32)
DEPTH="16"

# The Desktop geometry to use.
#GEOMETRY="<WIDTH>x<HEIGHT>"
#GEOMETRY="800x600"
GEOMETRY="1280x768"
#GEOMETRY="1920x1080"

# The name that the VNC Desktop will have.
NAME="my-vnc-server"

OPTIONS="-name ${NAME} -depth ${DEPTH} -geometry ${GEOMETRY} :${DISPLAY}"

. /lib/lsb/init-functions

case "$1" in
        start)
                log_action_begin_msg "Starting vncserver for user '${USER}' on localhost:${DISPLAY}"
                su ${USER} -c "/usr/bin/vncserver ${OPTIONS}"
        ;;

        stop)
                log_action_begin_msg "Stoping vncserver for user '${USER}' on localhost:${DISPLAY}"
                su ${USER} -c "/usr/bin/vncserver -kill :${DISPLAY}"
        ;;

        restart)
                $0 stop
                $0 start
        ;;
esac

exit 0
```
sudo chmod +x /etc/init.d/vncserver

~/.vnc/xstartup
```
#!/bin/sh

export XKL_XMODMAP_DISABLE=1
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey
vncconfig -iconic &

gnome-panel &
gnome-settings-daemon &
metacity &
nautilus &
gnome-terminal &
xterm &
```

sudo update-rc.d vncserver defaults
sudo update-rc.d vncserver enable

################################ GITHUB SETUP FOR DEVELOPER #################################
### 

# Setup your github credentials
# https://help.github.com/articles/set-up-git/

git config --global user.name "Bob the Minion"
git config --global user.email "bob@earthrover.cc"
git config --global core.editor vim

# Setup your git certificate
# https://help.github.com/articles/connecting-to-github-with-ssh/
ssh-keygen -t rsa -b 4096 -C "bob@earthrover.cc"

# Add the agent to our user boot
vim ~/.bashrc
```
eval $(ssh-agent -s) > /dev/null
```

ssh-add ~/.ssh/id_rsa

# Add SSH key to github
# https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

Add your SSH to github and test 

ssh git@github.com

################################# CLONE EARTH ROVER REPO ###################################
### 

# Create a ros workspace
# http://wiki.ros.org/catkin/Tutorials/create_a_workspace

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

source devel/setup.bash
echo $ROS_PACKAGE_PATH

# Add our setup to our main bash so the user has this setup on start
echo "source /home/earth/catkin_ws/devel/setup.bash" >> ~/.bashrc

### Clone earth rover repo
cd ~/catkin_ws/src

# The repo lives at github here:
# https://github.com/earthrover/earth-rover-ros

git clone git@github.com:earthrover/earth-rover-ros.git

cd /catkin_ws/src/earth-rover-ros
git submodule init
git submodule update

A result similar to this:
```
earth@earth-pi-ros:~/catkin_ws/src/earth-rover-ros$ git submodule init
Submodule 'earth_rover_description' (git@github.com:earthrover/earth_rover_description.git) registered for path 'earth_rover_description'
Submodule 'four_wheel_steering_msgs' (git@github.com:ros-drivers/four_wheel_steering_msgs.git) registered for path 'four_wheel_steering_msgs'
Submodule 'jrk_hardware' (git@github.com:sergioamr/jrk_hardware.git) registered for path 'jrk_hardware'
Submodule 'serial' (git@github.com:wjwwood/serial.git) registered for path 'serial'
Submodule 'teleop_twist_joy' (git@github.com:RALSpaceASG/teleop_twist_joy.git) registered for path 'teleop_twist_joy'
Submodule 'twist_mux' (https://github.com/ros-teleop/twist_mux) registered for path 'twist_mux'
Submodule 'ublox' (git@github.com:earthrover/ublox.git) registered for path 'ublox'
Submodule 'urdf_geometry_parser' (git@github.com:ros-controls/urdf_geometry_parser.git) registered for path 'urdf_geometry_parser'
Submodule 'zed-ros-wrapper' (git@github.com:earthrover/zed-ros-wrapper.git) registered for path 'zed-ros-wrapper'
earth@earth-pi-ros:~/catkin_ws/src/earth-rover-ros$
```

cd ~/catkin_ws

# Create a sym link to scripts to speed up access to launchers
ln ~/catkin_ws/src/earth-rover-ros/scripts/ -s scripts

# Build workspace
# earth@earth-pi-ros:~/catkin_ws$ catkin_make -j1

# We don't have enough memory to run the -j4 compilation
catkin_make -j1

# Check with rospack if we can build our packages 
rospack profile

###########################################################
### Troubleshooting ###

* My PS3 Joystick flashes and goes blank.

If your Pi was very busy doing something, it might be that the pairing will fail and you will have to reset the bluetooth interface

check on dmesg to see if there was something similar to this:
```
[  188.127222] input: PLAYSTATION(R)3 Controller as /devices/platform/soc/3f201000.uart/tty/ttyAMA0/hci0/hci0:11/0005:054C:0268.0001/input/input0
[  188.127644] sony 0005:054C:0268.0001: input,hidraw0: BLUETOOTH HID v1.00 Joystick [PLAYSTATION(R)3 Controller] on b8:27:eb:71:8d:75
[  203.526671] Bluetooth: hci0: Frame reassembly failed (-84)
[  203.526706] Bluetooth: hci0: Frame reassembly failed (-84)
[  203.526719] Bluetooth: hci0: Frame reassembly failed (-84)
[  203.526854] Bluetooth: hci0: Frame reassembly failed (-84)
[  203.526948] Bluetooth: hci0: Frame reassembly failed (-84)
[  203.527030] Bluetooth: hci0: Frame reassembly failed (-84)
[  203.594543] Bluetooth: hci0: Frame reassembly failed (-84)
[  203.594554] Bluetooth: hci0 ACL packet for unknown connection handle 326
[  203.594581] Bluetooth: hci0: Frame reassembly failed (-84)
[  217.364844] Bluetooth: hci0: Frame reassembly failed (-84)
```

Reset the bluetooth service:
sudo /etc/init.d/bluetooth restart

If you get the Player 1 interface on... you are good to go.

### Playstation 3 Controller for teleop )

At syslog there might be:

```
bluetoothd[487]: Authentication attempt without agent
bluetoothd[487]: Access denied: org.bluez.Error.Rejected
 profiles/input/device.c:ctrl_watch_cb() Device E0:AE:5E:3C:47:2D disconnected
```
[Bluetooth setup] (https://wiki.archlinux.org/index.php/Bluetooth_headset)

Use 

```
bluetoothctl
> trust <MAC ADDRESS>
```

Current Mac address of our PS3 controller:
E0:AE:5E:3C:47:2D

### Navigation Stack
[Tutorial](https://www.youtube.com/watch?v=HIK1KBw-Jn4)

* Creating the map

* Saving the map

### Overloop control
[Tutorial](https://www.youtube.com/watch?v=c-Uy4Kup9RE)

```
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------+ossssso+:----------/////::---------------------------------------------------
----------------------smdmdmNmyy+/::///ymdmNmmmmmmdh/:+/--------------------------------------------
-----------------------s:ymmmmo::/:----dNmdNmmmmmmNmm+++:://////osyyysoo+/--------ohhysssso++-------
----------------------:+--dmmmdyo::/::+mmddddmNNNNNNNh/:::----:sdddhhhhhdy-----syodmmmNNNmmmdd:-----
----------------------:+-:dddodmdo/:/yydmmNNNNNmmddhyssssssssyyyoydddms:s/---:/NmdmNmmmmdmNmmNh+----
--------:--yyyysso++/://-/ddy-:dmdo-/hmhmmmdhyysssssssssssyhhyyhmmmmmd//yyyyyydmmmdddmmNmmNNNNmd+---
-------hhsyNNNNNmmmmddh/-odmo--:dmdo+hhyysssssssssssysyyhdddddmNNmmmdddddyddmmmmmmNNNmmNNNNNNNNNy---
....--/mmmmmddmmmmNNNmNo:sdm//+osyssssssssssssssyyyhmmdmmmmmmmmmmmmmdddmmymmNmmmNNmmhdmNNmddmNNNs---
...-/+ddhddmmmmNmNNNNNmhyyhdsddddhhhhhhhhhhyhhddddmmmmNNmmmmmmmmmmmmdddmNydNNNNNNNmmmmNNdhyyymmNmo--
.../hhmmmmmmdmmNNNNNNhyssss+/ydmdddddddddmdhddmNNddmmmmmmdmmmmmNmdmmmddmdshmNNNNmmNmmNNmhyyyyhNNNy--
...:mmdmNmdddmNNNNmNNhhyyyysoydmmdddddy:/yyssyhmmmdddddmmmmmNNNNmddmmddddyhmNNNNNNNmmNNmyyyyyhNNm:--
...ymmNNmmmmNNNNmdmNmdmddddddddmmmmddmdhyhyyddmmddmmNmmmmNNNNNNNNNNmmmddmyhNNNNNNNNNmNNdyyyyyhmNh---
.-ymmmmmmmmdmNNNdmmmNmNNNNNhyyddmmmmmdhhddddmmmmNNNmdhdmNNNmmmmNNNNmmmmmNNmNNNNNNNNNNNNmhyyyymmNm---
./mmmNNNNmddmNNdmmdhhhddmNNyyyddmmmmmdyymNNNNNmmNNmmdmmNNmhyyyhmmNNmdhmmmNNNddmNNNNmmNNNhyyhdmNmh---
.-smmmNNNNmmNNNdNmddddddmNNhyyddmmNmNmyydmNNNNNNNmmdmmmNNhyyyyyhNNNNs/dmmNNdo+yNNNNNmmNNNmdmmNNo-...
..oNNmNNNNmNNNNdmNmmmmmmmmdoyyhdmmNNmmyydmNmNNmmmNNmdmNNmyyyyyyyNNNd/.-:+hmdysmNNNNNNNNNNNNNNNd-....
.-dNNNNmmmmmmNNmdmNNmmNNNNhhyydhmmmmmdyydmNmmNNNNNNmmmNNdyyyyyyyNNNo....-::+oo+mNNNNNNmNNNNNNmh--...
.-dNNNmNNNNmmNNNmdmdmNNNds/ossyssooosyyyhNNNmmmNNNNNmNmNdyyyyyyhmNNs--:::::::oymNNNNNNNNNNNNNmdhyo:-
../ymNNNNNNNNNNNNNNNNNNm:------.....-+ooshhmNNNNNNmmNmNNmyyyyyymmNNmosssooosyyddmNmNNNNNNNNmmdy+:-..
...-hNNNNNNmNNNNNNNNNNNhooo++oooo+///:::--/mNNNNmmmmmmNNNdhyyhmmNNdyo/:-...--/ohmNNNNNNmdhs+:-......
...-sdmNNNNNNNNNNNNNNNNy++/:...---:/+ossyyhmNNNmNNNNmmmNNNmmmmmNNy-........:+osyyhhhhyo/-...........
....-oydmmNNNNNNNNNNmmmdhs+:.....--/oshdmmmmmmmNNNNNNNNNNNNmmNNNNo+++//::------.....................
......-/hmmNNNNmmNmmdddyssoo+++syhdmmmmmmmmmmhmNNNNNmmNmNNmmmNNdm/////+osyhhhyyo:...................
...:+shdmmmmmddhs+:---::::::/+oo+/::+yhdddmmmdhdmNNNNNNNNNNNNNmmmmdho:.....---......................
...-::///+++/:-........................-:::/+ssyhdmmmNNNNNNNNmdho/-.................................
............................................-:+shmmmmmmmmmhs+:-.....................................
...........................................-/osyyhdddhs+:-..........................................
....................................................................................................
....................................................................................................
```