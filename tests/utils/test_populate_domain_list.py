from unittest.case import TestCase

from rrpproxy.utils.populate_domain_list import populate_domain_list


class TestPopulateDomainList(TestCase):
    def setUp(self):
        self.rrpproxy_output_data = {
            'property': {
                'domain': ['domain1.nl', 'domain2.nl', 'domain3.nl'],
                'domain status': ['ACTIVE', 'INACTIVE', 'ACTIVE'],
                'domain updated date': ['2018-06-12 16:59:00', '2018-06-12 16:40:00', '2018-06-12 16:30:00'],
                'nameserver': ['dummy1;dummy;dummy', 'dummy2;dummy;dummy', 'dummy3;dummy;dummy'],
                'admincontact': ['admin1', 'admin2', 'admin3'],
                'techcontact': ['tech1', 'tech2', 'tech3'],
                'billingcontact': ['billing1', 'billing2', 'billing3'],
                'ownercontact': ['owner1', 'owner2', 'owner3'],
            }
        }

    def test_returns_data_in_the_correct_format(self):
        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertEqual(domain_list, [
            {'name': 'domain1.nl', 'status': 'ACTIVE', 'updated_date': '2018-06-12 16:59:00',
             'nameserver': 'dummy1;dummy;dummy', 'admin_contact': 'admin1', 'tech_contact': 'tech1',
             'billing_contact': 'billing1', 'owner_contact': 'owner1'},
            {'name': 'domain2.nl', 'status': 'INACTIVE', 'updated_date': '2018-06-12 16:40:00',
             'nameserver': 'dummy2;dummy;dummy', 'admin_contact': 'admin2', 'tech_contact': 'tech2',
             'billing_contact': 'billing2', 'owner_contact': 'owner2'},
            {'name': 'domain3.nl', 'status': 'ACTIVE', 'updated_date': '2018-06-12 16:30:00',
             'nameserver': 'dummy3;dummy;dummy', 'admin_contact': 'admin3', 'tech_contact': 'tech3',
             'billing_contact': 'billing3', 'owner_contact': 'owner3'},
        ])

    def test_returns_data_without_nameserver_if_empty(self):
        self.rrpproxy_output_data['property']['nameserver'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('nameserver', domain_list[0])

    def test_returns_data_without_admin_contact_if_empty(self):
        self.rrpproxy_output_data['property']['admincontact'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('admin_contact', domain_list[0])

    def test_returns_data_without_tech_contact_if_empty(self):
        self.rrpproxy_output_data['property']['techcontact'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('tech_contact', domain_list[0])

    def test_returns_data_without_billing_contact_if_empty(self):
        self.rrpproxy_output_data['property']['billingcontact'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('billing_contact', domain_list[0])

    def test_returns_data_without_owner_contact_if_empty(self):
        self.rrpproxy_output_data['property']['ownercontact'][0] = ''

        domain_list = populate_domain_list(self.rrpproxy_output_data)

        self.assertNotIn('owner_contact', domain_list[0])
