
from firebase_wrapper import FirebaseWrapper

class Commander():

    def __init__(self, creds, google_api_key, custom_token_url, auth_domain, db_url):

        self.fetcher = FirebaseWrapper(creds,
                                              google_api_key,
                                              custom_token_url,
                                              auth_domain,
                                              db_url)
        self.functions = {}
        self.add_function("log", self.log)
        self.logged = []


    def start(self):
        self.fetcher.start_streaming()


    def stop(self):
        self.fetcher.stop_streaming()


    def log(self, message):
        self.logged.append(message)
        print message


    def add_function(self, name, func):
        self.functions[name] = func

    def tick(self, sentry_client=None):

        messages = self.fetcher.read()

        while messages is not None:

            event = messages["event"]
            path = messages["path"]
            data = messages["data"]

            if data is not None:
                print  "recieved command: ", data

                for timestamp, rpc in data.iteritems():

                    method = rpc.get("method")

                    if method is not None:
                        func = self.functions.get(method)
                        if func is not None:
                            params = rpc.get("params")
                            if params is not None:
                                try:
                                    func(*params)
                                except Exception as e:
                                    if sentry_client is None:
                                        print "Failed to run method: %s Error: %s" % (method, e)
                                    else:
                                        print "Failed to run method: %s check sentry for details" % (method)
                                        sentry_client.captureException()
                    else:
                        print "got a message but it's not json rpc: %s " % rpc

                    # when you are done delete the message from firebase
                    self.fetcher.delete_message(timestamp)

            messages = self.fetcher.read()

