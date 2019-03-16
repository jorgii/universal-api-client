from urllib import parse


class APIRequest(object):
    def __init__(self, url):
        self.url = url

    def __getattr__(self, name):
        updated_url = self._update_url(self.url, name)
        return APIRequest(updated_url)

    def __call__(self, identifier=None, query=None):
        updated_url = self._update_url(
            self.url, identifier=identifier, query=query)
        return APIRequest(updated_url)

    def _update_url(self, url, identifier=None, query=None):
        url_parts = list(parse.urlparse(url))
        if identifier:
            url_parts[2] = parse.urljoin(url_parts[2], str(identifier)) + '/'
        if query and isinstance(query, dict):
            query.update(parse.parse_qsl(url_parts[4]))
            url_parts[4] = parse.urlencode(query)
        return parse.urlunparse(url_parts)
