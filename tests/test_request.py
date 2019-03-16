import pytest

from universal_api_client.request import APIRequest


@pytest.fixture
def base_url():
    return 'https://swapi.co/api/'


@pytest.fixture
def request_instance(base_url):
    """API request fixture"""
    return APIRequest(base_url=base_url)


def test_url_single_path(request_instance, base_url):
    assert request_instance.people.url == f'{base_url}people/'


def test_url_multi_path(request_instance, base_url):
    assert request_instance.so.many.people.url == f'{base_url}so/many/people/'


def test_url_single_path_with_param(request_instance, base_url):
    assert request_instance.people(identifier=57812).url == \
        f'{base_url}people/57812/'


def test_url_multi_path_with_param(request_instance, base_url):
    assert request_instance.people(identifier=57812).are('so').many.url == \
        f'{base_url}people/57812/are/so/many/'


def test_url_single_with_query(request_instance, base_url):
    assert request_instance.people(query={'foo': 'bar'}).url == \
        f'{base_url}people/?foo=bar'
