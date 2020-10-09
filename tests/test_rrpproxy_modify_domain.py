from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyModifyDomain(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.modify_domain('example.com', renewalmode='autoexpire')

        call_mock.assert_called_once_with('ModifyDomain', domain='example.com', renewalmode='autoexpire')
        self.assertEqual(response, call_mock.return_value)
