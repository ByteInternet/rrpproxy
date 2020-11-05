class RRPProxyInternalStatusException(Exception):
    def __init__(self, *args, **kwargs):
        self.response_dict = kwargs.pop('response_dict')
        super(RRPProxyInternalStatusException, self).__init__(args, kwargs)
