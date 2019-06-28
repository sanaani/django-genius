"""
Helper classes and methods to handle the transactions available in
MerchantWare SOAP API
"""


class MerchantWareTransaction(object):
    def authorize(self, *args, **kwargs):
        raise NotImplementedError

    def sale(self, *args, **kwargs):
        raise NotImplementedError
