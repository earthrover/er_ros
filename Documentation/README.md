#### EARTH ROVER ROS ####

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

Notes on our ROS Earth Rover project.
This document contains general information about ROS and how we configure it for ER-UGV

# Common commands:

```
rosnode list
rosnode info /some_node

rostopic list
rostopic info /some_topic

rostopic echo /some_topic
```

# Use tab for autocompletion

```
rostopic pub /some_topic msg/MessageType "data: value" 
```

Messages are defined by a .msg format

# Ros master
```
roscore or roslaunch will start both.
```

ROS_MASTER_URI is where the master will be.
Master only keeps track of meta information

