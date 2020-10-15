import requests
from requests import Session

from rrpproxy import RRPProxy
from tests.test_rrpproxy_base import TestRRPProxyBase


class TestRRPProxyInit(TestRRPProxyBase):
    def test_init_sets_correct_api_url_and_query_params_when_using_sandbox_environment(self):
        self.assertEqual(self.proxy.api_url, 'https://api-ote.rrpproxy.net/api/call.cgi')
        self.assertEqual(self.proxy.query_params, {'s_login': self.username, 's_pw': self.password, 's_opmode': 'OTE'})

    def test_init_sets_correct_api_url_and_query_params_when_using_live_environment(self):
        self.proxy = RRPProxy(self.username, self.password)

        self.assertEqual(self.proxy.api_url, 'https://api.rrpproxy.net/api/call.cgi')
        self.assertEqual(self.proxy.query_params, {'s_login': self.username, 's_pw': self.password})

    def test_init_sets_requests_as_session_if_no_session_is_given(self):
        self.proxy = RRPProxy(self.username, self.password)

        self.assertEqual(self.proxy.session, requests)

    def test_init_sets_session_if_given(self):
        session = Session()
        self.proxy = RRPProxy(self.username, self.password, session=session)

        self.assertEqual(self.proxy.session, session)
