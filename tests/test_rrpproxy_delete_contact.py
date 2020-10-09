from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyDeleteContact(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.delete_contact('CONTACT-B')

        call_mock.assert_called_once_with('DeleteContact', contact='CONTACT-B')
        self.assertEqual(response, call_mock.return_value)
