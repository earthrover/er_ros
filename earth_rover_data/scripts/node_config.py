import os
import rospy

FIREBASE_CREDS_PATH = os.environ.get("FIREBASE_CREDS_PATH", rospy.get_param('firebase/creds_path', None))
FIREBASE_GOOGLE_API_KEY = os.environ.get("FIREBASE_GOOGLE_API_KEY", rospy.get_param('firebase/google_api_key', None))
FIREBASE_CUSTOM_TOKEN_URL = os.environ.get("FIREBASE_CUSTOM_TOKEN_URL", rospy.get_param('firebase/custom_token_url', None))
FIREBASE_AUTH_DOMAIN = os.environ.get("FIREBASE_AUTH_DOMAIN", rospy.get_param('firebase/custom_auth_domain', None))
FIREBASE_DB_URL = os.environ.get("FIREBASE_DB_URL", rospy.get_param('firebase/db_url', None))