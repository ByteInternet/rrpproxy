from unittest.mock import MagicMock

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyResponseToDict(TestRRPProxyBase):

    def test_response_to_dict_returns_a_dict_of_each_line_of_response_without_response_line_and_eof(self):
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 210\ndescription = Domain name available\nruntime = 0.267\nqueuetime = 0\nEOF\n')

        response = self.proxy.call('CheckDomain', domain='hypernode.com')

        self.assertEqual(response, {
            'code': 210,
            'description': 'Domain name available',
            'runtime': '0.267',
            'queuetime': '0'
        })

    def test_response_to_dict_returns_dict_of_each_line_including_property_object(self):
        rrpproxy_response = "\n".join([
            '[RESPONSE]',
            'code = 210',
            'description = Domain name available',
            'property[AMOUNT][0] = 100',
            'property[TYPE][0] = value',
            'property[PARAMETER 0][0] = value 1',
            'property[PARAMETER-1][0] = value-2',
            'runtime = 0.267',
            'queuetime = 0',
            'EOF\n'
        ])
        self.get_mock.return_value = MagicMock(text=rrpproxy_response)
        response = self.proxy.call('Command', domain='hypernode.com')

        self.assertEqual(response, {
            'code': 210,
            'description': 'Domain name available',
            'property': {
                'AMOUNT': ['100'],
                'TYPE': ['value'],
                'PARAMETER 0': ['value 1'],
                'PARAMETER-1': ['value-2'],
            },
            'runtime': '0.267',
            'queuetime': '0'
        })
