"""
Helper classes and methods to handle the transactions available in
MerchantWare SOAP API
"""
from djangogenius.client import GeniusSOAPClient
from djangogenius.response import TransactionResponse


class PaymentData:
    def __init__(self, token: str):
        self.token = token

    @property
    def source(self):
        return 'Vault'


class SaleData:
    def __init__(self, amount: float, invoice_number: str):
        self.amount = amount
        self.invoice_number = invoice_number

    @property
    def normalized_amount(self):
        return str(self.amount)


class MerchantWareTransaction:
    def __init__(self, client: GeniusSOAPClient):
        self.client = client

    def process(self, **data: dict):
        """Process transaction through MerchantWare API"""
        raise NotImplementedError("MerchantWareTransaction must be subclassed")


class Sale(MerchantWareTransaction):
    def process(self, payment_data: PaymentData, sale_data: SaleData):
        payment_data = self.client.get_data_type('ns0:PaymentData')(**{
            'Source': payment_data.source,
            'VaultToken': payment_data.token
        })

        sale_data = self.client.get_data_type('ns0:SaleRequest')(**{
            'Amount': sale_data.normalized_amount,
            'InvoiceNumber': sale_data.invoice_number
        })

        zeep_client = self.client.client
        with zeep_client.settings(strict=False):
            sale = zeep_client.service.Sale(self.client.merchant_data, payment_data, sale_data)

        return TransactionResponse(sale)
