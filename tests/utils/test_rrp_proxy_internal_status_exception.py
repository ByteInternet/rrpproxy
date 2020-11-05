from unittest.case import TestCase

from rrpproxy.utils.rrp_proxy_internal_status_exception import RRPProxyInternalStatusException


class TestRRPProxyInteralStatusException(TestCase):
    def test_inherits_from_exception(self):
        self.assertIsInstance(RRPProxyInternalStatusException(response_dict={}), Exception)

    def test_sets_passed_in_code(self):
        exception = RRPProxyInternalStatusException(response_dict={'my': 'custom', 'response': 'dict'})

        self.assertCountEqual(exception.response_dict, {'my': 'custom', 'response': 'dict'})
