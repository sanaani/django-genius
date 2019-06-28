"""Helper classes to handle MerchantWare Authentication"""

from zeep import Client
from django.conf import settings

MERCHANT_WARE_SERVICE_ENDPOINT = 'https://ps1.merchantware.net/Merchantware/ws/RetailTransaction/v45/Credit.asmx'


class GeniusCredentials(object):
    def __init__(self):
        self.merchant_name = settings.GENIUS_MERCHANT_NAME
        self.merchant_site_id = settings.GENIUS_MERCHANT_SITE_ID
        self.merchant_key = settings.GENIUS_MERCHANT_KEY


class GeniusSOAPClient(object):
    def __init__(self):
        self.__transport = Client(MERCHANT_WARE_SERVICE_ENDPOINT)
        self.__transport_request = self.__transport.get_type("ns0:TransportRequest")
