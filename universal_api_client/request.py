from urllib import parse

import requests


class APIRequest(object):
    '''URL builder and a thin wrapper around the requests library.

        :param url: Url for the request.
    '''
    def __init__(self, url):
        self.url = url

    def __getattr__(self, name):
        updated_url = self._update_url(self.url, name)
        return APIRequest(updated_url)

    def __call__(self, identifier=None):
        updated_url = self._update_url(
            self.url, identifier=identifier)
        return APIRequest(updated_url)

    def _update_url(self, url, identifier=None):
        url_parts = list(parse.urlparse(url))
        if identifier:
            url_parts[2] = parse.urljoin(url_parts[2], str(identifier)) + '/'
        return parse.urlunparse(url_parts)

    def get(self, **kwargs):
        '''Sends a GET request. Returns :class:`Response` object.

        :param \*\*kwargs: Optional arguments that ``request`` takes.
        '''

        return requests.get(url=self.url, **kwargs)

    def head(self, **kwargs):
        '''Sends a HEAD request. Returns :class:`Response` object.

        :param \*\*kwargs: Optional arguments that ``request`` takes.
        '''

        return requests.head(url=self.url, **kwargs)

    def post(self, data=None, **kwargs):
        '''Sends a POST request. Returns :class:`Response` object.

        :param data: (optional) Dictionary, bytes, or file-like object
            to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        '''

        return requests.post(url=self.url, data=data, **kwargs)

    def put(self, data=None, **kwargs):
        '''Sends a PUT request. Returns :class:`Response` object.

        :param data: (optional) Dictionary, bytes, or file-like object
            to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        '''

        return requests.put(url=self.url, data=data, **kwargs)

    def patch(self, data=None, **kwargs):
        '''Sends a PATCH request. Returns :class:`Response` object.

        :param data: (optional) Dictionary, bytes, or file-like object
            to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        '''

        return requests.patch(url=self.url, data=data, **kwargs)

    def delete(self, **kwargs):
        '''Sends a DELETE request. Returns :class:`Response` object.

        :param \*\*kwargs: Optional arguments that ``request`` takes.
        '''

        return requests.delete(url=self.url, **kwargs)

    def options(self, **kwargs):
        '''Sends a OPTIONS request. Returns :class:`Response` object.

        :param \*\*kwargs: Optional arguments that ``request`` takes.
        '''

        return requests.options(url=self.url, **kwargs)
