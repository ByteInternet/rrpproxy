from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyQueryTransferList(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.query_transfer_list()

        call_mock.assert_called_once_with('QueryTransferList')
        self.assertEqual(response, call_mock.return_value)

    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_with_kwargs_correctly(self, call_mock):
        response = self.proxy.query_transfer_list(domain='dogsarecool*')

        call_mock.assert_called_once_with('QueryTransferList', domain='dogsarecool*')
        self.assertEqual(response, call_mock.return_value)
