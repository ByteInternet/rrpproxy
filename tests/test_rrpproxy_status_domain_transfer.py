from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyStatusDomainTransfer(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.status_domain_transfer('example.com')

        call_mock.assert_called_once_with('StatusDomainTransfer', domain='example.com')
        self.assertEqual(response, call_mock.return_value)
