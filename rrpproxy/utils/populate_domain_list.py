
RRPPROXY_DOMAIN_FIELDS = ('domain', 'domain status', 'domain updated date', 'nameserver', 'admincontact',
                          'techcontact', 'billingcontact', 'ownercontact')


def populate_domain_list(domains_in_rrpproxy_format):
    """
    This method takes the default format of RRP domains
    (a dictionary of lists for each property) and converts it
    to a list of dictionaries. Each dict in the list represents
    a domain and has the various properties as keys.
    A property will be absent in the dict if it has it had no value.
    :param dict domains_in_rrpproxy_format: Dict of lists with domain properties
    :return: List of domain dictionaries
    :rtype: list
    """
    domain_list = []
    properties = domains_in_rrpproxy_format['property']
    for index in range(len(properties['domain'])):
        domain_with_details = {}
        for domain_field in RRPPROXY_DOMAIN_FIELDS:
            if properties[domain_field][index]:
                domain_with_details[domain_field] = properties[domain_field][index]

        domain_list.append(domain_with_details)

    return domain_list
