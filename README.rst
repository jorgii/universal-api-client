Universal REST API Client
=========================

|Build Status|

-  Free software: MIT license
-  Documentation: https://universal-api-client.readthedocs.io/en/latest/.

Features
--------

This library is a small REST API client with the following features:

-  Url builder - allows you to build a url by natively calling the
   client's attributes
-  HTTP requests - a thin wrapper around the requests library that
   allows full control of the HTTP requests.

Installation
------------

::

   pip install universal-api-client

Usage
-----

Initialising the client
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from universal_api_client import Client
   swapi_client = Client(base_url='https://swapi.co/api/')

Building a URL
~~~~~~~~~~~~~~

The url builder is part of the ``request`` (``APIRequest``) attribute of
the client.

.. code:: python

   swapi_client.request.people # <universal_api_client.request.APIRequest at 0x1093c3eb8>
   swapi_client.request.people.url # 'https://swapi.co/api/people/'
   swapi_client.request.people(identifier=1).url # 'https://swapi.co/api/people/1/'
   swapi_client.request.people(identifier='1').url # 'https://swapi.co/api/people/1/'

Making a request
~~~~~~~~~~~~~~~~

The requests are made by the already built ``APIRequest`` object. The
method call returns the appropriate method call from the requests
library.

.. code:: python

   response = swapi_client.request.people(identifier='1').get() # <Response [200]>
   print(response.status_code) # 200

Credits
-------

This package was created with `Cookiecutter`_ and the
`audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage

.. |Build Status| image:: https://travis-ci.org/jorgii/universal-api-client.svg?branch=master
   :target: https://travis-ci.org/jorgii/universal-api-client
