
def populate_domain_list(domains_in_rrpproxy_format):
    domain_list = []
    for key, domain in enumerate(domains_in_rrpproxy_format['property']['domain']):
        domain_list.append({
            'name': domains_in_rrpproxy_format['property']['domain'][key],
            'status': domains_in_rrpproxy_format['property']['domain status'][key],
            'updated_date': domains_in_rrpproxy_format['property']['domain updated date'][key],
            'nameserver': domains_in_rrpproxy_format['property']['nameserver'][key],
            'admin_contact': domains_in_rrpproxy_format['property']['admincontact'][key],
            'tech_contact': domains_in_rrpproxy_format['property']['techcontact'][key],
            'billing_contact': domains_in_rrpproxy_format['property']['billingcontact'][key],
            'owner_contact': domains_in_rrpproxy_format['property']['ownercontact'][key],
        })
    return domain_list
