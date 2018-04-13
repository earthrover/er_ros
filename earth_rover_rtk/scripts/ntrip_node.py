#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix

from threading import Lock
from ntrip_client.client import run_client
from node_config import *

node = None
mutex = Lock()

def fix_callback(data):
    mutex.acquire()
    try:
        if data.status >= 0:
            node.lat = data.latitude
            node.lon = data.longitude
            node.height = data.altitude
    finally:
        mutex.release()


def get_position():
    mutex.acquire()
    try:
        return node.lat, node.lon, node.height
    finally:
        mutex.release()


class RtkNode(object):

    def __init__(self):

        self.lat = None
        self.lon = None
        self.height = None


    def start(self):

        rospy.init_node('earth_rover_rtk', anonymous=True)

        ntripArgs = {}
        ntripArgs['lat'] = self.lat = NTRIP_LAT
        ntripArgs['lon'] = self.lon = NTRIP_LON
        ntripArgs['height'] = self.height = NTRIP_HEIGHT
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
        ntripArgs["position_callback"] = get_position

        ## start a subscriber to listen
        rospy.Subscriber("/earth_gps/fix", NavSatFix, fix_callback)

        run_client(ntripArgs, NTRIP_SERIAL_NAME)



if __name__ == '__main__':
    node = RtkNode()
    node.start()




