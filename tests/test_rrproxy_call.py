from unittest.mock import patch

import requests

from rrpproxy.utils.rrpproxy_api_down_exception import RRPProxyAPIDownException
from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyCall(TestRRPProxyBase):
    def test_call_calls_request_get_with_correct_url_and_parameters(self):
        query_params = self.proxy.query_params.copy()
        query_params.update({'some_parameter': 'some_value', 'other_parameter': 'other_value', 'command': 'CheckDomain'})

        self.proxy.call('CheckDomain', some_parameter='some_value', other_parameter='other_value')

        self.get_mock.assert_called_once_with(self.proxy.api_url, params=query_params)

    def test_call_calls_response_raise_for_status(self):
        self.proxy.call('CheckDomain', some_parameter='some_value', other_parameter='other_value')

        self.get_mock.return_value.raise_for_status.assert_called_once_with()

    def test_call_raises_rrpproxy_api_down_exception_when_there_is_a_connection_error(self):
        self.get_mock.side_effect = requests.ConnectionError

        with self.assertRaises(RRPProxyAPIDownException):
            self.proxy.call('CheckDomain', some_parameter='some_value', other_parameter='other_value')

    def test_call_logs_http_error_with_exception_if_api_returns_http_error(self):
        self.get_mock.side_effect = requests.HTTPError

        self.proxy.call('CheckDomain', some_parameter='some_value', other_parameter='other_value')

        self.logger_mock.error.assert_called_once_with('Error returned from API Call', exc_info=True)

    @patch('rrpproxy.RRPProxy.response_to_dict')
    def test_call_returns_response_to_dict(self, response_to_dict_mock):
        response = self.proxy.call('CheckDomain', domain='hypernode.com')

        response_to_dict_mock.assert_called_once_with(self.get_mock.return_value.text)
        self.assertEqual(response, response_to_dict_mock.return_value)
