import os
import rospy

NTRIP_LAT = os.environ.get("NTRIP_LAT", rospy.get_param('ntrip/lat', 51.5096617))
NTRIP_LON = os.environ.get("NTRIP_LON", rospy.get_param('ntrip/lon', -0.1191824))
NTRIP_HEIGHT = os.environ.get("NTRIP_HEIGHT", rospy.get_param('ntrip/height', 16.12))
NTRIP_USER = os.environ.get("NTRIP_USER", rospy.get_param('ntrip/user', None))
NTRIP_CASTER = os.environ.get("NTRIP_CASTER", rospy.get_param('ntrip/caster', None))
NTRIP_PORT = os.environ.get("NTRIP_PORT", rospy.get_param('ntrip/port', 2101))
NTRIP_MOUNTPOINT = os.environ.get("NTRIP_MOUNTPOINT", rospy.get_param('ntrip/mountpoint', None))
NTRIP_V2 = os.environ.get("NTRIP_V2", rospy.get_param('ntrip/v2',False))
NTRIP_VERBOSE = os.environ.get("NTRIP_VERBOSE", rospy.get_param('ntrip/verbose',False))
NTRIP_SERIAL_NAME = os.environ.get("NTRIP_SERIAL_NAME", rospy.get_param('ntrip/serial_name', "Earth Rover GPS"))
NTRIP_RESEND_SECS = os.environ.get("NTRIP_RESEND_SECS", rospy.get_param('ntrip/resend_secs', 0))