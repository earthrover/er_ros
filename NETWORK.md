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

#### DUCKING JETSON HOTSPOT

Obviously... on the jetson things would not be this easy... why would they?

[Tutorial](https://devtalk.nvidia.com/default/topic/1010353/jetson-tx2/tx2-as-a-wifi-hotspot-/)

```
For those of you who is looking for a bridging solution.
My working configuration is as follows

1) echo 2 > /sys/module/bcmdhd/parameters/op_mode OR echo -e "options bcmdhd op_mode=2\n" >> /etc/modprobe.d/bcmdhd.conf

2) install create_ap script from here https://github.com/oblique/create_ap

3) prepare network interfaces side
/etc/network/interfaces:
...
source interfaces.d/wlan0
source interfaces.d/br0

/etc/network/interfaces.d/br0:
auto br0
iface br0 inet static
address 192.168.100.10
netmask 255.255.255.0
gateway 192.168.100.1
bridge_ports eth0 wlan0

/etc/network/interfaces.d/wlan0:
auto wlan0
iface wlan0 inet manual

4) If you have DHCP server on your 192.168.100.0/24 LAN do nothing or you should set up your own on TX2:
/etc/dnsmasq.conf :
...
interface=lo,br0
no-dhcp-interface=lo
dhcp-range=192.168.100.101,192.168.100.110,255.255.255.0,12h
...
and make sure dnsmasq starts when br0 is ready - 
/lib/systemd/system/dnsmasq.service:
[Unit]
Description=dnsmasq - A lightweight DHCP and caching DNS server
Requires=network.target
After=network-online.target
Wants=network-online.target

5) start create_ap as a srevice or manually, something like 
create_ap --no-virt -w 2 -m bridge wlan0 br0 Jetson-TX2 <YourSecret>
```
  
## JETSON - EARTH ROVER - ROS

#### Installation

We have to make our iptables persistent so we can load and save them
```
sudo apt-get install iptables-persistent
```

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

#### UTILS

##### Connect to a wifi network from terminal
```ifconfig wlan0```

```iwconfig wlan0 essid name key password```
Note: If you want to type the ASCII password, you would use iwconfig wlan0 essid name key s:password.

```dhclient wlan0```
