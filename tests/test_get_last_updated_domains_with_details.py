from unittest.mock import Mock, patch, call

from rrpproxy.utils.populate_domain_list import populate_domain_list
from tests.test_rrpproxy_base import TestRRPProxyBase


class TestGetLastUpdatedDomainsWithDetails(TestRRPProxyBase):
    def setUp(self):
        super().setUp()

        self.time_sleep_mock = self.set_up_patch('rrpproxy.rrpproxy.time.sleep')
        self.proxy.query_domain_list = Mock()
        self.proxy.query_domain_list.return_value = self.sample_query_domain_list

    def test_calls_query_domain_list_correctly(self):
        index = 3

        self.proxy.get_last_updated_domains_with_details(index=index)

        self.proxy.query_domain_list.assert_called_once_with(first=index, type='ALL', orderby='DOMAINUPDATEDDATE',
                                                             order='DESC')

    @patch('rrpproxy.rrpproxy.populate_domain_list')
    def test_calls_query_domain_list_once_if_retrieve_all_is_set_to_false(self, _):
        self.proxy.query_domain_list.side_effect = [
            {
                'property': {
                    'last': ['2'],
                    'total': ['4'],
                    'domain': ['domain1.nl', 'domain2.nl']
                }
            },
            {
                'property': {
                    'last': ['4'],
                    'total': ['4'],
                    'domain': ['domZain3.nl', 'domain4.nl']
                }
            }
        ]

        self.proxy.get_last_updated_domains_with_details(retrieve_all=False)

        self.proxy.query_domain_list.assert_called_once_with(first=0, type='ALL', orderby='DOMAINUPDATEDDATE', order='DESC')

    @patch('rrpproxy.rrpproxy.populate_domain_list')
    def test_calls_query_domain_list_n_times_if_retrieve_all_is_true_and_there_are_more_domains_in_next_page(self, _):
        self.proxy.query_domain_list.side_effect = [
            {
                'property': {
                    'last': ['2'],
                    'total': ['4'],
                    'domain': ['domain1.nl', 'domain2.nl']
                }
            },
            {
                'property': {
                    'last': ['4'],
                    'total': ['4'],
                    'domain': ['domZain3.nl', 'domain4.nl']
                }
            }
        ]

        self.proxy.get_last_updated_domains_with_details(retrieve_all=True)

        self.proxy.query_domain_list.assert_has_calls([
            call(first=0, type='ALL', orderby='DOMAINUPDATEDDATE', order='DESC'),
            call(first=3, type='ALL', orderby='DOMAINUPDATEDDATE', order='DESC')
        ])

    def test_returns_domain_list_when_retrieve_all_is_true_but_there_are_no_more_items_on_the_next_page(self):
        ret = self.proxy.get_last_updated_domains_with_details(retrieve_all=True)

        self.assertEqual(ret, populate_domain_list(self.proxy.query_domain_list.return_value))

    def test_returns_empty_array_when_there_are_no_more_items_on_the_next_page_and_domain_list_is_absent(self):
        self.proxy.query_domain_list.return_value = {
            'property': {
                'last': ['201'],
                'total': ['200']
            }
        }

        ret = self.proxy.get_last_updated_domains_with_details()

        self.assertEqual(ret, [])

    @patch('rrpproxy.rrpproxy.populate_domain_list')
    def test_calls_sleep_when_there_are_more_domains_on_the_next_call_and_retrieve_all_is_true(self, _):
        self.proxy.query_domain_list.side_effect = [
            {
                'property': {
                    'last': ['2'],
                    'total': ['4'],
                    'domain': ['domain1.nl', 'domain2.nl']
                }
            },
            {
                'property': {
                    'last': ['4'],
                    'total': ['4'],
                    'domain': ['domZain3.nl', 'domain4.nl']
                }
            }
        ]

        self.proxy.get_last_updated_domains_with_details(retrieve_all=True)

        self.time_sleep_mock.assert_called_once_with(1)

    @patch('rrpproxy.rrpproxy.populate_domain_list')
    def test_calls_sleep_with_correct_amount_of_seconds_if_time_between_calls_is_specified(self, _):
        self.proxy.query_domain_list.side_effect = [
            {
                'property': {
                    'last': ['2'],
                    'total': ['4'],
                    'domain': ['domain1.nl', 'domain2.nl']
                }
            },
            {
                'property': {
                    'last': ['4'],
                    'total': ['4'],
                    'domain': ['domain3.nl', 'domain4.nl']
                }
            }
        ]

        self.proxy.get_last_updated_domains_with_details(retrieve_all=True, time_between_calls_in_seconds=5)

        self.time_sleep_mock.assert_called_once_with(5)

    def test_returns_domain_list_and_a_recursive_call_with_another_index_when_there_are_more_domains_on_the_next_page(
            self):
        first_response = {
            'property': {
                'last': ['2'],
                'total': ['4'],
                'domain': ['domain1.nl', 'domain2.nl'],
                'domain status': ['ACTIVE', 'ACTIVE'],
                'domain updated date': ['2021-01-21', '2021-01-21'],
                'nameserver': ['ns1;ns2;ns3', 'ns1;ns2;ns3'],
                'admincontact': ['CNT-123', 'CNT-456'],
                'techcontact': ['CNT-123', 'CNT-456'],
                'billingcontact': ['CNT-123', 'CNT-456'],
                'ownercontact': ['CNT-123', 'CNT-456'],
            }
        }
        second_response = {
            'property': {
                'last': ['4'],
                'total': ['4'],
                'domain': ['domain3.nl', 'domain4.nl'],
                'domain status': ['ACTIVE', 'ACTIVE'],
                'domain updated date': ['2021-01-21', '2021-01-21'],
                'nameserver': ['ns1;ns2;ns3', 'ns1;ns2;ns3'],
                'admincontact': ['CNT-123', 'CNT-456'],
                'techcontact': ['CNT-123', 'CNT-456'],
                'billingcontact': ['CNT-123', 'CNT-456'],
                'ownercontact': ['CNT-123', 'CNT-456'],
            }
        }
        self.proxy.query_domain_list.side_effect = [first_response, second_response]

        ret = self.proxy.get_last_updated_domains_with_details(retrieve_all=True)

        self.assertEqual(ret, populate_domain_list(first_response) + populate_domain_list(second_response))
