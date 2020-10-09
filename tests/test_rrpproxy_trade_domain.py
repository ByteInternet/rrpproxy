from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyTradeDomain(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.trade_domain(domain='example.com', ownercontact0='CONTACT-A')

        call_mock.assert_called_once_with('TradeDomain', domain='example.com', ownercontact0='CONTACT-A')
        self.assertEqual(response, call_mock.return_value)
