from unittest import TestCase, mock

from rrpproxy import RRPProxy


class TestRRPProxyBase(TestCase):
    def setUp(self):
        self.get_mock = self.set_up_patch('requests.get')
        self.logger_mock = self.set_up_patch('rrpproxy.rrpproxy.logger')
        self.username = 'dummy_username'
        self.password = 'secret_password'
        self.proxy = RRPProxy(self.username, self.password, use_test_environment=True)
        self.sample_query_domain_list = {
            'property': {
                'last': ['2'],
                'total': ['2'],
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

    def set_up_patch(self, name, *args, **kwargs):
        patch = mock.patch(name, *args, **kwargs)
        self.addCleanup(patch.stop)
        return patch.start()
