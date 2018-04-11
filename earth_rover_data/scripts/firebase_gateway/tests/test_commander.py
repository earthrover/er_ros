import unittest
import os
import json
import time
from collections import deque
from firebase_gateway.firebase_wrapper import FirebaseWrapper
from firebase_gateway import Commander

CREDS_PATH = os.path.join(os.path.dirname(__file__), "creds.json")

from config_local import *

class FetcherTestCase(unittest.TestCase):


    def testAuth(self):

        with open(CREDS_PATH) as f:
            creds = json.loads(f.read())

        fetcher = FirebaseWrapper(creds,
                                         GOOGLE_API_KEY,
                                         CUSTOM_TOKEN_URL,
                                         AUTH_DOMAIN,
                                         DB_URL)


        messages = fetcher.get_messages()

        self.assertTrue(len(messages), 1)
        self.assertEqual(messages[0][0], u'20180329-235530-906588')
        self.assertEqual(messages[0][1]["toothpaste"], "top")


    def testStreaming(self):

        with open(CREDS_PATH) as f:
            creds = json.loads(f.read())


        fetcher = FirebaseWrapper(creds,
                                         GOOGLE_API_KEY,
                                         CUSTOM_TOKEN_URL,
                                         AUTH_DOMAIN,
                                         DB_URL)

        fetcher.start_streaming()

        time.sleep(2)
        fetcher.stop_streaming()
        message = fetcher.read()

        self.assertTrue(message is not None)


    def testSetState(self):

        with open(CREDS_PATH) as f:
            creds = json.loads(f.read())


        wrapper = FirebaseWrapper(creds,
                                         GOOGLE_API_KEY,
                                         CUSTOM_TOKEN_URL,
                                         AUTH_DOMAIN,
                                         DB_URL)

        wrapper.set_state({"location": {"lon": -2.24}})



    def testCommander(self):

        with open(CREDS_PATH) as f:
            creds = json.loads(f.read())

        commander = Commander(creds,
                              GOOGLE_API_KEY,
                              CUSTOM_TOKEN_URL,
                              AUTH_DOMAIN,
                              DB_URL)
        commander.start()
        time.sleep(2)
        commander.tick()
        commander.stop()


