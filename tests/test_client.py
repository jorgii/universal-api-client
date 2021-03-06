import pytest

from requests.auth import HTTPBasicAuth

from universal_api_client.client import Client
from universal_api_client.request import APIRequest


@pytest.fixture
def base_url():
    return 'https://swapi.co/api/'


@pytest.fixture
def client(base_url):
    """API client fixture"""
    return Client(base_url=base_url)


def test_base_url():
    client = Client(base_url='https://google.com/')
    assert client.base_url == 'https://google.com/'


def test_auth():
    auth = HTTPBasicAuth('user', 'pass')
    client = Client(
        base_url='https://google.com/',
        auth=auth)
    assert client.auth == auth


def test_generate_request(client):
    assert isinstance(client.request, APIRequest)


def test_multiple_client_request_calls(client, base_url):
    assert client.request.people.url == \
        '{}people/'.format(base_url)
    assert client.request.people.url == \
        '{}people/'.format(base_url)
    assert client.request.people.url == \
        '{}people/'.format(base_url)


def test_client_no_trailing_slash():
    client = Client(
        base_url='https://google.com/',
        trailing_slash=False)
    assert client.request.trailing_slash is False
