from unittest.mock import Mock, patch, call

from rrpproxy.utils.populate_domain_list import populate_domain_list
from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyGetDomainWithDetails(TestRRPProxyBase):
    def setUp(self):
        super().setUp()

        self.domain = 'abc.com'
        self.proxy.query_domain_list = Mock()
        self.query_domain_list_data = {
            'property': {
                'domain': ['abc.com'],
                'domain status': ['ACTIVE'],
                'domain updated date': ['2021-01-21'],
                'nameserver': ['ns1;ns2;ns3'],
                'admincontact': ['CNT-123'],
                'techcontact': ['CNT-123'],
                'billingcontact': ['CNT-123'],
                'ownercontact': ['CNT-123'],
            }
        }
        self.proxy.query_domain_list.return_value = self.query_domain_list_data

    def test_calls_query_domain_list_correctly(self):
        self.proxy.get_domain_with_details(self.domain)

        self.proxy.query_domain_list.assert_called_once_with(domain=self.domain, type='ALL')
    
    def test_returns_proper_details_of_domain(self):
        res = self.proxy.get_domain_with_details(self.domain)

        self.assertEqual(res, populate_domain_list(self.query_domain_list_data))
