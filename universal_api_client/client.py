from .request import APIRequest


class Client(object):
    '''API client capable of generating requests

        :param base_url: Base url for the client.
    '''
    def __init__(self, base_url):
        self.base_url = base_url

    @property
    def request(self):
        '''Returns an instance of universal_api_client.request.APIRequest
        with base_url as starting url.
        '''
        return APIRequest(self.base_url)
