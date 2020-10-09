from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxySetAuthCode(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.set_auth_code(domain='hypernode.com', auth='%$GF', action='SET')

        call_mock.assert_called_once_with('SetAuthCode', domain='hypernode.com', auth='%$GF', action='SET')
        self.assertEqual(response, call_mock.return_value)
