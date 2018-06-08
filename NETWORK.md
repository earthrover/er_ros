NETWORK CONFIGURATION
=====================

Documentation of how the internal network is setup in the Earth Rover UGV.

## ROUTER

Our current router is "Earth Rover Demo"
We use a normal router with a DHCP on the range of 192.168.1.200+
Our machines have fixed ips on this network 

## PI 

Description per interface
#### ETHERNET PORT
Fixed ip 192.168.0.50

#### WIFI

##### Earth rover demo 
Fixed ip 192.168.1.50

##### Hotspot

We expose our internal network usign the Hotspot functionality of Ubuntu
Here is the setup:

Simple steps: Create wifi hotspot in ubuntu

```
Disable Wifi (Uncheck Enable Wi-Fi)
Go to network connection (Edit Connections...)
Click "Add"
Choose "Wi-Fi" and click "Create"
Type in Connection name like "wifi-hotspot"
Type in SSID as "Earth Rover XXX" (xxx being our rover ID number)
Choose Device MAC Address from the dropdown (wlan0)
Wifi Security select "WPA & WPA2 Personal" and set a password.
Go to IPv4 Settings tab, from Method drop-down box select Shared to other computers.
Then save and close.
Open Terminal (Ctrl+Alt+T) and type in the following command with your connection name used in step 5.
```

```
sudo vim /etc/NetworkManager/system-connections/wifi-hotspot
```

```
Find mode=infrastructure and change it to mode=ap
```

Now check the network section where wi-fi will be connected to the created hotspot automatically. If you can not find it, go to Connect to Hidden Network... Find the connection and connect to it.

[Source](http://ubuntuhandbook.org/index.php/2014/09/3-ways-create-wifi-hotspot-ubuntu/)

## JETSON - EARTH ROVER - ROS

#### SSH TUNNEL

We have to add Gateway forwarding functionality into our ubuntu 

```
sudo vim /etc/ssh_d/sshd_config
```

Add 
```
# Gateway for SSH
GatewayPorts yes
ClientAliveInterval 15
ClientAliveCountMax 3
```

Accept the ports from the PI to redirect
```
sudo iptables -A FORWARD -p tcp --dport 15900 -j ACCEPT
sudo iptables -A FORWARD -p tcp --dport 122 -j ACCEPT
sudo iptables-save
```

#### WIFI
Fixed 192.168.1.25

#### ETHERNET PORT 1
Fixed 192.168.0.25

#### ETHERNET PORT 2
Undefined, it will forward into the network

#### GATEWAY SETUP
[https://www.homenetworkhelp.info/articles-install-simple-network-gateway/](How to setup a Gateway)
