from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyQueryDomainList(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.query_domain_list()

        call_mock.assert_called_once_with('QueryDomainList')
        self.assertEqual(response, call_mock.return_value)

    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_with_kwargs_correctly(self, call_mock):
        response = self.proxy.query_domain_list(domain='dogsarecool*')

        call_mock.assert_called_once_with('QueryDomainList', domain='dogsarecool*')
        self.assertEqual(response, call_mock.return_value)
