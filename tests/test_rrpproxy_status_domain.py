from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyStatusDomain(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.status_domain('example.com')

        call_mock.assert_called_once_with('StatusDomain', domain='example.com')
        self.assertEqual(response, call_mock.return_value)
