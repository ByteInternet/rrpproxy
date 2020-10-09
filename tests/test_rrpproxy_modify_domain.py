from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyModifyDomain(TestRRPProxyBase):
    def setup(self):
        super().setUp()

    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.modify_domain('example.com', renewalMode='autoexpire')

        call_mock.assert_called_once_with('ModifyDomain', domain='example.com', renewalMode='autoexpire')
        self.assertEqual(response, call_mock.return_value)
