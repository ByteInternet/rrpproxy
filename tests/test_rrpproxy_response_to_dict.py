from unittest.mock import MagicMock

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyResponseToDict(TestRRPProxyBase):
    def test_response_to_dict_returns_a_dict_of_each_line_of_response_without_response_line_and_eof(self):
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 210\ndescription = Domain name available\nruntime = 0.267\nqueuetime = 0\nEOF\n')

        response = self.proxy.call('CheckDomain', domain='hypernode.com')

        self.assertEqual(response, {
            'code': '210',
            'description': 'Domain name available',
            'runtime': '0.267',
            'queuetime': '0'
        })

    def test_response_to_dict_returns_dict_of_each_line_including_property_object(self):
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 210\ndescription = Domain name available\nproperty[AMOUNT][0] = 100\nproperty[TYPE][0] = value\nruntime = 0.267\nqueuetime = 0\nEOF\n')
        response = self.proxy.call('Command', domain='hypernode.com')

        self.assertEqual(response, {
            'code': '210',
            'description': 'Domain name available',
            'property': {
                'AMOUNT': ['100'],
                'TYPE': ['value']
            },
            'runtime': '0.267',
            'queuetime': '0'
        })
