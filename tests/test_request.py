import pytest

from universal_api_client.request import APIRequest


@pytest.fixture
def base_url():
    return 'https://swapi.co/api/'


@pytest.fixture
def request_instance(base_url):
    """API request fixture"""
    return APIRequest(url=base_url)


def test_url_single_path(request_instance, base_url):
    assert request_instance.people.url == '{}people/'.format(base_url)


def test_url_multi_path(request_instance, base_url):
    assert request_instance.so.many.people.url == \
        '{}so/many/people/'.format(base_url)


def test_url_single_path_with_identifier(request_instance, base_url):
    assert request_instance.people(identifier=57812).url == \
        '{}people/57812/'.format(base_url)


def test_url_multi_path_with_identifier(request_instance, base_url):
    assert request_instance.people(identifier=57812).are('so').many.url == \
        '{}people/57812/are/so/many/'.format(base_url)


def test_url_multi_path_with_many_requests(request_instance, base_url):
    assert request_instance.people(identifier=57812).are('so').many.url == \
        '{}people/57812/are/so/many/'.format(base_url)
    assert request_instance.people(identifier=57812).are('so').many.url == \
        '{}people/57812/are/so/many/'.format(base_url)
    assert request_instance.people(identifier=57812).are('so').many.url == \
        '{}people/57812/are/so/many/'.format(base_url)


def test_url_single_with_query(request_instance, base_url):
    assert request_instance.people(query={'foo': 'bar'}).url == \
        '{}people/?foo=bar'.format(base_url)


def test_url_multi_path_with_query_and_identifier(request_instance, base_url):
    assert request_instance.people(
        identifier=123).chances(query={'foo': 'bar'}).url == \
            '{}people/123/chances/?foo=bar'.format(base_url)


def test_url_multi_path_with_mixed_query_and_identifier(request_instance,
                                                        base_url):
    assert request_instance.people(
        identifier=123, query={'foo': 'bar'}).chances.url == \
            '{}people/123/chances/?foo=bar'.format(base_url)
