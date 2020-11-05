class RRPProxyInternalStatusException(Exception):
    def __init__(self, *args, **kwargs):
        self.code = kwargs.pop('code')
        super(RRPProxyInternalStatusException, self).__init__(args, kwargs)
