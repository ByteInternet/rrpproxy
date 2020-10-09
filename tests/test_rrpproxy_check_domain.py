from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyCheckDomain(TestRRPProxyBase):
    def setup(self):
        super().setUp()

    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.check_domain('example.com')

        call_mock.assert_called_once_with('CheckDomain', domain='example.com')
        self.assertEqual(response, call_mock.return_value)
