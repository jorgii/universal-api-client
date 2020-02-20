# Universal REST API Client

[![Build Status](https://travis-ci.org/jorgii/universal-api-client.svg?branch=master)](https://travis-ci.org/jorgii/universal-api-client) [![codecov](https://codecov.io/gh/jorgii/universal-api-client/branch/master/graph/badge.svg)](https://codecov.io/gh/jorgii/universal-api-client) [![PyPI version](https://badge.fury.io/py/universal-api-client.svg)](https://badge.fury.io/py/universal-api-client)

  - Free software: MIT license
  - Documentation:
    <https://universal-api-client.readthedocs.io/en/latest/>.

## Features

This library is a small REST API client with the following features:

  - Url builder - allows you to build a url by natively calling the
    client's attributes
  - HTTP requests - a thin wrapper around the [requests](https://requests.readthedocs.io/) library that
    allows full control of the HTTP requests.

## Installation

```shell
pip install universal-api-client
```

## Usage

### Initialising the client

``` python
from universal_api_client import Client
swapi_client = Client(base_url='https://swapi.co/api/')
```

### Building a URL

The url builder is part of the `request` (`APIRequest`) attribute of the
client.

``` python
swapi_client.request.people # <universal_api_client.request.APIRequest at 0x1093c3eb8>
swapi_client.request.people.url # 'https://swapi.co/api/people/'
swapi_client.request.people(identifier=1).url # 'https://swapi.co/api/people/1/'
swapi_client.request.people(identifier='1').url # 'https://swapi.co/api/people/1/'
```

### Making a request

The requests are made by the already built `APIRequest` object. The
method call returns the appropriate method call from the requests
library.

``` python
response = swapi_client.request.people(identifier='1').get() # <Response [200]>
print(response.status_code) # 200
```

### Authentication

The library allows the use of the requests authentication classes ([request.auth](https://requests.readthedocs.io/en/master/user/authentication/#authentication)).

There are 2 ways to add authentication:

1. When initializing the client.
```python
from requests.auth import HTTPBasicAuth

swapi_client = Client(base_url='https://swapi.co/api/', auth=HTTPBasicAuth('user', 'pass'))
```

2. When performing the request (overrides the authentication set in the client).

```python
from requests.auth import HTTPBasicAuth

swapi_client.request.people.get(auth=HTTPBasicAuth('user', 'pass'))
```

### Trailing slash

Some API urls require (or not) a trailing slash at the end of the URL. This can be controlled by the `trailing_slash` flag when creating the client:

``` python
from universal_api_client import Client
swapi_client = Client(base_url='https://swapi.co/api/', trailing_slash=False)

swapi_client.request.people(identifier='1').url # 'https://swapi.co/api/people/1'
```


## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
