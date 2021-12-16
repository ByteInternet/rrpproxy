
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
        domain_with_details = {
            'name': properties['domain'][index],
            'status': properties['domain status'][index],
            'updated_date': properties['domain updated date'][index],
        }

        if properties['nameserver'][index]:
            domain_with_details['nameserver'] = properties['nameserver'][index]
        if properties['admincontact'][index]:
            domain_with_details['admin_contact'] = properties['admincontact'][index]
        if properties['techcontact'][index]:
            domain_with_details['tech_contact'] = properties['techcontact'][index]
        if properties['billingcontact'][index]:
            domain_with_details['billing_contact'] = properties['billingcontact'][index]
        if properties['ownercontact'][index]:
            domain_with_details['owner_contact'] = properties['ownercontact'][index]

        domain_list.append(domain_with_details)

    return domain_list
