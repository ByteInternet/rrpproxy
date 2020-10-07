# rrpproxy

A python connector for RRP Proxy

## connect
```
from rrpproxy import RRPProxy
proxy = RRPProxy('username', 'password')
```

## connect to sandbox
```
from rrpproxy import RRPProxy
proxy = RRPProxy('username', 'password', True)
```
## usage
```
proxy.check_domain('hypernode.com')
```
## Running tests
The tests can be run by using `$ tox`
## More info
For more information related to the RRP Proxy API, visit: https://wiki.rrpproxy.net/api/api-commands/api-command-reference