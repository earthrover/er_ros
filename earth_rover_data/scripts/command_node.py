import json
import time
from threading import Lock
import rospy

from firebase_gateway import Commander
import navigation_api
from node_config import *


mutex = Lock()
node = None



class EarthRoverCommandNode(object):

    def __init__(self,
                 creds_path,
                 google_api_key,
                 custom_token_url,
                 auth_domain,
                 db_url):

        self.state = {}

        with open(creds_path) as f:
            creds = json.loads(f.read())

        self.commander = Commander(creds,
                                  google_api_key,
                                  custom_token_url,
                                  auth_domain,
                                  db_url)

        navigation_api.init_api()
        self.commander.add_function("nav_start", navigation_api.start)
        self.commander.add_function("nav_pause", navigation_api.pause)
        self.commander.add_function("nav_cancel", navigation_api.cancel)
        self.commander.add_function("nav_add_waypoint", navigation_api.add_waypoint)


    def start(self):
        rospy.init_node('earth_rover_command', anonymous=True)

        self.commander.start()

        while True:
            try:
                time.sleep(1)
                self.commander.tick()
            except KeyboardInterrupt as e:
                print("done")
                break

        self.commander.stop()




if __name__ == '__main__':
    node = EarthRoverCommandNode(creds_path=FIREBASE_CREDS_PATH,
                 google_api_key=FIREBASE_GOOGLE_API_KEY,
                 custom_token_url=FIREBASE_CUSTOM_TOKEN_URL,
                 auth_domain=FIREBASE_AUTH_DOMAIN,
                 db_url=FIREBASE_DB_URL)
    node.start()

