from urllib import parse


class APIRequest(object):
    def __init__(self, base_url):
        self.base_url = base_url
        self._url = parse.urlparse(base_url)

    @property
    def url(self):
        return parse.urlunparse(self._url)

    def __getattr__(self, name):
        self._url = self.update_url(self._url, path=name)
        return self

    def __call__(self, identifier=None, query=None):
        self._url = self.update_url(self._url, path=identifier, query=query)
        return self

    def update_url(self, url, path=None, query=None):
        url_parts = list(url)
        if path:
            url_parts[2] = parse.urljoin(url.path, str(path)) + '/'
        if query and isinstance(query, dict):
            query.update(parse.parse_qsl(url.query))
            url_parts[4] = parse.urlencode(query)
        return parse.urlparse(parse.urlunparse(url_parts))
