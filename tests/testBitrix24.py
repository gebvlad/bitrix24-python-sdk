#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for Bitrix24"""

import unittest
from bitrix24 import Bitrix24


class TestBitrix24WithCorrectAccessTokens(unittest.TestCase):
    access_data = {
        'auth_token': '<YOUR_AUTH_TOKEN>',
        'refresh_token': '<YOUR_REFRESH_TOKEN>',
        'domain': '<YOUR_BITRIX24_THIRD_LEVEL_DOMAIN>',
        'client_id': '<YOUR_CLIENT_ID>',
        'client_secret': '<YOUR_CLIENT_SECRET>'
    }

    def check_access_data(self):
        for i in self.access_data:
            if '<YOUR' in self.access_data[i]:
                self.skipTest('Add your access data')

    def setUp(self):
        self.check_access_data()
        self.bx24 = Bitrix24(
            self.access_data['domain'],
            self.access_data['auth_token'],
            self.access_data['refresh_token'],
            self.access_data['client_id'],
            self.access_data['client_secret']
        )

    def test_get_tokens(self):
        tokens = self.bx24.get_tokens()
        self.assertEqual(tokens, {'auth_token': self.access_data['auth_token'],
                                  'refresh_token': self.access_data['refresh_token']})

    def test_refresh_tokens(self):
        self.assertTrue(self.bx24.refresh_tokens())

    def test_call_app_info(self):
        result = self.bx24.call('app.info')
        self.assertTrue('STATUS' in result['result'])

    def test_call_methods(self):
        result = self.bx24.call('methods', {'scope': ''})
        self.assertTrue(isinstance(result['result'], list))

    def test_call_batch(self):
        result = self.bx24.call('batch', {'halt': 0, 'cmd': {0: 'scope', 1: 'methods'}})
        self.assertTrue(isinstance(result['result'], dict))

    def test_call_with_empty_method(self):
        self.assertRaises(Exception, self.bx24.call, '')

    def test_call_non_exists_function(self):
        result = self.bx24.call('--------------------')
        self.assertEqual(result['error'], 'ERROR_METHOD_NOT_FOUND')


class TestBitrix24WithIncorrectAccessTokens(unittest.TestCase):
    def setUp(self):
        self.bx24 = Bitrix24('test', 'auth_token', 'refresh_token')

    def test_get_tokens(self):
        tokens = self.bx24.get_tokens()
        self.assertEqual(tokens, {'auth_token': 'auth_token', 'refresh_token': 'refresh_token'})

    def test_fail_refresh_tokens(self):
        result = self.bx24.refresh_tokens()
        self.assertTrue('error' in result)

    def test_fail_call(self):
        result = self.bx24.call('app.info')
        self.assertEqual(result['error'], 'invalid_token')

    def test_call_with_empty_method(self):
        self.assertRaises(Exception, self.bx24.call, '')

    def test_call_non_exists_function(self):
        result = self.bx24.call('--------------------')
        self.assertEqual(result['error'], 'ERROR_METHOD_NOT_FOUND')


if __name__ == '__main__':
    unittest.main()
