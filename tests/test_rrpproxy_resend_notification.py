from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyResendNotification(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.resend_notification(type='domaintransfer', object='some_object', reason='some reason')

        call_mock.assert_called_once_with('ResendNotification', type='domaintransfer', object='some_object', reason='some reason')
        self.assertEqual(response, call_mock.return_value)
