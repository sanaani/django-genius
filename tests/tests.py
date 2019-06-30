from unittest.mock import patch

from django.test import TestCase, override_settings

from djangogenius.client import GeniusCredentials, GeniusSOAPClient
from djangogenius.forms import GeniusPaymentForm


class FormsTestCase(TestCase):
    def test_form_validation(self):
        form = GeniusPaymentForm({'paymentToken': None})
        self.assertFalse(form.is_valid())

        form = GeniusPaymentForm({'paymentToken': 'fake-token'})
        self.assertTrue(form.is_valid())


class SOAPClientTestCase(TestCase):

    @override_settings(GENIUS_MERCHANT_NAME='TEST-MERCHANT')
    @override_settings(GENIUS_MERCHANT_SITE_ID='TEST-SITE')
    @override_settings(GENIUS_MERCHANT_KEY='TEST-KEY')
    def test_credentials(self):
        creds = GeniusCredentials()
        self.assertEqual('TEST-MERCHANT', creds.merchant_name)
        self.assertEqual('TEST-SITE', creds.merchant_site_id)
        self.assertEqual('TEST-KEY', creds.merchant_key)

    @override_settings(GENIUS_MERCHANT_NAME='TEST-MERCHANT')
    def test_client_setup(self):
        credit_client = GeniusSOAPClient(GeniusCredentials())
        merchant_data = credit_client.merchant_data
        self.assertEqual('TEST-MERCHANT', merchant_data.MerchantName)

        # data = dict(
        #     Amount=1.01,
        #     SoftwareName="Test Software",
        #     InvoiceNumber="10",
        #     Source='Vault',
        #     VaultToken='fake-token',
        #
        # )
        # transaction = credit_client.create_transaction(**data)
