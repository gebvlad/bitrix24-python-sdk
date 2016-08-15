bitrix24-python-sdk
===================
.. image:: https://img.shields.io/pypi/v/bitrix24-python-sdk.svg
    :target: https://pypi.python.org/pypi/bitrix24-python-sdk

.. image:: https://img.shields.io/pypi/dm/bitrix24-python-sdk.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/bitrix24-python-sdk

.. image:: https://img.shields.io/pypi/l/bitrix24-python-sdk.svg
    :target: https://pypi.python.org/pypi/bitrix24-python-sdk

Requirements
-----------

- Python 2.6+ or 3.x
- requests
- multidimensional_urlencode

Installation
------------

.. code-block:: bash

    $ pip install bitrix24-python-sdk

Description
-----------

*Bitrix24 REST API wrapper*

bitrix24-python-sdk is a simple API wrapper for working with Bitrix24 REST API

- Bitrix24 API documentation - English: https://training.bitrix24.com/rest_help/
- Bitrix24 API documentation - Russian: http://dev.1c-bitrix.ru/rest_help/


Quickstart
----------

.. code-block:: python

    from bitrix24 import Bitrix24

    bx24 = Bitrix24('YOUR_THIRD_LEVEL_DOMAIN', 'YOUR_AUTH_TOKEN')

    print(bx24.call('app.info'))



TODO
----

1. Tests
2. Documentation