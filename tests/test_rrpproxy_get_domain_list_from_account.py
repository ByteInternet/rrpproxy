from unittest.mock import Mock

from tests.test_rrpproxy_base import TestRRPProxyBase


class TestGetDomainListFromAccount(TestRRPProxyBase):
    def setUp(self):
        super().setUp()

        self.time_sleep_mock = self.set_up_patch('rrpproxy.rrpproxy.time.sleep')
        self.proxy.query_domain_list = Mock()
        self.proxy.query_domain_list.return_value = {'property': {
                'last': ['2'],
                'total': ['2'],
                'domain': ['domain1.nl', 'domain2.nl']
        }}

    def test_calls_query_domain_list_correctly(self):
        index = 3
        self.proxy.get_domain_list_from_account(index=index)

        self.proxy.query_domain_list.assert_called_once_with(first=index)

    def test_returns_domain_list_when_there_are_no_more_items_on_the_next_page(self):
        ret = self.proxy.get_domain_list_from_account()

        self.assertEqual(ret, self.proxy.query_domain_list.return_value['property']['domain'])

    def test_returns_empty_array_when_there_are_no_more_items_on_the_next_page_and_domain_list_is_absent(self):
        self.proxy.query_domain_list.return_value = {
            'property': {
                'last': ['201'],
                'total': ['200'],
            }
        }

        ret = self.proxy.get_domain_list_from_account()

        self.assertEqual(ret, [])

    def test_calls_sleep_when_there_are_more_domains_on_the_next_call(self):
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

        self.proxy.get_domain_list_from_account()

        self.time_sleep_mock.assert_called_once_with(1)

    def test_calls_sleep_with_correct_amount_of_seconds_if_time_between_calls_is_specified(self):
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

        self.proxy.get_domain_list_from_account(time_between_calls_in_seconds=5)

        self.time_sleep_mock.assert_called_once_with(5)

    def test_returns_domain_list_and_a_recursive_call_with_another_index_when_there_are_more_domains_on_the_next_page(
            self):
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

        ret = self.proxy.get_domain_list_from_account()

        self.assertEqual(ret, ['domain1.nl', 'domain2.nl', 'domain3.nl', 'domain4.nl'])
