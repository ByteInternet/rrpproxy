from unittest.mock import patch

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyGetZoneInfo(TestRRPProxyBase):
    @patch('rrpproxy.RRPProxy.call')
    def test_calls_call_correctly(self, call_mock):
        response = self.proxy.get_zone_info(zone='some_zone', domain='hypernode.com')

        call_mock.assert_called_once_with('GetZoneInfo', zone='some_zone', domain='hypernode.com')
        self.assertEqual(response, call_mock.return_value)
