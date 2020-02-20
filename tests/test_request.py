from unittest.mock import patch

import pytest

from requests.auth import HTTPBasicAuth

from universal_api_client.request import APIRequest


@pytest.fixture
def base_url():
    return 'https://swapi.co/api/'


@pytest.fixture
def basic_auth():
    return HTTPBasicAuth('user', 'pass')


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


def test_url_single_path_with_identifier_no_trailing_slash(base_url):
    request_instance = APIRequest(url=base_url, trailing_slash=False)
    assert request_instance.people(identifier=57812).url == \
        '{}people/57812'.format(base_url)


def test_url_multi_path_with_identifier(request_instance, base_url):
    assert request_instance.people(identifier=57812).are('so').many.url == \
        '{}people/57812/are/so/many/'.format(base_url)


def test_url_multi_path_no_trailing_slash(base_url):
    request_instance = APIRequest(url=base_url, trailing_slash=False)
    assert request_instance.people(identifier=57812).are('so').many.url == \
        '{}people/57812/are/so/many'.format(base_url)


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
def test_get_with_auth(mocked_requests, request_instance, basic_auth):
    request_instance.get(auth=basic_auth)
    mocked_requests.get.assert_called_once_with(
        url=request_instance.url,
        auth=basic_auth)


@patch('universal_api_client.request.requests')
def test_head(mocked_requests, request_instance):
    params = {'foo': 'bar'}
    request_instance.head(params=params)
    mocked_requests.head.assert_called_once_with(
        url=request_instance.url,
        params=params)


@patch('universal_api_client.request.requests')
def test_head_with_auth(mocked_requests, request_instance, basic_auth):
    request_instance.head(auth=basic_auth)
    mocked_requests.head.assert_called_once_with(
        url=request_instance.url,
        auth=basic_auth)


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
def test_post_with_auth(mocked_requests, request_instance, basic_auth):
    request_instance.post(auth=basic_auth)
    mocked_requests.post.assert_called_once_with(
        url=request_instance.url,
        data=None,
        auth=basic_auth)


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
def test_put_with_auth(mocked_requests, request_instance, basic_auth):
    request_instance.put(auth=basic_auth)
    mocked_requests.put.assert_called_once_with(
        url=request_instance.url,
        data=None,
        auth=basic_auth)


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
def test_patch_with_auth(mocked_requests, request_instance, basic_auth):
    request_instance.patch(auth=basic_auth)
    mocked_requests.patch.assert_called_once_with(
        url=request_instance.url,
        data=None,
        auth=basic_auth)


@patch('universal_api_client.request.requests')
def test_delete(mocked_requests, request_instance):
    params = {'foo': 'bar'}
    request_instance.delete(params=params)
    mocked_requests.delete.assert_called_once_with(
        url=request_instance.url,
        params=params)


@patch('universal_api_client.request.requests')
def test_delete_with_auth(mocked_requests, request_instance, basic_auth):
    request_instance.delete(auth=basic_auth)
    mocked_requests.delete.assert_called_once_with(
        url=request_instance.url,
        auth=basic_auth)


@patch('universal_api_client.request.requests')
def test_options(mocked_requests, request_instance):
    params = {'foo': 'bar'}
    request_instance.options(params=params)
    mocked_requests.options.assert_called_once_with(
        url=request_instance.url,
        params=params)


@patch('universal_api_client.request.requests')
def test_options_with_auth(mocked_requests, request_instance, basic_auth):
    request_instance.options(auth=basic_auth)
    mocked_requests.options.assert_called_once_with(
        url=request_instance.url,
        auth=basic_auth)


def test_update_kwargs_no_auth(request_instance):
    kwargs = request_instance._update_kwargs({})
    assert kwargs == {}


def test_update_kwargs_auth_in_kwargs(request_instance):
    kwargs = request_instance._update_kwargs({'auth': 'foo'})
    assert kwargs == {'auth': 'foo'}


def test_update_kwargs_auth_in_instance(request_instance):
    request_instance.auth = 'foo'
    kwargs = request_instance._update_kwargs({})
    assert kwargs == {'auth': 'foo'}


def test_update_kwargs_auth_in_instance_and_kwargs(request_instance):
    request_instance.auth = 'foo'
    kwargs = request_instance._update_kwargs({'auth': 'bar'})
    assert kwargs == {'auth': 'bar'}
