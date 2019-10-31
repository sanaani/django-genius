"""
Helper classes and methods to handle the transactions available in
MerchantWare SOAP API
"""
from djangogenius.client import GeniusSOAPClient
from djangogenius.ds import (
    AuthorizationRequest,
    CaptureRequest,
    PaymentData,
    TransactionResponse,
    VaultBoardingResponse,
    VaultTokenResponse45,
    VaultPaymentData,
    SaleRequest,
    KeyedPaymentData)


class MerchantWareTransaction:
    def __init__(self, genius_client: GeniusSOAPClient):
        self.client = genius_client
        self.service = genius_client.client.service

    def process(self, **data: dict):
        """Process transaction through MerchantWare API"""
        raise NotImplementedError("MerchantWareTransaction must be subclassed")


class Authorize(MerchantWareTransaction):
    def process(self, payment_data: VaultPaymentData, request_data: AuthorizationRequest):
        payment_data = self.client.get_data_type("ns0:PaymentData")(**payment_data.__dict__)
        request_data = self.client.get_data_type("ns0:AuthorizationRequest")(**request_data.__dict__)

        authorization = self.service.Authorize(self.client.merchant_credentials, payment_data, request_data)
        return TransactionResponse(authorization)


class Capture(MerchantWareTransaction):
    def process(self, payment_data: VaultPaymentData, request_data: CaptureRequest):
        payment_data = self.client.get_data_type("ns0:PaymentData")(**payment_data.__dict__)
        request_data = self.client.get_data_type("ns0:CaptureRequest")(**request_data.__dict__)

        response = self.service.Capture(self.client.merchant_credentials, payment_data, request_data)
        return TransactionResponse(response)


class Sale(MerchantWareTransaction):
    def process(self, payment_data: PaymentData, sale_data: SaleRequest):
        payment_data = self.client.get_data_type("ns0:PaymentData")(**payment_data.__dict__)
        sale_data = self.client.get_data_type("ns0:SaleRequest")(**sale_data.__dict__)

        sale = self.service.Sale(self.client.merchant_credentials, payment_data, sale_data)
        return TransactionResponse(sale)


class BoardCard(MerchantWareTransaction):
    def process(self, card_data: KeyedPaymentData):
        payment = self.client.get_data_type("ns0:PaymentData")(card_data)
        boarding_request = self.client.get_data_type("ns0:BoardingRequest")({})
        response = self.service.BoardCard(self.client.merchant_credentials, payment, boarding_request)

        return VaultBoardingResponse(response)


class FindBoardedCard(MerchantWareTransaction):
    def process(self, token: str):
        vault_token_request = self.client.get_data_type("ns0:VaultTokenRequest")
        token_request = vault_token_request(VaultToken=token)

        result = self.service.FindBoardedCard(self.client.merchant_credentials, token_request)
        return VaultTokenResponse45(result)


class UpdateBoardedCard(MerchantWareTransaction):
    def process(self, token: str):
        vault_token_request = self.client.get_data_type("ns0:VaultTokenRequest")
        token_request = vault_token_request(VaultToken=token)

        result = self.service.UpdateBoardedCard(self.client.merchant_credentials, token_request)
        return VaultTokenResponse45(result)
