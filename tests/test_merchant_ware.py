from unittest.mock import MagicMock

from django.test import TestCase

from djangogenius.transaction import Sale, PaymentData, SaleData
from tests.utils import build_client


class MerchantWareTransactionTestCase(TestCase):

    def test_sale(self):
        """Test Sale method of MerchatWare API"""

        client = build_client()
        sale = Sale(client)

        payment_data = PaymentData(token='test-token')
        sale_data = SaleData(100, '1')

        client.client.service.Sale = MagicMock(name='MockedSale')
        sale.process(payment_data, sale_data)
        client.client.service.Sale.assert_called()
