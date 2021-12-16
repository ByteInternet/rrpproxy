
def populate_domain_list(domains_in_rrpproxy_format):
    domain_list = []
    for key, domain in enumerate(domains_in_rrpproxy_format['property']['domain']):
        domain_with_details = {
            'name': domains_in_rrpproxy_format['property']['domain'][key],
            'status': domains_in_rrpproxy_format['property']['domain status'][key],
            'updated_date': domains_in_rrpproxy_format['property']['domain updated date'][key],
        }

        if domains_in_rrpproxy_format['property']['nameserver'][key]:
            domain_with_details['nameserver'] = domains_in_rrpproxy_format['property']['nameserver'][key]
        if domains_in_rrpproxy_format['property']['admincontact'][key]:
            domain_with_details['admin_contact'] = domains_in_rrpproxy_format['property']['admincontact'][key]
        if domains_in_rrpproxy_format['property']['techcontact'][key]:
            domain_with_details['tech_contact'] = domains_in_rrpproxy_format['property']['techcontact'][key]
        if domains_in_rrpproxy_format['property']['billingcontact'][key]:
            domain_with_details['billing_contact'] = domains_in_rrpproxy_format['property']['billingcontact'][key]
        if domains_in_rrpproxy_format['property']['ownercontact'][key]:
            domain_with_details['owner_contact'] = domains_in_rrpproxy_format['property']['ownercontact'][key]

        domain_list.append(domain_with_details)

    return domain_list
