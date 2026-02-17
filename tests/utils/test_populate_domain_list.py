from unittest.case import TestCase

from rrpproxy.utils.populate_domain_list import (
    populate_domain_list,
    RRPPROXY_DOMAIN_FIELDS,
)


class TestPopulateDomainList(TestCase):
    def setUp(self):
        self.rrpproxy_output_data = {
            'property': {
                'domain': ['domain1.nl', 'domain2.nl', 'domain3.nl'],
                'domain status': ['ACTIVE', 'INACTIVE', 'ACTIVE'],
                'domain updated date': [
                    '2018-06-12 16:59:00',
                    '2018-06-12 16:40:00',
                    '2018-06-12 16:30:00',
                ],
                'nameserver': [
                    'dummy1;dummy;dummy',
                    'dummy2;dummy;dummy',
                    'dummy3;dummy;dummy',
                ],
                'admincontact': ['admin1', 'admin2', 'admin3'],
                'techcontact': ['tech1', 'tech2', 'tech3'],
                'billingcontact': ['billing1', 'billing2', 'billing3'],
                'ownercontact': ['owner1', 'owner2', 'owner3'],
                'domain auth code': ['authcode1', 'authcode2', 'authcode3'],
            }
        }

    def test_rrpproxy_domain_fields_are_correct(self):
        self.assertEqual(
            RRPPROXY_DOMAIN_FIELDS,
            (
                'domain',
                'domain status',
                'domain updated date',
                'nameserver',
                'admincontact',
                'techcontact',
                'billingcontact',
                'ownercontact',
                'domain auth code',
            ),
        )

    def test_returns_data_in_the_correct_format(self):
        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertEqual(
            domain_list,
            [
                {
                    'domain': 'domain1.nl',
                    'domain status': 'ACTIVE',
                    'domain updated date': '2018-06-12 16:59:00',
                    'nameserver': 'dummy1;dummy;dummy',
                    'admincontact': 'admin1',
                    'techcontact': 'tech1',
                    'billingcontact': 'billing1',
                    'ownercontact': 'owner1',
                    'domain auth code': 'authcode1',
                },
                {
                    'domain': 'domain2.nl',
                    'domain status': 'INACTIVE',
                    'domain updated date': '2018-06-12 16:40:00',
                    'nameserver': 'dummy2;dummy;dummy',
                    'admincontact': 'admin2',
                    'techcontact': 'tech2',
                    'billingcontact': 'billing2',
                    'ownercontact': 'owner2',
                    'domain auth code': 'authcode2',
                },
                {
                    'domain': 'domain3.nl',
                    'domain status': 'ACTIVE',
                    'domain updated date': '2018-06-12 16:30:00',
                    'nameserver': 'dummy3;dummy;dummy',
                    'admincontact': 'admin3',
                    'techcontact': 'tech3',
                    'billingcontact': 'billing3',
                    'ownercontact': 'owner3',
                    'domain auth code': 'authcode3',
                },
            ],
        )

    def test_returns_data_without_nameserver_if_empty(self):
        self.rrpproxy_output_data['property']['nameserver'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('nameserver', domain_list[0])

    def test_returns_data_without_admin_contact_if_empty(self):
        self.rrpproxy_output_data['property']['admincontact'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('admincontact', domain_list[0])

    def test_returns_data_without_tech_contact_if_empty(self):
        self.rrpproxy_output_data['property']['techcontact'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('techcontact', domain_list[0])

    def test_returns_data_without_billing_contact_if_empty(self):
        self.rrpproxy_output_data['property']['billingcontact'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('billingcontact', domain_list[0])

    def test_returns_data_without_owner_contact_if_empty(self):
        self.rrpproxy_output_data['property']['ownercontact'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('ownercontact', domain_list[0])

    def test_returns_data_with_auth_code_if_present(self):
        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertEqual(domain_list[0]['domain auth code'], 'authcode1')
        self.assertEqual(domain_list[1]['domain auth code'], 'authcode2')
        self.assertEqual(domain_list[2]['domain auth code'], 'authcode3')

    def test_returns_data_without_auth_code_if_empty(self):
        self.rrpproxy_output_data['property']['domain auth code'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('domain auth code', domain_list[0])

    def test_returns_data_without_auth_code_if_field_missing(self):
        del self.rrpproxy_output_data['property']['domain auth code']

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('domain auth code', domain_list[0])
