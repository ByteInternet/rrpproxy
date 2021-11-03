from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyQueryForeignTransferList(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.query_foreign_transfer_list()

        call_mock.assert_called_once_with('QueryForeignTransferList')
        self.assertEqual(response, call_mock.return_value)

    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_with_kwargs_correctly(self, call_mock):
        response = self.proxy.query_foreign_transfer_list(domain='dogsarecool*')

        call_mock.assert_called_once_with('QueryForeignTransferList', domain='dogsarecool*')
        self.assertEqual(response, call_mock.return_value)
