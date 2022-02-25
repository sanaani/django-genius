"""Helper classes to handle MerchantWare Authentication"""

from zeep import Client
from django.conf import settings

from .ds import MerchantCredentials


class GeniusCredentials:
    def __init__(self):
        assert 1 <= len(settings.GENIUS_MERCHANT_NAME) <= 160
        assert 8 <= len(settings.GENIUS_MERCHANT_SITE_ID) <= 160
        assert 1 <= len(settings.GENIUS_MERCHANT_KEY) <= 160

        self.merchant_name = settings.GENIUS_MERCHANT_NAME
        self.merchant_site_id = settings.GENIUS_MERCHANT_SITE_ID
        self.merchant_key = settings.GENIUS_MERCHANT_KEY

    def get_merchant_credentials_ds(self):
        return MerchantCredentials(
            merchant_name=self.merchant_name, merchant_site_id=self.merchant_site_id, merchant_key=self.merchant_key
        )


class GeniusSOAPClient:
    def __init__(self, credentials: GeniusCredentials):
        self.client = Client(settings.GENIUS_MERCHANT_TRANSPORT_SERVICE_WSDL)
        self.creds = credentials

    def get_data_type(self, type: str, data: object):
        """Get construct object from data structure defined in the WSDL document"""
        return self.client.get_type(type)(**data.__dict__)

    @property
    def merchant_credentials(self):
        ds = self.creds.get_merchant_credentials_ds()
        return self.get_data_type("ns0:MerchantCredentials", ds)
