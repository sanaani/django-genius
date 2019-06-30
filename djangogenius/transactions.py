"""
Helper classes and methods to handle the transactions available in
MerchantWare SOAP API
"""


class Profile:
    def __init__(self):
        pass


class MerchantWareTransaction:
    def authorize(self, *args, **kwargs):
        raise NotImplementedError

    def sale(self, *args, **kwargs):
        raise NotImplementedError
