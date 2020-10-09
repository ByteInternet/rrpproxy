from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyModifyContact(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.modify_contact(contact='CONTACT-A', city='Amsterdam')

        call_mock.assert_called_once_with('ModifyContact', contact='CONTACT-A', city='Amsterdam')
        self.assertEqual(response, call_mock.return_value)
