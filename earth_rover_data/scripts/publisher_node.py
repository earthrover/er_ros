#!/usr/bin/env python

import json
import time
from threading import Lock
import rospy
from sensor_msgs.msg import NavSatFix

from firebase_gateway.firebase_wrapper import FirebaseWrapper
from node_config import *


mutex = Lock()

node = None

def fix_callback(data):
    mutex.acquire()
    try:
        node.state["fix"] = {
            "status": data.status.status,
            "service": data.status.service,
            "lat": data.latitude,
            "lon": data.longitude,
            "alt": data.altitude,
        }
    finally:
        mutex.release()


class EarthRoverPublisherNode(object):

    def __init__(self,
                 creds_path,
                 google_api_key,
                 custom_token_url,
                 auth_domain,
                 db_url):

        self.state = {}

        with open(creds_path) as f:
            creds = json.loads(f.read())

        self.wrapper = FirebaseWrapper(creds,
                                  google_api_key,
                                  custom_token_url,
                                  auth_domain,
                                  db_url)

    def start(self):
        rospy.init_node('earth_rover_publisher', anonymous=True)
        ## start a subscriber to listen
        rospy.Subscriber("/gps/fix", NavSatFix, fix_callback)

        while True:
            try:
                time.sleep(10)
                self.publish()
            except KeyboardInterrupt as e:
                print("done")


    def publish(self):
        mutex.acquire()
        self.wrapper.set_state(self.state)
        mutex.release()


if __name__ == '__main__':
    node = EarthRoverPublisherNode(creds_path=FIREBASE_CREDS_PATH,
                 google_api_key=FIREBASE_GOOGLE_API_KEY,
                 custom_token_url=FIREBASE_CUSTOM_TOKEN_URL,
                 auth_domain=FIREBASE_AUTH_DOMAIN,
                 db_url=FIREBASE_DB_URL)
    node.start()


