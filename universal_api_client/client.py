from .request import APIRequest


class Client(object):
    def __init__(self, base_url):
        self.base_url = base_url

    @property
    def request(self):
        return APIRequest(self.base_url)
