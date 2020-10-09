from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyCheckContact(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.check_contact('CONTACT-A')

        call_mock.assert_called_once_with('CheckContact', contact='CONTACT-A')
        self.assertEqual(response, call_mock.return_value)
