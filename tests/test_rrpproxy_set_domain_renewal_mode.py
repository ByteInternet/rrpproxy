from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxySetDomainRenewalMode(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.set_domain_renewal_mode(domain='hypernode.com', token='%$GF', renewalmode='renewalmode')

        call_mock.assert_called_once_with('SetDomainRenewalmode', domain='hypernode.com', token='%$GF', renewalmode='renewalmode')
        self.assertEqual(response, call_mock.return_value)
