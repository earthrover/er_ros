import socket
import six
import json
from requests.exceptions import HTTPError

from pyrebase.pyrebase import Database, Stream, ClosableSSEClient


class Py2ClosableSSEClient(ClosableSSEClient):

    def close(self):
        self.should_connect = False
        self.retry = 0
        if six.PY2:
            self.resp.raw._fp.fp._sock.shutdown(socket.SHUT_RDWR)
            self.resp.raw._fp.fp._sock.close()
        else:
            self.resp.raw._fp.fp.raw._sock.shutdown(socket.SHUT_RDWR)
            self.resp.raw._fp.fp.raw._sock.close()


class CustomTokenStream(Stream):

    def __init__(self, url_source, stream_handler, build_headers, stream_id):
        self.url_source = url_source
        url = url_source()
        self.should_stop = False
        Stream.__init__(self, url, stream_handler, build_headers, stream_id)


    def start_stream(self):

        while not self.should_stop:
            try:
                self.sse = Py2ClosableSSEClient(self.url, session=self.make_session(), build_headers=self.build_headers)
                for msg in self.sse:
                    if msg:
                        msg_data = json.loads(msg.data)
                        msg_data["event"] = msg.event
                        if self.stream_id:
                            msg_data["stream_id"] = self.stream_id
                        self.stream_handler(msg_data)
            except HTTPError as e:
                self.url = self.url_source()

    def close(self):
        self.should_stop = True
        Stream.close(self)


class CustomTokenDatabase(Database):

    fetcher = None

    def build_url_with_custom_token(self):
        return self.build_request_url(self.fetcher.get_id_token())


    def stream(self, stream_handler, token=None, stream_id=None):
        return CustomTokenStream(self.build_url_with_custom_token, stream_handler, self.build_headers, stream_id)