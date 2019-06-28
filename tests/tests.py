from django.test import TestCase, override_settings

from djangogenius.client import GeniusCredentials
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
