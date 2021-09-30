from unittest.mock import patch, MagicMock

import requests
from requests import HTTPError

from rrpproxy.utils.rrp_proxy_internal_status_exception import RRPProxyInternalStatusException
from rrpproxy.utils.rrpproxy_api_down_exception import RRPProxyAPIDownException
from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyCall(TestRRPProxyBase):
    def setUp(self):
        super(TestRRPProxyCall, self).setUp()
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 200\nEOF\n')

    def test_call_calls_session_get_with_correct_url_and_parameters(self):
        query_params = self.proxy.query_params.copy()
        query_params.update({'some_parameter': 'some_value', 'other_parameter': 'other_value', 'command': 'CheckDomain'})

        self.proxy.call('CheckDomain', some_parameter='some_value', other_parameter='other_value')

        self.proxy.session.get.assert_called_once_with(self.proxy.api_url, params=query_params)

    def test_call_calls_response_raise_for_status(self):
        self.proxy.call('CheckDomain', some_parameter='some_value', other_parameter='other_value')

        self.proxy.session.get.return_value.raise_for_status.assert_called_once_with()

    def test_call_raises_rrpproxy_api_down_exception_when_there_is_a_connection_error(self):
        self.get_mock.side_effect = requests.ConnectionError

        with self.assertRaises(RRPProxyAPIDownException):
            self.proxy.call('CheckDomain', some_parameter='some_value', other_parameter='other_value')

    def test_call_logs_http_error_with_exception_if_api_returns_http_error(self):
        self.get_mock.side_effect = requests.HTTPError

        with self.assertRaises(HTTPError):
            self.proxy.call('CheckDomain', some_parameter='some_value', other_parameter='other_value')

        self.logger_mock.error.assert_called_once_with('Error returned from API Call', exc_info=True)

    @patch('rrpproxy.RRPProxy.response_to_dict')
    def test_call_returns_response_to_dict(self, response_to_dict_mock):
        response_to_dict_mock.return_value = {'code': 200}

        response = self.proxy.call('CheckDomain', domain='hypernode.com')

        response_to_dict_mock.assert_called_once_with(self.get_mock.return_value.text)
        self.assertEqual(response, response_to_dict_mock.return_value)

    def test_raises_rrp_proxy_internal_status_exception_if_code_is_400(self):
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 400\nEOF\n')

        with self.assertRaises(RRPProxyInternalStatusException) as cm:
            self.proxy.call('CheckDomain', domain='hypernode.com')
        self.maxDiff=None
        self.assertEqual(cm.exception.args[0], ("Request was successfully handled, but RRP returned internal status "
                                                "code '400'. Please investigate and handle accordingly.",))
        self.assertCountEqual(cm.exception.response_dict, {'code': 400})

    def test_raises_rrp_proxy_internal_status_exception_if_code_is_higher_than_400(self):
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 401\nEOF\n')

        with self.assertRaises(RRPProxyInternalStatusException) as cm:
            self.proxy.call('CheckDomain', domain='hypernode.com')

        self.assertEqual(cm.exception.args[0], ("Request was successfully handled, but RRP returned internal status "
                                                "code '401'. Please investigate and handle accordingly.",))
        self.assertCountEqual(cm.exception.response_dict, {'code': 401})

    def test_raises_rrp_proxy_internal_status_exception_with_error_description_if_available(self):
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 400\ndescription = my error\nEOF\n')

        with self.assertRaises(RRPProxyInternalStatusException) as cm:
            self.proxy.call('CheckDomain', domain='hypernode.com')

        self.assertEqual(cm.exception.args[0], ("Request was successfully handled, but RRP returned internal status "
                                                "code '400'. Please investigate and handle accordingly. Description: "
                                                "my error",))
        self.assertCountEqual(cm.exception.response_dict, {'code': 400, 'description': 'my error'})

    def test_does_not_raise_rrp_proxy_internal_status_exception_if_code_is_lower_than_400(self):
        self.get_mock.return_value = MagicMock(text='[RESPONSE]\ncode = 399\nEOF\n')

        # Should not raise
        self.proxy.call('CheckDomain', domain='hypernode.com')
