"""Helper classes to handle MerchantWare Authentication"""

from zeep import Client
from django.conf import settings


class GeniusCredentials:
    def __init__(self):
        assert 1 <= len(settings.GENIUS_MERCHANT_NAME) <= 160
        assert 8 <= len(settings.GENIUS_MERCHANT_SITE_ID) <= 160
        assert 1 <= len(settings.GENIUS_MERCHANT_KEY) <= 160

        self.merchant_name = settings.GENIUS_MERCHANT_NAME
        self.merchant_site_id = settings.GENIUS_MERCHANT_SITE_ID
        self.merchant_key = settings.GENIUS_MERCHANT_KEY


class GeniusSOAPClient:
    def __init__(self, credentials: GeniusCredentials):
        self.client = Client(settings.GENIUS_MERCHANT_TRANSPORT_SERVICE_WSDL)
        self.creds = credentials

    def get_data_type(self, type: str):
        """Get constructor for a data structured defined in the WSDL document"""
        return self.client.get_type(type)

    @property
    def merchant_credentials(self):
        return self.get_data_type("ns0:MerchantCredentials")(
            self.creds.merchant_name, self.creds.merchant_site_id, self.creds.merchant_key
        )
