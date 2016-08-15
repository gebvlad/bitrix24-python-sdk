bitrix24-python-sdk
===================

.. image:: https://img.shields.io/pypi/v/bitrix24-python-sdk.svg
    :target: https://pypi.python.org/pypi/bitrix24-python-sdk

.. image:: https://img.shields.io/pypi/dm/bitrix24-python-sdk.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/bitrix24-python-sdk


Description
===========

*Bitrix24 REST API wrapper*

bitrix24-python-sdk is a simple API wrapper for working with Bitrix24 REST API

- Bitrix24 API documentation - English: https://training.bitrix24.com/rest_help/
- Bitrix24 API documentation - Russian: http://dev.1c-bitrix.ru/rest_help/


Requirements
============

- Python 2.6+ or 3.x
- requests
- multidimensional_urlencode

Installation
============

.. code-block:: bash

    $ pip install bitrix24-python-sdk
    ...


Quickstart
==========

.. code-block:: python

    from bitrix24 import Bitrix24

    bx24 = Bitrix24('YOUR_THIRD_LEVEL_DOMAIN', 'YOUR_AUTH_TOKEN')

    print(bx24.call('app.info'))
    ...

Notes
=====

For some functions the order of parameters is important.
For example, methods from scope "task":

.. code-block:: python

    bx24.call(
        'task.item.list',
        {'ORDER': {'GROUP_ID': 'asc'}},
        {'FILTER': {'GROUP_ID': 1,'REAL_STATUS': {0: STATE_NEW}}},
        {'PARAMS': {'NAV_PARAMS': {'nPageSize': 50, 'iNumPage': 2}}}
    )
    ...

Author
======

Vladislav Sikach - <github@sijmusic.info>
See also the list of `contributors <https://github.com/gebvlad/bitrix24-python-sdk/graphs/contributorsn>`_ which participated in this project


Need custom Bitrix24 application?
=================================
email: <github@sijmusic.info>


TODO
====

1. Documentation
2. Tests