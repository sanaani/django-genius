class BoardingRequest:
    pass


class BaseRequest:
    RegisterNumber: str = ""
    MerchantTransactionId: str = ""
    CardAcceptorTerminalId: str = ""

    def __init__(self, *, register_number: str, merchant_transaction_id: str, card_acceptor_terminal_id: str = ""):
        self.RegisterNumber = register_number
        self.MerchantTransactionId = merchant_transaction_id
        self.CardAcceptorTerminalId = card_acceptor_terminal_id


class CaptureRequest(BaseRequest):
    Amount: str = ""
    InvoiceNumber: str = ""

    def __init__(self, *, amount: str, invoice_number: str, **kwargs):
        self.Amount = amount
        self.InvoiceNumber = invoice_number
        super().__init__(**kwargs)


class AuthorizationRequest(CaptureRequest):
    pass


class SaleRequest(CaptureRequest):
    def __init__(
        self,
        *,
        tax_amount: str,
        purchase_order_number: str,
        customer_code: str,
        cashback_amount: str = "0",
        surcharge_amount: str = "0",
        health_care_amount_details: str = "",
        enable_partion_authorization: str = "false",
        force_duplicate: str = "false",
        **kwargs
    ):
        self.CashbackAmount = cashback_amount
        self.SurchargeAmount = surcharge_amount
        self.TaxAmount = tax_amount
        self.HealthCareAmountDetails = health_care_amount_details
        self.PurchaseOrderNumber = purchase_order_number
        self.CustomerCode = customer_code
        self.EnablePartialAuthorization = enable_partion_authorization
        self.ForceDuplicate = force_duplicate

        super().__init__(**kwargs)


class VoidRequest(BaseRequest):
    Token: str = ""

    def __init__(self, token: str, **kwargs):
        self.Token = token
        super().__init__(**kwargs)


class VaultTokenRequest:
    VaultToken: str = ""

    def __init__(self, token: str):
        self.VaultToken = token


class UpdateBoardedCardRequest(VaultTokenRequest):
    ExpirationDate: str = ""

    def __init__(self, token: str, expiration_date: str):
        super().__init__(token)
        self.ExpirationDate = expiration_date
