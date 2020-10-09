from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyAddContact(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.add_contact(title='Mr.', firstName='Alejandro')

        call_mock.assert_called_once_with('AddContact', title='Mr.', firstName='Alejandro')
        self.assertEqual(response, call_mock.return_value)
