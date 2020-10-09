from unittest import TestCase

from rrpproxy.utils.rrpproxy_api_down_exception import RRPProxyAPIDownException


class TestRRPProxyAPIDownException(TestCase):
    def test_rrpproxy_api_down_exception_inherits_from_exception(self):
        self.assertIsInstance(RRPProxyAPIDownException(), Exception)
