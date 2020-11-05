from unittest.case import TestCase

from rrpproxy.utils.rrp_proxy_internal_status_exception import RRPProxyInternalStatusException


class TestRRPProxyInteralStatusException(TestCase):
    def test_inherits_from_exception(self):
        self.assertIsInstance(RRPProxyInternalStatusException(code=400), Exception)

    def test_sets_passed_in_code(self):
        exception = RRPProxyInternalStatusException(code=400)

        self.assertEqual(exception.code, 400)
