# rrpproxy

A python connector for RRP Proxy

## connect
```
from rrpproxy import RRPProxy
proxy = RRPProxy('username', 'password')
```
 
RRPProxy advises to use long standing connections. If you want to re-use the same Session:

```
import requests
from rrpproxy import RRPProxy

session = requests.Session()
proxy = RRPProxy('username', 'password', session=session)
```

## connect to sandbox
```
from rrpproxy import RRPProxy
proxy = RRPProxy('username', 'password', use_test_environment=True)
```
## usage
```
proxy.check_domain('hypernode.com')
```
> ```lang-json
> {'code': '210',
>  'description': 'Domain name available',
>  'runtime': '0.267',
>  'queuetime': '0'
> } 

```
proxy.add_domain(domain='newdomain.tld', period=2, ownercontact0='Owner', techcontact0='Tech-user', billingcontact0='Billing-User', admincontact0='Admin', auth='2foo"BAR%', nameserver0='nameserver', nameserver1='nameserver1', x-fee-amount=2000)
```
> ```lang-json
> {'code': '200',
>  'description': 'Command completed succesfully',
>  'property': {
>       'x-fee-amount': ['2000'],
>       'x-fee-application': ['0'],
>       'x-fee-currency': ['EUR'],
>       'created date': ['2015-06-24 11:53:27'],
>       'registration expiration date': ['2017-06-24 11:53:27'],
>       'renewal date': ['2017-07-29 11:53:27'],
>       'roid': ['13530236711060_DOMAIN-KEYSYS'],
>       'status': ['ACTIVE'],
>  },
> 'runtime': '0.1',
> 'queuetime: '0',
> }
> ```
## Running tests
The tests can be run by using `$ tox`
## More info
For more information related to the RRP Proxy API, visit: https://wiki.rrpproxy.net/api/api-commands/api-command-reference