import re
from urllib import parse
import requests


class RRPProxy:
    def __init__(self, username, password, use_test_environment=False):
        credential_parameters = 's_login={}&s_pw={}'.format(username, password)
        self.api_url = 'https://{}.rrpproxy.net/api/call.cgi?{}'.format('api-ote' if use_test_environment else 'api',
                                                                        credential_parameters)
        if use_test_environment:
            self.api_url += '&s_opmode=OTE'

    def call(self, command, **data):
        """This function will perform the API call"""
        scheme, netloc, path, params, query, fragment = parse.urlparse(self.api_url)

        query_dict = dict(parse.parse_qsl(query))
        query_dict.update({**data, **{'command': command}})
        query = parse.urlencode(query_dict)

        url = parse.urlunparse((scheme, netloc, path, params, query, fragment))
        response = requests.get(url)

        return self.response_to_dict(response.text)

    def response_to_dict(self, response_text):
        """This function translates response text into a dict"""
        response_text = response_text.replace('[RESPONSE]\n', '').replace('EOF\n', '')
        response_dict = {}
        for response_line in response_text.splitlines():
            key = response_line.split('=')[0].strip()
            value = response_line.split('=')[1].strip()
            if 'property[' in key:
                property_key = re.search(r"property\[([A-Za-z0-9_]+)\]", key).group(1)
                if 'property' not in response_dict: response_dict['property'] = {}
                if property_key not in response_dict['property']: response_dict['property'][property_key] = []
                response_dict['property'][property_key].append(value)
            else:
                response_dict[key] = value
        return response_dict

    def add_domain(self, domain, period, **domain_data):
        """
        Checks if domainname is available at the registry, creates the contacthandles in the registry
        and starts the registration at the registry
        """
        return self.call('AddDomain', domain=domain, period=period, **domain_data)

    def add_contact(self, **contact_data):
        """Allows you to add a new contact. System automatically substitutes existing handles."""
        return self.call('AddContact', **contact_data)

    def check_domain(self, domain):
        """Checks if the desired domain name is available and may be registered at the registry"""
        return self.call('CheckDomain', domain=domain)

    def delete_domain(self, domain):
        return self.call('DeleteDomain', domain=domain)

    def modify_domain(self, domain, **domain_data):
        return self.call('ModifyDomain', domain=domain, **domain_data)

    def renew_domain(self, domain, **domain_data):
        return self.call('RenewDomain', domain=domain, **domain_data)

    def status_domain(self, domain):
        """Enables you to check the actual status of a Domain in your portfolio"""
        return self.call('StatusDomain', domain=domain)
