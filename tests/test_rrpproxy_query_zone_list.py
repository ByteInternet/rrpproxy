from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyQueryZoneList(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.query_zone_list()

        call_mock.assert_called_once_with('QueryZoneList')
        self.assertEqual(response, call_mock.return_value)
