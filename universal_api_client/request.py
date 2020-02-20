from urllib import parse

import requests


class APIRequest(object):
    """
    URL builder and a thin wrapper around the requests library.

    **Parameters**

    * **url** - Url for the request.
    * **auth** - (optional) Authentication from the `requests.auth` package.
    * **trailing_slash** - (optional) Flag to define whether to put
    trailing slash at the end of the generated url.
    """
    def __init__(self, url, auth=None, trailing_slash=True):
        self.url = url
        self.auth = auth
        self.trailing_slash = trailing_slash

    def __getattr__(self, name):
        updated_url = self._append_to_url(self.url, name, self.trailing_slash)
        return APIRequest(url=updated_url, trailing_slash=self.trailing_slash)

    def __call__(self, identifier=None):
        updated_url = self._append_to_url(
            self.url,
            identifier,
            self.trailing_slash)
        return APIRequest(url=updated_url, trailing_slash=self.trailing_slash)

    def _append_to_url(self, base, name, trailing_slash=True):
        name = str(name)
        if base[-1] != '/':
            base = base + '/'
        if trailing_slash:
            name = name + '/'
        return parse.urljoin(base, name)

    def _update_kwargs(self, kwargs):
        if 'auth' not in kwargs and self.auth:
            kwargs['auth'] = self.auth
        return kwargs

    def get(self, **kwargs):
        """
        Sends a GET request. Returns `Response` object.

        **Parameters**

        * **\\*\\*kwargs** - (optional) Optional arguments that `request`
        takes.
        """
        kwargs = self._update_kwargs(kwargs)
        return requests.get(url=self.url, **kwargs)

    def head(self, **kwargs):
        """
        Sends a HEAD request. Returns `Response` object.

        **Parameters**

        * **\\*\\*kwargs** - (optional) Optional arguments that `request`
        takes.
        """

        kwargs = self._update_kwargs(kwargs)
        return requests.head(url=self.url, **kwargs)

    def post(self, data=None, **kwargs):
        """
        Sends a POST request. Returns `Response` object.

        **Parameters**

        * **data** - (optional) Dictionary, bytes, or file-like object
        to send in the body of the `Request`.
        * **\\*\\*kwargs** - (optional) Optional arguments that `request`
        takes.
        """

        kwargs = self._update_kwargs(kwargs)
        return requests.post(url=self.url, data=data, **kwargs)

    def put(self, data=None, **kwargs):
        """
        Sends a PUT request. Returns `Response` object.

        **Parameters**

        * **data** - (optional) Dictionary, bytes, or file-like object
        to send in the body of the `Request`.
        * **\\*\\*kwargs** - (optional) Optional arguments that `request`
        takes.
        """

        kwargs = self._update_kwargs(kwargs)
        return requests.put(url=self.url, data=data, **kwargs)

    def patch(self, data=None, **kwargs):
        """
        Sends a PATCH request. Returns `Response` object.

        **Parameters**

        * **data** - (optional) Dictionary, bytes, or file-like object
        to send in the body of the `Request`.
        * **\\*\\*kwargs** - (optional) Optional arguments that `request`
        takes.
        """

        kwargs = self._update_kwargs(kwargs)
        return requests.patch(url=self.url, data=data, **kwargs)

    def delete(self, **kwargs):
        """
        Sends a DELETE request. Returns `Response` object.

        **Parameters**

        * **\\*\\*kwargs** - (optional) Optional arguments that `request`
        takes.
        """

        kwargs = self._update_kwargs(kwargs)
        return requests.delete(url=self.url, **kwargs)

    def options(self, **kwargs):
        """
        Sends a OPTIONS request. Returns `Response` object.

        **Parameters**

        * **\\*\\*kwargs** - (optional) Optional arguments that `request`
        takes.
        """

        kwargs = self._update_kwargs(kwargs)
        return requests.options(url=self.url, **kwargs)
