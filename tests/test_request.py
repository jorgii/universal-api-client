from unittest.mock import patch

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


@patch('universal_api_client.request.requests')
def test_get(mocked_requests, request_instance):
    params = {'foo': 'bar'}
    request_instance.get(params=params)
    mocked_requests.get.assert_called_once_with(
        url=request_instance.url,
        params=params)


@patch('universal_api_client.request.requests')
def test_head(mocked_requests, request_instance):
    params = {'foo': 'bar'}
    request_instance.head(params=params)
    mocked_requests.head.assert_called_once_with(
        url=request_instance.url,
        params=params)


@patch('universal_api_client.request.requests')
def test_post(mocked_requests, request_instance):
    params = {'foo': 'bar'}
    data = {'one': 'two'}
    request_instance.post(data=data, params=params)
    mocked_requests.post.assert_called_once_with(
        url=request_instance.url,
        data=data,
        params=params)


@patch('universal_api_client.request.requests')
def test_put(mocked_requests, request_instance):
    params = {'foo': 'bar'}
    data = {'one': 'two'}
    request_instance.put(data=data, params=params)
    mocked_requests.put.assert_called_once_with(
        url=request_instance.url,
        data=data,
        params=params)


@patch('universal_api_client.request.requests')
def test_patch(mocked_requests, request_instance):
    params = {'foo': 'bar'}
    data = {'one': 'two'}
    request_instance.patch(data=data, params=params)
    mocked_requests.patch.assert_called_once_with(
        url=request_instance.url,
        data=data,
        params=params)


@patch('universal_api_client.request.requests')
def test_delete(mocked_requests, request_instance):
    params = {'foo': 'bar'}
    request_instance.delete(params=params)
    mocked_requests.delete.assert_called_once_with(
        url=request_instance.url,
        params=params)
