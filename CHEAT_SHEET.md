EARTH ROVER CHEAT SHEET
=======================

```
                        `.-:::--.`                         
                   -+shmMMNmmddmmNMNmho/.                   
        `..`   `+hNMds/-.         `.:+ymMmy:                
     `yyo++osddMms:                     `/yNNy-             
     yo    +mMy:                         `./dMMdyssssso-    
     oy  -dMy.                     `-+ssso+:.`:mMy`   .ys   
      ho+MN:                  `:osso/.          oMm-   +h   
      `mMd`               ./sys/.                :NN: /d`   
      +Mmd-           `/syo-                      :MNhs`    
     `NM-.hs`      :syo:                           sMh      
     oMh   :ho``/yy+.                              `MM.     
     hM+    `yNN/`                                  dM+     
     dM/  -sy/`/ho`                                 hMo     
     hMo/ho.     :yy-                               dM/     
     +MM/          .oh/`                           .MM.     
    :dNM/             :yy:                         yMy      
   sy`:MN.              `+ys-                     +Mm`      
  oh   /MN-                .+ys-                 +MNy       
  oy`   :NM+                  .+ys/`           `hMd.ys      
   /sssssyNMm:                   `:sys:`     `oNN+   m-     
           -hMm+`                    `:oss+:sNNs`   `m:     
             .sNMh+.                   `:sNMdyysssssy:      
                -odMNhs+:-.`    `.-/oydMNh+.                
                   `-+shdNMMMMMMMNmdyo/.                    
                           `````                            
                            ``                              
      ydsssss`     hm`     ydssh/  `sssmdsss  +h      :d    
      yo          yhod`    ys  .M.     ho     +h      /m    
      yh+++:     od` sh    ys:oho      ho     +m++++++ym    
      ys...`    +m`   hy   ys.sh:      ho     +d......+m    
      yy::::-  :m.    `do  ys  .sh:    ho     +h      /m    
                                                            
```

Useful commands to run and debug

### [Ros Cheat Sheet](https://github.com/ros/cheatsheet/releases)

### General 

* Version release of the Jetpack installed
```
nvidia@earth-jetson:~$ head -1 /etc/nv_tegra_release 
# R28 (release), REVISION: 2.0, GCID: 10136452, BOARD: t186ref, EABI: aarch64, DATE: Fri Dec  1 14:20:33 UTC 2017
```

* Kernel running on device
```
root@earth-jetson:~# uname -a
Linux earth-jetson 4.4.38 #2 SMP PREEMPT Tue Feb 20 12:30:46 UTC 2018 aarch64 aarch64 aarch64 GNU/Linux
```

* Rospack 

List of packages
```
nvidia@earth-jetson:~$ rospack list | grep earth
ankle_publisher /home/nvidia/catkin_ws/src/earth-rover-ros/ankle_publisher
earth_rover /home/nvidia/catkin_ws/src/earth-rover-ros/earth_rover
earth_rover_description /home/nvidia/catkin_ws/src/earth-rover-ros/earth_rover_description
four_wheel_steering_controller /home/nvidia/catkin_ws/src/earth-rover-ros/four_wheel_steering_controller
four_wheel_steering_msgs /home/nvidia/catkin_ws/src/earth-rover-ros/four_wheel_steering_msgs
jrk_hardware /home/nvidia/catkin_ws/src/earth-rover-ros/jrk_hardware
serial /home/nvidia/catkin_ws/src/earth-rover-ros/serial
teleop_twist_joy /home/nvidia/catkin_ws/src/earth-rover-ros/teleop_twist_joy
twist_mux /home/nvidia/catkin_ws/src/earth-rover-ros/twist_mux
ublox_gps /home/nvidia/catkin_ws/src/earth-rover-ros/ublox/ublox_gps
ublox_msgs /home/nvidia/catkin_ws/src/earth-rover-ros/ublox/ublox_msgs
ublox_serialization /home/nvidia/catkin_ws/src/earth-rover-ros/ublox/ublox_serialization
urdf_geometry_parser /home/nvidia/catkin_ws/src/earth-rover-ros/urdf_geometry_parser
zed_wrapper /home/nvidia/catkin_ws/src/earth-rover-ros/zed-ros-wrapper
```

```
nvidia@earth-jetson:~$ rospack profile
Full tree crawl took 0.048930 seconds.
Directories marked with (*) contain no manifest.  You may
want to delete these directories.
To get just of list of directories without manifests,
re-run the profile with --zombie-only
-------------------------------------------------------------
0.032520   /opt/ros/kinetic/share
0.015146   /home/nvidia/catkin_ws/src
0.006695 * /home/nvidia/catkin_ws/src/devel
0.004618 * /home/nvidia/catkin_ws/src/devel/share
0.004404   /home/nvidia/catkin_ws/src/earth-rover-ros
0.001523 * /home/nvidia/catkin_ws/src/CMakeFiles
0.001305 * /home/nvidia/catkin_ws/src/devel/lib
0.001020   /home/nvidia/catkin_ws/src/earth-rover-ros/ublox
0.000773 * /home/nvidia/catkin_ws/src/gtest
0.000642 * /home/nvidia/catkin_ws/src/gtest/CMakeFiles
0.000622 * /home/nvidia/catkin_ws/src/devel/lib/python2.7
0.000536 * /home/nvidia/catkin_ws/src/devel/lib/python2.7/dist-packages
0.000515 * /home/nvidia/catkin_ws/src/devel/share/roseus
0.000486 * /home/nvidia/catkin_ws/src/devel/share/gennodejs
0.000478 * /home/nvidia/catkin_ws/src/catkin_generated
0.000441 * /home/nvidia/catkin_ws/src/CMakeFiles/3.5.1
0.000427 * /home/nvidia/catkin_ws/src/devel/share/common-lisp
0.000417 * /home/nvidia/catkin_ws/src/devel/share/roseus/ros
0.000399 * /home/nvidia/catkin_ws/src/devel/share/gennodejs/ros
0.000371 * /opt/ros/kinetic/share/OpenCV-3.3.1
```

Whitelist all the packages so you can build your entire workspace
```
catkin_make -DCATKIN_WHITELIST_PACKAGES=""
```

Build with debug output
```
catkin_make -DCMAKE_VERBOSE_MAKEFILE=ON
```