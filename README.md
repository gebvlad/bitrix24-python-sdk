#bitrix24-python-sdk
bitrix24-python-sdk is a simple API wrapper for working with Bitrix24 REST API

[Bitrix24 API documentation - Russian](http://dev.1c-bitrix.ru/rest_help/)<br />
[Bitrix24 API documentation - English](https://training.bitrix24.com/rest_help/)

##Requirements
Python 2.6 or later.  

##Installation
    pip install bitrix24-python-sdk
    
##Usage example
``` python
    from bitrix24 import Bitrix24
    bx24 = Bitrix24('YOUR_THIRD_LEVEL_DOMAIN', 'YOUR_AUTH_TOKEN')
    bx24.call('app.info')
```
## Notes
Some function needed determinate parameters consequence as described in Bitrix24 documentation. 
For example, methods from scope "task":
``` python
    bx24.call(
        'task.item.list',
        {'ORDER': {'GROUP_ID': 'asc'}},
        {'FILTER': {'GROUP_ID': 1,'REAL_STATUS': {0: STATE_NEW}}},
        {'PARAMS': {'NAV_PARAMS': {'nPageSize': 50, 'iNumPage': 2}}}
    )
```
## License
bitrix24-python-sdk is licensed under the MIT License - see the `LICENSE` file for details


## Author
Vladislav Sikach - <github@sijmusic.info><br />
See also the list of [contributors](https://github.com/gebvlad/bitrix24-python-sdk/graphs/contributors) which participated in this project

## Need custom Bitrix24 application? ##
email: <github@sijmusic.info>