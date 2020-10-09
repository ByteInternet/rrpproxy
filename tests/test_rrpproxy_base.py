from unittest import TestCase, mock

from rrpproxy import RRPProxy


class TestRRPProxyBase(TestCase):
    def setUp(self):
        self.get_mock = self.set_up_patch('requests.get')
        self.logger_mock = self.set_up_patch('rrpproxy.rrpproxy.logger')
        self.username = 'dummy_username'
        self.password = 'secret_password'
        self.proxy = RRPProxy(self.username, self.password, use_test_environment=True)

    def set_up_patch(self, name, *args, **kwargs):
        patch = mock.patch(name, *args, **kwargs)
        self.addCleanup(patch.stop)
        return patch.start()
