from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyCheckDomainTransfer(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.check_domain_transfer(domain='hypernode.com', auth='hjd7s', action='approve')

        call_mock.assert_called_once_with('CheckDomainTransfer', domain='hypernode.com', auth='hjd7s', action='approve')
        self.assertEqual(response, call_mock.return_value)
