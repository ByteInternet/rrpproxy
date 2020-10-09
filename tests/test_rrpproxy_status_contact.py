from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyStatusContact(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.status_contact(contact='CONTACT-A', auth='$%FS')

        call_mock.assert_called_once_with('StatusContact', contact='CONTACT-A', auth='$%FS')
        self.assertEqual(response, call_mock.return_value)
