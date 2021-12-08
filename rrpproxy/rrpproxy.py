import logging
import re
import requests
import time

from rrpproxy.utils.rrp_proxy_internal_status_exception import RRPProxyInternalStatusException
from rrpproxy.utils.rrpproxy_api_down_exception import RRPProxyAPIDownException

logger = logging.getLogger(__name__)


class RRPProxy:
    def __init__(self, username, password, session=None, use_test_environment=False):
        self.session = session
        if not session:
            self.session = requests

        self.query_params = {
            's_login': username,
            's_pw': password
        }
        environment = 'api'

        if use_test_environment:
            environment = 'api-ote'
            self.query_params['s_opmode'] = 'OTE'

        self.api_url = 'https://{}.rrpproxy.net/api/call.cgi'.format(environment)

    def call(self, command, **data):
        query_dict = self.query_params.copy()

        query_dict.update(data)
        query_dict['command'] = command

        try:
            response = self.session.get(self.api_url, params=query_dict)
            response.raise_for_status()
            response_dict = self.response_to_dict(response.text)
            if response_dict['code'] >= 400:
                exc_text = "Request was successfully handled, but RRP returned internal status code '{}'. Please " \
                           "investigate and handle accordingly.".format(response_dict['code'])
                if 'description' in response_dict:
                    exc_text += " Description: {}".format(response_dict['description'])
                raise RRPProxyInternalStatusException(exc_text, response_dict=response_dict)
            return response_dict
        except requests.ConnectionError:
            raise RRPProxyAPIDownException
        except requests.HTTPError:
            logger.error('Error returned from API Call', exc_info=True)
            raise

    def response_to_dict(self, response_text):
        response_text = response_text.replace('[RESPONSE]\n', '').replace('EOF\n', '')
        response_dict = {}
        for response_line in response_text.splitlines():
            key = response_line.split('=')[0].strip()
            value = response_line.split('=')[1].strip()
            if 'property[' in key:
                property_key = re.search(r"property\[([A-Za-z0-9_ -]+)\]", key).group(1)
                if 'property' not in response_dict:
                    response_dict['property'] = {}
                if property_key not in response_dict['property']:
                    response_dict['property'][property_key] = []
                response_dict['property'][property_key].append(value)
            elif 'code' == key:
                response_dict['code'] = int(value)
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

    def check_contact(self, contact):
        """Check availability of a contact"""
        return self.call('CheckContact', contact=contact)

    def check_domain(self, domain):
        """Checks if the desired domain name is available and may be registered at the registry"""
        return self.call('CheckDomain', domain=domain)

    def check_domain_transfer(self, domain, **transfer_data):
        """Check transfer requirements of particular gTLDs"""
        return self.call('CheckDomainTransfer', domain=domain, **transfer_data)

    def delete_domain(self, domain):
        """The command is used to request the deletion of the domain"""
        return self.call('DeleteDomain', domain=domain)

    def delete_contact(self, contact):
        """Delete a contact"""
        return self.call('DeleteContact', contact=contact)

    def get_zone_info(self, zone, domain):
        """Query information about a zone"""
        return self.call('GetZoneInfo', zone=zone, domain=domain)

    def modify_contact(self, contact, **contact_data):
        """Modify a contact handle"""
        return self.call('ModifyContact', contact=contact, **contact_data)

    def modify_domain(self, domain, **domain_data):
        """Modify domain data"""
        return self.call('ModifyDomain', domain=domain, **domain_data)

    def renew_domain(self, domain, **domain_data):
        """Command used to renew domains explicitly for a specified period of time"""
        return self.call('RenewDomain', domain=domain, **domain_data)

    def resend_notification(self, type, object, **extra_data):
        return self.call('ResendNotification', type=type, object=object, **extra_data)

    def set_auth_code(self, domain, **extra_data):
        return self.call('SetAuthCode', domain=domain, **extra_data)

    def set_domain_renewal_mode(self, domain, token, renewalmode):
        return self.call('SetDomainRenewalmode', domain=domain, token=token, renewalmode=renewalmode)

    def status_contact(self, contact, auth):
        return self.call('StatusContact', contact=contact, auth=auth)

    def status_domain(self, domain):
        """Enables you to check the actual status of a Domain in your portfolio"""
        return self.call('StatusDomain', domain=domain)

    def status_domain_transfer(self, domain):
        return self.call('StatusDomainTransfer', domain=domain)

    def trade_domain(self, domain, **trade_data):
        """Change registrant of a domain"""
        return self.call('TradeDomain', domain=domain, **trade_data)

    def transfer_domain(self, domain, action, **transfer_data):
        """This command allows you to request, approve, deny or cancel a domain transfer."""
        return self.call('TransferDomain', domain=domain, action=action, **transfer_data)

    def query_domain_list(self, **query_domain_data):
        """Query list of domains in account."""
        return self.call('QueryDomainList', **query_domain_data)

    def query_transfer_list(self, **query_transfer_data):
        """Query a list of incoming (running) domain transfers from an external registrar"""
        return self.call('QueryTransferList', **query_transfer_data)

    def query_foreign_transfer_list(self, **query_transfer_data):
        """Query a list of all domain which are currently in a transfer-out process"""
        return self.call('QueryForeignTransferList', **query_transfer_data)

    def query_zone_list(self):
        """Query list of activated zones in account"""
        return self.call('QueryZoneList')

    def get_domain_list_from_account(self, index=0, time_between_calls_in_seconds=1):
        """Returns list of domains registered in your account"""
        domain_list = self.query_domain_list(first=index)
        next_index = int(domain_list['property']['last'][0]) + 1
        total_domains = int(domain_list['property']['total'][0])
        if total_domains < next_index:
            return domain_list['property']['domain'] if 'domain' in domain_list['property'] else []
        else:
            # According to RRPProxy (https://wiki.rrpproxy.net/api/epp-server/frequently-asked-questions )
            # there is a rate limit of 1 command per second, therefore I added time.sleep as a parameter so
            # we can add any custom delay between calls case we want to
            time.sleep(time_between_calls_in_seconds)
            return domain_list['property']['domain'] + self.get_domain_list_from_account(index=next_index)
