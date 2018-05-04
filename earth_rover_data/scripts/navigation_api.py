import rospy

from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import Quaternion
from earth_rover_navigation.srv import *

api = None

class NavigationApi(object):

    def __init__(self):

        self.start_service = rospy.ServiceProxy('/earth_rover_navigation/start_navigation', StartNavigation)
        self.pause_service = rospy.ServiceProxy('/earth_rover_navigation/pause_navigation', PauseNavigation)
        self.cancel_service = rospy.ServiceProxy('/earth_rover_navigation/cancel_navigation', CancelNavigation)
        self.add_waypoint_service = rospy.ServiceProxy('/earth_rover_navigation/add_geo_waypoint', GeoWpSrv)


def init_api():
    global api
    api = NavigationApi()

def start():
    api.start_service()

def pause():
    api.pause_service()

def cancel():
    api.cancel_service()


def add_waypoint(lat, lon, east, north):
    fix = NavSatFix(latitude=lat, logitude=lon)
    direction = Quaternion(x=east, y=north, z=0.0, w=1.0)
    api.add_waypoint_service(gps_wp=fix, orientation=direction)

