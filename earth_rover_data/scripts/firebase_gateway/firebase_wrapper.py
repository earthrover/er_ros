import pyrebase
import auth
from collections import deque
from requests.exceptions import HTTPError
from pyrebase_patches import CustomTokenDatabase



class FirebaseWrapper():

    def __init__(self,
                 credentials,
                 api_key,
                 custom_token_url,
                 auth_domain,
                 db_url):

        self.entity_uuid = credentials["ugv_id"]
        self.api_key = api_key
        self.custom_token_url = custom_token_url
        self.credentials = credentials
        self.queue = deque()

        self.custom_token = None
        self.id_token = None
        self.refresh_token = None
        self.stream = None

        config = {
            "apiKey": api_key,
            "authDomain": auth_domain,
            "databaseURL": db_url,
            "storageBucket": None
        }

        self.firebase = pyrebase.initialize_app(config)
        self.auth = self.firebase.auth()
        self.db = CustomTokenDatabase(self.firebase.credentials,
                                      self.firebase.api_key,
                                      self.firebase.database_url,
                                      self.firebase.requests)
        self.db.fetcher = self


    def read(self):
        try:
            return self.queue.popleft()
        except IndexError:
            return None


    def refresh_custom_token(self):
        token_info = auth.get_firebase_custom_token(self.credentials, self.custom_token_url)
        self.custom_token = token_info["firebase_custom_token"]


    def refresh_id_token(self):

        try:
            user_json = self.auth.sign_in_with_custom_token(self.custom_token)
        except HTTPError as e:
            self.refresh_custom_token()
            user_json = self.auth.sign_in_with_custom_token(self.custom_token)
        print("id_token: ", user_json["idToken"])
        self.id_token = user_json["idToken"]
        self.refresh_token = user_json["refreshToken"]


    def delete_message(self, timestamp):

        try:
            self.db.child("ugv").child(self.entity_uuid).child("commands").child(timestamp).remove(token=self.id_token)
        except HTTPError as e:
            self.refresh_id_token()
            self.db.child("ugv").child(self.entity_uuid).child("commands").child(timestamp).remove(token=self.id_token)


    def set_state(self, attrs):
        try:
            self.db.child("ugv").child(self.entity_uuid).child("state").set(attrs, token=self.id_token)
        except HTTPError as e:
            self.refresh_id_token()
            self.db.child("ugv").child(self.entity_uuid).child("state").set(attrs, token=self.id_token)


    def get_messages(self):

        try:
            rsp = self.db.child("ugv").child(self.entity_uuid).child("commands").get(token=self.id_token)
        except HTTPError as e:
            self.refresh_id_token()
            rsp = self.db.child("ugv").child(self.entity_uuid).child("commands").get(token=self.id_token)

        messages = []
        for k, v in rsp.val().iteritems():
            messages.append((k, v))

        return messages


    def stop_streaming(self):
        self.stream.close()


    def get_id_token(self):
        self.refresh_custom_token()
        self.refresh_id_token()
        return self.id_token

    def stream_handler(self, message):
        self.queue.append(message)

    def start_streaming(self):
        self.stream = self.db.child("ugv").child(self.entity_uuid).child("commands").stream(self.stream_handler, token=self.id_token)








