#!/usr/bin/python -u
"""
This is heavily based on the NtripPerlClient program written by BKG.
Then heavily based on a unavco original.
"""

import socket
import sys
import datetime
import base64
import time
# import ssl
import serial
import serial.tools.list_ports as prtlst

from config import *

version=0.1
useragent="NTRIP EarthRoverClient/%.1f" % version

# reconnect parameter (fixed values):
factor=2 # How much the sleep time increases with each failed attempt
maxReconnect=10
maxReconnectTime=1200
sleepTime=1 # So the first one is 1 second
maxConnectTime=0

class NtripClient(object):
    def __init__(self,
                 buffer=50,
                 user="",
                 out=sys.stdout,
                 port=2101,
                 caster="",
                 mountpoint="",
                 host=False,
                 lat=46,
                 lon=122,
                 height=1212,
                 ssl=False,
                 verbose=False,
                 UDP_Port=None,
                 V2=False,
                 headerFile=sys.stderr,
                 headerOutput=False,
                 position_callback=None,
                 resend_secs=0
                 ):
        self.buffer=buffer
        self.user=base64.b64encode(user)
        self.out=out
        self.port=port
        self.caster=caster
        self.mountpoint=mountpoint
        self.setPosition(lat, lon)
        self.height=height
        self.verbose=verbose
        self.ssl=ssl
        self.host=host
        self.UDP_Port=UDP_Port
        self.V2=V2
        self.headerFile=headerFile
        self.headerOutput=headerOutput
        self.maxConnectTime=maxConnectTime
        self.lastGga = 0
        self.position_callback = position_callback
        self.resend_secs = resend_secs

        self.socket=None

        if UDP_Port:
            self.UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.UDP_socket.bind(('', 0))
            self.UDP_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        else:
            self.UDP_socket=None


    def setPosition(self, lat, lon):
        self.flagN="N"
        self.flagE="E"
        if lon>180:
            lon=(lon-360)*-1
            self.flagE="W"
        elif (lon<0 and lon>= -180):
            lon=lon*-1
            self.flagE="W"
        elif lon<-180:
            lon=lon+360
            self.flagE="E"
        else:
            self.lon=lon
        if lat<0:
            lat=lat*-1
            self.flagN="S"
        self.lonDeg=int(lon)
        self.latDeg=int(lat)
        self.lonMin=(lon-self.lonDeg)*60
        self.latMin=(lat-self.latDeg)*60

    def getMountPointString(self):

        header = \
            "GET /{} HTTP/1.1\r\n".format(self.mountpoint) + \
            "Host \r\n".format(self.caster) + \
            "Ntrip-Version: Ntrip/1.0\r\n" + \
            "User-Agent: NTRIP_earth_rover/0.0\r\n" + \
            "Authorization: Basic {}\r\n\r\n".format(self.user)

        return header

    def getGGAString(self):
        if self.position_callback is not None:
            lat, lon, self.height = self.position_callback()
            self.setPosition(lat, lon)
        now = datetime.datetime.utcnow()
        ggaString= "GPGGA,%02d%02d%04.2f,%02d%011.8f,%1s,%03d%011.8f,%1s,1,05,0.19,+00400,M,%5.3f,M,," % \
            (now.hour,now.minute,now.second,self.latDeg,self.latMin,self.flagN,self.lonDeg,self.lonMin,self.flagE,self.height)
        checksum = self.calcultateCheckSum(ggaString)
        if self.verbose:
            print  "$%s*%s\r\n" % (ggaString, checksum)
        return "$%s*%s\r\n" % (ggaString, checksum)

    def calcultateCheckSum(self, stringToCheck):
        xsum_calc = 0
        for char in stringToCheck:
            xsum_calc = xsum_calc ^ ord(char)
        return "%02X" % xsum_calc

    def send_gga(self):
        now = time.time()
        if now > self.lastGga + self.resend_secs:
            self.socket.sendall(self.getGGAString())
            self.lastGga = now

    def readData(self):
        reconnectTry=1
        sleepTime=1
        reconnectTime=0

        if maxConnectTime > 0 :
            EndConnect=datetime.timedelta(seconds=maxConnectTime)
        try:
            while reconnectTry<=maxReconnect:
                found_header=False
                if self.verbose:
                    sys.stderr.write('Connection {0} of {1}\n'.format(reconnectTry,maxReconnect))

                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # if self.ssl:
                #     self.socket=ssl.wrap_socket(self.socket)

                error_indicator = self.socket.connect_ex((self.caster, self.port))

                if error_indicator==0:
                    sleepTime = 1
                    connectTime=datetime.datetime.now()

                    self.socket.settimeout(10)
                    self.socket.sendall(self.getMountPointString())

                    while not found_header:
                        casterResponse=self.socket.recv(4096) #All the data
                        header_lines = casterResponse.split("\r\n")

                        for line in header_lines:
                            if line=="":
                                if not found_header:
                                    found_header=True
                                    if self.verbose:
                                        sys.stderr.write("End Of Header"+"\n")
                            else:
                                if self.verbose:
                                    sys.stderr.write("Header: " + line+"\n")
                            if self.headerOutput:
                                self.headerFile.write(line+"\n")

                        for line in header_lines:
                            print(line)
                            if line.find("SOURCETABLE")>=0:
                                sys.stderr.write("Mount point does not exist")
                                sys.exit(1)
                            elif line.find("401 Unauthorized")>=0:
                                sys.stderr.write("Unauthorized request\n")
                                sys.exit(1)
                            elif line.find("404 Not Found")>=0:
                                sys.stderr.write("Mount Point does not exist\n")
                                sys.exit(2)
                            elif line.find("ICY 200 OK")>=0:
                                #Request was valid
                                self.send_gga()
                            elif line.find("HTTP/1.0 200 OK")>=0:
                                #Request was valid
                                self.send_gga()
                            elif line.find("HTTP/1.1 200 OK")>=0:
                                #Request was valid
                                self.send_gga()

                    data = "Initial data"
                    while data:
                        try:
                            data=self.socket.recv(self.buffer)
                            self.out.write(data)
                            if self.resend_secs > 0:
                                self.send_gga()
                            if self.UDP_socket:
                                self.UDP_socket.sendto(data, ('<broadcast>', self.UDP_Port))
#                            print datetime.datetime.now()-connectTime
                            if maxConnectTime :
                                if datetime.datetime.now() > connectTime+EndConnect:
                                    if self.verbose:
                                        sys.stderr.write("Connection Timed exceeded\n")
                                    sys.exit(0)

                        except socket.timeout:
                            sys.stderr.write('Connection TimedOut\n')
                            if self.verbose:
                                sys.stderr.write('Connection TimedOut\n')
                            data=False
                        except socket.error:
                            sys.stderr.write('Connection Error\n')
                            if self.verbose:
                                sys.stderr.write('Connection Error\n')
                            data=False

                    if self.verbose:
                        sys.stderr.write('Closing Connection 2\n')
                    self.socket.close()
                    self.socket=None

                    if reconnectTry < maxReconnect :
                        sys.stderr.write( "%s No Connection to NtripCaster.  Trying again in %i seconds\n" % (datetime.datetime.now(), sleepTime))
                        time.sleep(sleepTime)
                        sleepTime *= factor

                        if sleepTime>maxReconnectTime:
                            sleepTime=maxReconnectTime

                    reconnectTry += 1
                else:
                    self.socket=None
                    if self.verbose:
                        print("Error indicator: ", error_indicator)

                    if reconnectTry < maxReconnect :
                        sys.stderr.write( "%s No Connection to NtripCaster.  Trying again in %i seconds\n" % (datetime.datetime.now(), sleepTime))
                        time.sleep(sleepTime)
                        sleepTime *= factor
                        if sleepTime>maxReconnectTime:
                            sleepTime=maxReconnectTime
                    reconnectTry += 1

        except KeyboardInterrupt:
            if self.socket:
                self.socket.close()
            sys.exit()


def look_for_device(serial_name, ):
    pts = prtlst.comports()
    for pt in pts:
        if serial_name in str(pt.product):  # check 'USB' string in device description
            return pt[0]
    return None


def run_client(ntripArgs, serial_name):

    device = look_for_device(serial_name)

    ser = None

    if device is not None:
        ser = serial.Serial(device, baudrate=115200, timeout=1)
        ntripArgs['out'] = ser

    print "Device: %s" % device
    print "Server: " + ntripArgs['caster']
    print "Port: " + str(ntripArgs['port'])
    print "User: " + ntripArgs['user']
    # print "mountpoint: " +ntripArgs['mountpoint']

    if ntripArgs['V2']:
        print "NTRIP: V2"
    else:
        print "NTRIP: V1 "
    if ntripArgs["ssl"]:
        print "SSL Connection"
    else:
        print "Uncrypted Connection"
    print ""

    n = NtripClient(**ntripArgs)
    try:
        n.readData()
    finally:
        if ser is not None:
            ser.close()
        print "done"



if __name__ == '__main__':

    ntripArgs = {}
    ntripArgs['lat'] = NTRIP_LAT
    ntripArgs['lon'] = NTRIP_LON
    ntripArgs['height'] = NTRIP_HEIGHT
    ntripArgs['host'] = False
    ntripArgs['ssl'] = False
    ntripArgs['user'] = NTRIP_USER
    ntripArgs['caster'] = NTRIP_CASTER
    ntripArgs['port'] = NTRIP_PORT
    ntripArgs['mountpoint'] = NTRIP_MOUNTPOINT
    ntripArgs['V2'] = NTRIP_V2
    ntripArgs['verbose'] = NTRIP_VERBOSE
    ntripArgs['headerOutput'] = False
    ntripArgs['resend_secs'] = NTRIP_RESEND_SECS

    run_client(ntripArgs, NTRIP_SERIAL_NAME)




