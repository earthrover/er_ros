INSTALL
===============

Documentation to install and run earth rover UGV

### Build Status

### Ros modules to install

```
sudo apt-get -y install ros-kinetic-ros-control ros-kinetic-ros-controllers
sudo apt-get -y install ros-kinetic-joint-state-controller 
sudo apt-get -y install ros-kinetic-effort-controllers 
sudo apt-get -y install ros-kinetic-position-controllers
sudo apt-get -y install ros-kinetic-control-toolbox
sudo apt-get -y install ros-kinetic-velocity-controllers
```

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


### Playstation 3 Controller for teleop

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