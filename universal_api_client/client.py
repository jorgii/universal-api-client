from .request import APIRequest


class Client(object):
    """
    API client capable of generating requests

    **Parameters**

    * **base_url** - Base url for the client.
    * **auth** - (optional) Authentication from the `requests.auth` package.
    """
    def __init__(self, base_url, auth=None):
        self.base_url = base_url
        self.auth = auth

    @property
    def request(self):
        """
           Returns an instance of universal_api_client.request.APIRequest
           with base_url as starting url.
        """
        return APIRequest(url=self.base_url, auth=self.auth)
