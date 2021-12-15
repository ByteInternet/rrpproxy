from unittest.mock import Mock

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestGetDomainListFromAccount(TestRRPProxyBase):
    def setUp(self):
        super().setUp()

        self.time_sleep_mock = self.set_up_patch('rrpproxy.rrpproxy.time.sleep')
        self.proxy.query_domain_list = Mock()
        self.proxy.query_domain_list.return_value = self.sample_query_domain_list

    def test_calls_get_domain_list_with_details_correctly(self):
        self.proxy.get_last_updated_domains_with_details = Mock()
        self.proxy.get_last_updated_domains_with_details.return_value = []

        self.proxy.get_domain_list_from_account(one_argument='one_value')

        self.proxy.get_last_updated_domains_with_details.assert_called_once_with(retrieve_all=True,
                                                                                 one_argument='one_value')

    def test_returns_array_of_domains(self):
        ret = self.proxy.get_domain_list_from_account()

        self.assertEqual(ret, ['domain1.nl', 'domain2.nl'])
