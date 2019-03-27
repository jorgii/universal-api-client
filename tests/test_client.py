import pytest

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


def test_generate_request(client):
    assert isinstance(client.request, APIRequest)


def test_multiple_client_request_calls(client, base_url):
    assert client.request.people.url == \
        '{}people/'.format(base_url)
    assert client.request.people.url == \
        '{}people/'.format(base_url)
    assert client.request.people.url == \
        '{}people/'.format(base_url)
