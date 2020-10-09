from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyAddDomain(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.add_domain('example.com', 1, ownerContact0='ABC')

        call_mock.assert_called_once_with('AddDomain', domain='example.com', period=1, ownerContact0='ABC')
        self.assertEqual(response, call_mock.return_value)
