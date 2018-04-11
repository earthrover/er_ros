INSTALL
===============

Documentation to install and run earth rover UGV

## JETSON - EARTH ROVER - ROS

Install Jetpack 3.2 and CTI patches from Connect Tech Inc.
This will add the support for the Carrier boards

Create User "Earth" with administrator privileges

```
sudo addgroup -a G nvidia,adm,dialout,cdrom,floppy,sudo,audio,dip,video earthadd
```

Enable Universe so we have access to ROS and python
```
sudo add-apt-repository universe
```
 
###### Rename machine
The /etc/hostname file contains just the name of the machine.
Change the name into rover-jetson-XXX

That /etc/hosts has an entry for localhost. It should have something like:

 127.0.0.1    localhost.localdomain localhost
 127.0.1.1    rover-jetson-XXX
 
Enable universe to have access to every package
```
sudo add-apt-repository universe
```

## RASPBERRY PI - EARTH ROVER - ROS

###### Install SYSTEM UBUNTU MATE 16.04 LTS

###### Create user 'earth'

#### Install SSH Server
```
sudo apt-get -y install openssh-server

sudo systemctl enable ssh
sudo service ssh start

sudo service ssh status
```

#### Install screen
We use screen to launch processes and have access to their terminals
later on

```
sudo apt-get -y install screen
```

###### Remove Splash from grub 
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

###### Shutdown 
Disable printer services
```
sudo systemctl disable cups-browsed.service
```

###### Remove all libre office

```
sudo apt-get -y remove --purge libreoffice*
sudo apt-get -y purge --auto-remove scratch

sudo apt-get clean
sudo apt-get autoremove
```

###### Remove modem manager since we need the ACM and USB access
```
sudo apt-get -y remove modemmanager
```

###### Add user to dial up 
```
sudo usermod -a -G dialout $USER
```
Log out to get the group assigned

```
earth@earth-pi-ros:~$ groups
earth adm dialout cdrom sudo dip video plugdev input lpadmin sambashare spi i2c gpio
```

GIT
----------------------------

```
sudo apt-get -y install git
```

ROS
----------------------------

#### Install ROS and Build tools
###### [Installation](http://wiki.ros.org/kinetic/Installation/Ubuntu)

Install Build essentials
------------------------

```
sudo apt-get install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake
sudo rosdep init
rosdep update
```

#### Install Joystick 
```
sudo apt-get -y install jstest-gtk
```

Install Ros modules and tools
-----------------------------

###### [ROS on Raspberry PI](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi)

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

sudo apt-get update
sudo apt-get upgrade
```

Install full kinetic. We will do a better package installation later on.

```
sudo apt-get -y install ros-kinetic-desktop-full
```

###### To compile our controllers we need the controller interface

```
sudo apt-get -y install ros-kinetic-controller-interface ros-kinetic-four-wheel-steering-msgs ros-kinetic-controller-manager
sudo apt-get -y install ros-kinetic-teleop-twist-joy ros-kinetic-jsk-teleop-joy ros-kinetic-joy-teleop
sudo apt-get -y install ros-kinetic-realtime-tools
sudo apt-get -y install ros-kinetic-urdf-geometry-parser

sudo apt-get -y install ros-kinetic-ros-control ros-kinetic-ros-controllers ros-kinetic-control-toolbox ros-kinetic-velocity-controllers
sudo apt-get -y install ros-kinetic-joint-state-controller ros-kinetic-effort-controllers ros-kinetic-position-controllers ros-kinetic-joy
```

Add kinetic to your setup (Check if it is correct)
```
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
```

* ros-kinetic-robot-controllers
See [ros_control](http://wiki.ros.org/ros_control) and [ros_controllers](http://wiki.ros.org/ros_controllers) documentation on ros.org
**"ros_control: A generic and simple control framework for ROS"**,
The Journal of Open Source Software, 2017. ([PDF](http://www.theoj.org/joss-papers/joss.00456/10.21105.joss.00456.pdf))

#### Controllers

Four wheel controller requirements
```
sudo apt-get -y install libevent-pthreads-2.0-5
sudo apt-get -y install python-pthreading
```

Service starter
------------------------


```
earth@earth-pi-ros:~$ sudo vim /etc/init.d/ros_earth_rover
```

We create a launch file to init the service in a screen
```
#!/bin/sh

### BEGIN INIT INFO
# Provides: ros_earth_rover
# Required-Start: $network
# Required-Stop:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: ensure ros daemons are started (nmbd and smbd)
### END INIT INFO

case $1 in
     start)
       su - earth -c "screen -dmS ROS bash --rcfile .bashrc -ci /home/earth/catkin_ws/src/earth-rover-ros/scripts/launch_all.sh"
       ;;
     stop)
        kill -s 15 `pidof screen`
        ;;
esac
exit 0
```

Execute and enable service
```
sudo chmod +x /etc/init.d/ros_earth_rover
sudo systemctl enable ros_earth_rover
```



Development tools
------------------------

#### Install editors
```
sudo apt-get -y install vim astyle
```

#### Install Samba
```
sudo apt-get -y install samba
```

Edit
sudo vim /etc/samba/smb.conf
```
[global]
   allow insecure wide links = yes

[homes]
   follow symlinks = yes
   wide links = yes
   
   browseable = yes
   read only = no
   create mask = 0775
   directory mask = 0775
   valid users = %S
```

```
sudo /etc/init.d/samba restart
sudo smbpasswd -a earth
```

#### Sudoers
Sudo without password for earth user

```
sudo vim /etc/sudoers
```

Add at the bottom of the sudoers file and save
```
%earth ALL=(ALL) NOPASSWD:ALL
```

VNC 
------------------------

#### Install Vnc and GNOME minimal
```
sudo apt-get -y install vnc4server
sudo apt-get -y install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal gnome-themes-ubuntu
```

Create file

```
sudo vim /etc/init.d/vncserver
```

Create the service launcher
```
#!/bin/sh -e
## BEGIN INIT INFO
# Provides:          vncserver
# Required-Start:    networking
# Required-Stop:
# Default-Start:     3 4 5
# Default-Stop:      0 6
## END INIT INFO
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

Make it executable
```
sudo chmod +x /etc/init.d/vncserver
```

Edit the user xstartup
```
mkdir .vnc
vim ~/.vnc/xstartup
```

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

```
sudo update-rc.d vncserver defaults
sudo update-rc.d vncserver enable
```

GITHUB SETUP FOR DEVELOPERS
---------------------------

#### Setup your github credentials
###### [Github Article](https://help.github.com/articles/set-up-git/)

```
git config --global user.name "Bob the Minion"
git config --global user.email "bob@earthrover.cc"
git config --global core.editor vim
```

#### Setup your git certificate
###### [Github with SSH](https://help.github.com/articles/connecting-to-github-with-ssh/)

```
ssh-keygen -t rsa -b 4096 -C "bob@earthrover.cc"
```

#### Add the agent to our user boot

Add ssh agent to bashrc so it autostarts when a terminal is created
```
vim ~/.bashrc
```

Add to the bottom of the file
```
eval $(ssh-agent -s) > /dev/null
```

Add your credentials to ssh for the ssh client to find
```
eval $(ssh-agent -s) 
ssh-add ~/.ssh/id_rsa
```

#### Add SSH key to github
###### [Github add key to account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)

Add your SSH to github and test 

```
ssh git@github.com
```

Something like this should be your output
```
earth@earth-pi-ros:~/catkin_ws/src/earth-rover-ros$ ssh git@github.com
PTY allocation request failed on channel 0
Hi sergioamr! You've successfully authenticated, but GitHub does not provide shell access.
Connection to github.com closed.
```

CLONE EARTH ROVER REPO
---------------------------

###### [Create a ROS workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

```
source /opt/ros/kinetic/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

Run this command to get the environment setup and check that you have the right package parameters
```
source devel/setup.bash
echo $ROS_PACKAGE_PATH
```

#### Add our setup to our main bash so the user has this setup on start
```
echo "source /home/earth/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

#### Clone earth rover repo
```
cd ~/catkin_ws/src
```

#### The repo lives at github here:
###### [Earth Rover ROS modules](https://github.com/earthrover/earth-rover-ros)

```
git clone git@github.com:earthrover/earth-rover-ros.git

cd ~/catkin_ws/src/earth-rover-ros
git submodule init
git submodule update
```
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

###### Create a sym link to scripts to speed up access to launchers
```
ln ~/catkin_ws/src/earth-rover-ros/scripts/ -s scripts
```

Create Eclipse cmake format 
```
cd ~/catkin_ws/
./scripts/catkin_eclipse.sh
```

Enter your ROS workspace.
```
cd ~/catkin_ws
```

#### White list all the packages
```
cd ~/catkin_ws
catkin_make -DCATKIN_WHITELIST_PACKAGES="" -j1
```

#### Build workspace
```
earth@earth-pi-ros:~/catkin_ws$ catkin_make -j1
```

###### We don't have enough memory to run the -j4 compilation so we use -j1
```
catkin_make -j1
```

#### Check with rospack if we can build our packages 
```
rospack profile
```

Troubleshooting
---------------------------

* Joystick connects as player 2

If your joystick is connected as player 2, it means it is mounted as /dev/input/js1
We have to modify our modules to be able to find the remote controller properly

The list of handlers of joysticks are here:
cat /proc/bus/input/devices

We will have to parse later on and create on the fly or search for the joystick.

* Failed to load Kernel modules
```
https://askubuntu.com/questions/779251/what-to-do-after-failed-to-start-load-kernel-modules
```

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

## Playstation 3 Controller for teleop )

At syslog there might be:

```
bluetoothd[487]: Authentication attempt without agent
bluetoothd[487]: Access denied: org.bluez.Error.Rejected
 profiles/input/device.c:ctrl_watch_cb() Device E0:AE:5E:3C:47:2D disconnected
```

[Bluetooth setup](https://wiki.archlinux.org/index.php/Bluetooth_headset)

Use 

```
bluetoothctl
> trust <MAC ADDRESS>
```

Current Mac address of our PS3 controller:
E0:AE:5E:3C:47:2D

## Navigation Stack
[Tutorial](https://www.youtube.com/watch?v=HIK1KBw-Jn4)

* Creating the map

* Saving the map

### Screen setup

We use Screen a lot. 

Here is an example setup for your screen file:
```
vim ~/.screenrc
```

```
# Use bash
shell /bin/bash

autodetach on

# Big scrollback
defscrollback 5000

# No annoying startup message
startup_message off

# Display the status line at the bottom
hardstatus on
hardstatus alwayslastline
hardstatus string "%{.kW}%-w%{.bW}%t [%n]%{-}%+w %=%{..G} %H %{..Y} %Y/%m/%d %c"

# Setup screens
chdir /home/vagrant/Sites # All screens start in ~/Sites folder
screen -t 'server' 0 bash # Make first screen for running server
screen -t 'workspace' 1 bash # Make screen for general work i.e. running git commands
screen -t 'ros'    2 bash # Make screen for general work i.e. running git commands

# Switch to the workspace screen
select 1

vbell off
bell_msg ""

# termcapinfo xterm ti@:te@
termcapinfo xterm 'hs:ts=\E]2;:fs=\007:ds=\E]2;screen\007:ti@:te@'
```

## Ntrip Differential GPS

### Setup
First install pip:
sudo apt-get install python-pip

Then install pyserial:
pip install pyserial

### Config
configure server to use and serial device in /ntrip/config.py

### Usage
Run the python script /ntrip/client.py to stream differential gps data to the ublox over serial. 

## Overloop control
[Tutorial](https://www.youtube.com/watch?v=c-Uy4Kup9RE)

## Indicator IP

sudo apt-add-repository ppa:bovender/bovender
sudo apt-get update
sudo apt-get install indicator-ip

```
indicator-ip --autostart
```

This will install the indicator-ip on the startup applications
add ```indicator-ip -i wlan0```

## Replace text at ubuntu desktop

We can replace the desktop name so we can identify the machine by looking at the name at the desktop
```
cat > /tmp/foo.po
msgid "Ubuntu Desktop"
msgstr "Earth Rover - Network Name"
^D

cd /usr/share/locale/en/LC_MESSAGES
sudo msgfmt -o unity.mo /tmp/foo.po
```

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
