from unittest.case import TestCase

from rrpproxy.utils.populate_domain_list import populate_domain_list


class TestPopulateDomainList(TestCase):
    def test_returns_data_in_the_correct_format(self):
        rrpproxy_output_data = {
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

        domain_list = populate_domain_list(rrpproxy_output_data)

        self.assertEqual(len(domain_list), len(rrpproxy_output_data['property']['domain']))
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
