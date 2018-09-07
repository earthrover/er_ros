#### EARTH ROVER ROS ####

Notes on our DATA Capturing.

There are currently two datasets from the farms visit:

# Data Set 1 - Summer 2018

Data set 1 contains ZED and Realsense capturing

The realsense capturing was done without Infrared cameras but the quality is good.

# Data Set 2 - September 2018

Data set 2 is as described in this document:
## Information stored

Our current data capturing process splits our data in several sections of
1 minute folders.

### Rover Ros bag 

Example

```
2018-09-05-13-56-02.bag
```

![RosBag](rosbag.png)

This rosbag contains IMU, Joystick feedback if there was any, RAW ublox data

User rqt_bag to inspect this bag format

### Realsense camera capturing

Install Librealsense on your favourite distribution

[librealsense](https://github.com/IntelRealSense/librealsense/)

Our current data capturing set contains the Realsense full video pipeline data in a Ros bag.

This bag contains 1 minute of video data at 15fps for the following streams:

1. Infrared data
We only capture one frame from the two available
640x480 IR

2. Color data
1280x720 Color RGB

3. Depth data
640x480 Z16

Metadata to create the full reconstruction 

Use the ros bag inspector from Intel to explore the raw meta data
[Rosbag Inspector](https://github.com/IntelRealSense/librealsense/tree/master/tools/rosbag-inspector)

![LibrealsenseRosBag](rosbag_realsense.jpg)

Our Librealsense metadata contains JSON metadata companion files.
The capturing framerate is faster than the GPS position framerate, therefore not every frame contains extra metadata.

```
earth@rover_002:~/data/8799ecf/180904_133002$ cat frame_0833.json
{
    "altitude": 48.876,
    "ang_vel": {
        "x": 0.0,
        "y": 0.0,
        "z": -0.0011111111111111111
    },
    "frame": 833,
    "latitude": 53.427129199999996,
    "linear_acel": {
        "x": 0.001,
        "y": 0.002,
        "z": -0.003
    },
    "longitude": -0.9160134,
    "magnetic_field": {
        "x": 15.5,
        "y": 71.1875,
        "z": 26.25
    },
    "orientation": {
        "w": 0.994140625,
        "x": 0.03076171875,
        "y": 0.10369873046875,
        "z": 0.00250244140625
    },
    "seq": 183,
    "service": 3,
    "stamp_nsecs": 332028,
    "stamp_secs": 1536067860,
    "status": 0
```
If you need more detailed metadata, the best is to open the companion rosbag which has all the raw metadata and more topics, this is just a simple digested summary of the topics which we were interested at the time of capture.

### Go Pro data
We use two camaras - Hero 5 and Hero 6

There is a folder with a tool to extract the metadata from the GPS

## Formats

TODO
```

```

## PCL Exporter

TODO 


```
                                                                                                 
                                      `.:/+osyhhdddhhyyso+/-.                                       
                                 -/shmNMMMMMMMMMMMMMMMMMMMMMMNdy+:`                                 
                             -ohNMMMMMmhyo+/:-..````..-:/+sydNMMMMNds/`                             
              `....`     `/ymMMMMdy+-``                     ``./ohNMMMNd+.                          
          -odmdhhhddmdhssNMMMmy/.`                                `-ohNMMNd/`                       
         +Nh:```````.oNMMMms-`                                       `.+hMMMNs.                     
        `Md`      `/dMMMh/`                                             ./mMMMNhhdddddddhs+:`       
        `Md      :dMMMy-`                                        .-/oyhddhyssmMMMy-.....:/sdm+      
         hM-   `sNMMd:                                     .-/ohdhhyo/-.``   .oNMMm:       `oM+     
         .Nm. -dMMN+`                                 .-+yddhy+:.``            -hMMNo`      -My     
          :Nd+NMMd-                              `-/sddhs+-.`                   `oMMMy`     yM:     
           -NMMMh`                           .-+ydhy+-.`                          /NMMh`  `sMo      
           :NMMm`                        `-ohdds/-`                                /NMMh`-dN+       
          .NMMmNy.                   `-+hdds/.`                                     +MMMhNh-        
          hMMN.:dm+`              ./yddy/-`                                          yMMMo`         
         :MMMo  `omh:         `-+hdho-`                                              `NMMh          
         hMMN`    .yNy-    `-sdmy/.                                                   sMMM.         
        `NMMy       :hNs.:sdms:`                                                      -MMM+         
        -MMM+        `oMNMh:`                                                          NMMy         
        /MMM:      .+dmy/dms.                                                          dMMd         
        /MMM:   `:ymh/`   :hNy-                                                        dMMd         
        -MMM/ .odmo-        -yNh:`                                                     NMMh         
        `MMMhsNd/`            .omd+`                                                  .MMMo         
         hMMMh:                 `/dNs-                                                oMMM-         
        `hMMM+                     -sNd+`                                            `NMMd          
       /NmdMMN`                      `/dNy:                                          sMMM:          
     `yMo .NMMh                         .omms-                                      :MMMy           
    `dN:   /MMMs                           -sNmo-                                  -NMMd`           
    hM:     +MMMy                             :yNmo-                              :NMMMo            
   `Md       +MMMh`                             `:smms:                          +NMMdsMo           
    mN-       :NMMm/                               `-sdNy/.                    .yMMMy` sM+          
    .yNho/--...:mMMMy.                                `.+ymdo:`              `+NMMN/    dN.         
      ./oyyhhhhhhhmMMNs.                                  `:ohmdo:.        `/mMMMy.     /Mo         
           ````````omMMNy:                                   ``:ohdds+-` .+mMMMh-       :Ms         
                    .omMMNdo-                                     `-+ydNmNMMMd:`      ./mm.         
                      `/hNMMNdo:`                                  -/yNMMMdyhddddhhhhddho.          
                         .+hNMMNmho:-`                        .:+ymNMMMds:` ``...----..`            
                            ./sdNMMMNmdyo/:--...````..--:/+shmNNMMMmh+-`                            
                               `.:oydmNMMMMNNNmmmmmmmNNNMMMMMNdhs/-`                                
                                    `.-:/osyhdddddddddhhyo+:-.`                                     
                                              ```````                                               
                                                                                                    
           ``````````            `            `..```        `````````````     `                     
          :ddhhhhhhhhy`         odo          :mdhhhhs:     -hhhhhdddhhhhh-   :d/           yh       
          +My--------.         /MNM+         +My...:hNs    `-----sMy-----`   +Ms           NM`      
          +Ms                 :Nm-mN:        +Ms     dM-         oMo         +Ms           NM`      
          +Ms                -NN- -NN-       +Ms   `-NN.         oMo         +Ms           NM`      
          +Mdoooooo-        .mN:   :Nm.      +Ms`oshmh-          oMo         +MdoooooooooooMM`      
          +Mdoooooo-       `dM/     /Md`     +Ms`sNMo`           oMo         +MdoooooooooooNM`      
          +Ms             `hMo       +Mh`    +Ms  .sNd/`         oMo         +Ms           NM`      
          +Ms             sMy         sMy    +Ms    .sNm+`       oMo         +Ms           NM`      
          +Mmddddddddy`  :Nh           yN/   /No      `oNm.      +Mo         /Ms           mN`      
           ----------.    .             .     .         `.       `-`          -`           ..       
                                                                                                   
                                                                                                   
```
