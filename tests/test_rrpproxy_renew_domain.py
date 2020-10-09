from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyRenewDomain(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.renew_domain('example.com', period=5, expiration=2025)

        call_mock.assert_called_once_with('RenewDomain', domain='example.com', period=5, expiration=2025)
        self.assertEqual(response, call_mock.return_value)
