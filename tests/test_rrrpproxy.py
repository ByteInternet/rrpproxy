from unittest import TestCase, mock
from unittest.mock import MagicMock, patch

from rrpproxy import RRPProxy


class TestRRRPProxy(TestCase):
    def setUp(self):
        self.get_mock = self.set_up_patch('requests.get')
        self.username = 'dummy_username'
        self.password = 'secret_password'
        self.proxy = RRPProxy(self.username, self.password, True)

    def set_up_patch(self, name, *args, **kwargs):
        patch = mock.patch(name, *args, **kwargs)
        self.addCleanup(patch.stop)
        return patch.start()

    def test_init_sets_correct_api_url_when_using_sandbox_environment(self):
        self.assertEqual(self.proxy.api_url,
                         'https://api-ote.rrpproxy.net/api/call.cgi?s_login={}&s_pw={}&s_opmode=OTE'.format(self.username, self.password))

    def test_init_sets_correct_api_url_when_using_live_environment(self):
        self.proxy = RRPProxy(self.username, self.password, False)

        self.assertEqual(self.proxy.api_url,
                         'https://api.rrpproxy.net/api/call.cgi?s_login={}&s_pw={}'.format(self.username, self.password))

    def test_call_calls_request_get_with_correct_url(self):
        self.proxy.call('CheckDomain', some_parameter='some_value')

        self.get_mock.assert_called_once_with(self.proxy.api_url + '&some_parameter=some_value&command=CheckDomain')

    @patch('rrpproxy.RRPProxy.response_to_dict')
    def test_call_returns_response_to_dict(self, response_to_dict_mock):
        response = self.proxy.call('CheckDomain', domain='hypernode.com')

        response_to_dict_mock.assert_called_once_with(self.get_mock.return_value.text)
        self.assertEqual(response, response_to_dict_mock.return_value)

    def test_response_to_dict_returns_a_dict_of_each_line_of_response_without_response_line_and_eof(self):
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 210\ndescription = Domain name available\nruntime = 0.267\nqueuetime = 0\nEOF\n')

        response = self.proxy.call('CheckDomain', domain='hypernode.com')

        self.assertEqual(response, {
            'code': '210',
            'description': 'Domain name available',
            'runtime': '0.267',
            'queuetime': '0'
        })

    def test_response_to_dict_returns_dict_of_each_line_including_property_object(self):
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 210\ndescription = Domain name available\nproperty[AMOUNT][0] = 100\nproperty[TYPE][0] = value\nruntime = 0.267\nqueuetime = 0\nEOF\n')
        response = self.proxy.call('Command', domain='hypernode.com')

        self.assertEqual(response, {
            'code': '210',
            'description': 'Domain name available',
            'property': {
                'AMOUNT': ['100'],
                'TYPE': ['value']
            },
            'runtime': '0.267',
            'queuetime': '0'
        })

    @patch('rrpproxy.RRPProxy.call')
    def test_add_contact_calls_call_correctly(self, call_mock):
        response = self.proxy.add_contact(title='Mr.', firstName='Alejandro')

        call_mock.assert_called_once_with('AddContact', title='Mr.', firstName='Alejandro')
        self.assertEqual(response, call_mock.return_value)

    @patch('rrpproxy.RRPProxy.call')
    def test_add_domain_calls_call_correctly(self, call_mock):
        response = self.proxy.add_domain('example.com', 1, ownerContact0='ABC')

        call_mock.assert_called_once_with('AddDomain', domain='example.com', period=1, ownerContact0='ABC')
        self.assertEqual(response, call_mock.return_value)

    @patch('rrpproxy.RRPProxy.call')
    def test_check_domain_calls_call_correctly(self, call_mock):
        response = self.proxy.check_domain('example.com')

        call_mock.assert_called_once_with('CheckDomain', domain='example.com')
        self.assertEqual(response, call_mock.return_value)

    @patch('rrpproxy.RRPProxy.call')
    def test_delete_domain_calls_call_correctly(self, call_mock):
        response = self.proxy.delete_domain('example.com')

        call_mock.assert_called_once_with('DeleteDomain', domain='example.com')
        self.assertEqual(response, call_mock.return_value)

    @patch('rrpproxy.RRPProxy.call')
    def test_modify_domain_calls_call_correctly(self, call_mock):
        response = self.proxy.modify_domain('example.com', renewalMode='autoexpire')

        call_mock.assert_called_once_with('ModifyDomain', domain='example.com', renewalMode='autoexpire')
        self.assertEqual(response, call_mock.return_value)

    @patch('rrpproxy.RRPProxy.call')
    def test_renew_domain_calls_call_correctly(self, call_mock):
        response = self.proxy.renew_domain('example.com', period=5, expiration=2025)

        call_mock.assert_called_once_with('RenewDomain', domain='example.com', period=5, expiration=2025)
        self.assertEqual(response, call_mock.return_value)

    @patch('rrpproxy.RRPProxy.call')
    def test_status_domain_calls_call_correctly(self, call_mock):
        response = self.proxy.status_domain('example.com')

        call_mock.assert_called_once_with('StatusDomain', domain='example.com')
        self.assertEqual(response, call_mock.return_value)
