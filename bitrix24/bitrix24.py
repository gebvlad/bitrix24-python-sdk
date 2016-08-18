#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wrapper over Bitrix24 cloud API"""

from json import loads
from logging import info
from time import sleep
from requests import adapters, post, exceptions
from multidimensional_urlencode import urlencode

# Retries for API request
adapters.DEFAULT_RETRIES = 10


class Bitrix24(object):
    """Class for working with Bitrix24 cloud API"""
    # Cloud Bitrix24 API endpoint
    api_url = 'https://%s.bitrix24.%s/rest/%s.json'
    # Bitrix24 oauth server
    oauth_url = 'https://oauth.bitrix.info/oauth/token/'
    # Timeout for API request in seconds
    timeout = 60

    def __init__(self, domain, auth_token, refresh_token='', client_id='', client_secret='', high_level_domain='ru'):
        """Create Bitrix24 API object
        :param domain: Cloud Bitrix24 third level domain 
        :param auth_token: Auth token
        :param refresh_token: Refresh token
        :param client_id: Client ID for refreshing access tokens
        :param client_secret: Client secret for refreshing access tokens
        :param high_level_domain: High level domain of Bitrix24 cloud domain
        """
        if high_level_domain not in ('ru', 'com', 'de'):
            raise Exception('Unsupported high level domain')

        self.domain = domain
        self.auth_token = auth_token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.high_level_domain = high_level_domain

    def call(self, method, params1=None, params2=None, params3=None, params4=None):
        """Call Bitrix24 API method
        :param method: Method name
        :param params1: Method parameters 1
        :param params2: Method parameters 2. Needed for methods with determinate consequence of parameters
        :param params3: Method parameters 3. Needed for methods with determinate consequence of parameters
        :param params4: Method parameters 4. Needed for methods with determinate consequence of parameters
        :return: Call result
        """
        if method == '' or not isinstance(method, str):
            raise Exception('Empty Method')

        if method == 'batch' and 'prepared' not in params1:
            params1['cmd'] = self.prepare_batch(params1['cmd'])
            params1['prepared'] = True

        encoded_parameters = ''

        for i in [params1, params2, params3, params4, {'auth': self.auth_token}]:
            if i is not None:
                encoded_parameters += urlencode(i) + '&'

        r = {}

        try:
            # request url
            url = self.api_url % (self.domain, self.high_level_domain, method)
            # Make API request
            r = post(url, params=encoded_parameters, timeout=self.timeout)
            # Decode response
            result = loads(r.text)
        except ValueError:
            result = dict(error='Error on decode api response [' + r.text + ']')
        except exceptions.ReadTimeout:
            result = dict(error='Timeout waiting expired [' + str(self.timeout) + ' sec]')
        except exceptions.ConnectionError:
            result = dict(error='Max retries exceeded [' + str(adapters.DEFAULT_RETRIES) + ']')
        if 'error' in result and result['error'] in ('NO_AUTH_FOUND', 'expired_token'):
            result = self.refresh_tokens()
            if result is not True:
                return result
            # Repeat API request after renew token
            result = self.call(method, params1, params2, params3, params4)
        elif 'error' in result and result['error'] in 'QUERY_LIMIT_EXCEEDED':
            # Suspend call on two second, wait for expired limitation time by Bitrix24 API
            sleep(2)
            return self.call(method, params1, params2, params3, params4)
        return result

    def refresh_tokens(self):
        """Refresh access tokens
        :return:
        """
        r = {}

        try:
            # Make call to oauth server
            r = post(
                self.oauth_url,
                params={'grant_type': 'refresh_token', 'client_id': self.client_id, 'client_secret': self.client_secret,
                        'refresh_token': self.refresh_token})
            result = loads(r.text)
            # Renew access tokens
            self.auth_token = result['access_token']
            self.refresh_token = result['refresh_token']
            info(['Tokens', self.auth_token, self.refresh_token])
            return True
        except (ValueError, KeyError):
            result = dict(error='Error on decode oauth response [' + r.text + ']')
            return result

    def get_tokens(self):
        """Get access tokens
        :return: dict
        """
        return {'auth_token': self.auth_token, 'refresh_token': self.refresh_token}

    @staticmethod
    def prepare_batch(params):
        """
        Prepare methods for batch call
        :param params: dict
        :return: dict
        """
        if not isinstance(params, dict):
            raise Exception('Invalid `cmd` structure')

        batched_params = dict()

        for call_id in params:
            if not isinstance(params[call_id], list):
                raise Exception('Invalid `cmd` method description')
            method = params[call_id].pop(0)
            temp = ''
            for i in params[call_id]:
                temp += urlencode(i) + '&'
            batched_params[call_id] = method + '?' + temp

        return batched_params
