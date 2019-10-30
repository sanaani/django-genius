class BaseRequest:
    RegisterNumber: str = ""
    MerchantTransactionId: str = ""
    CardAcceptorTerminalId: str = ""


class CaptureRequest(BaseRequest):
    Amount: str = ""
    InvoiceNumber: str = ""


class AuthorizationRequest(CaptureRequest):
    pass


class SaleRequest(CaptureRequest):
    CashbackAmount: str = ""
    SurchargeAmount: str = ""
    TaxAmount: str = ""
    HealthCareAmountDetails: str = ""
    CardAcceptorTerminalId: str = ""
    PurchaseOrderNumber: str = ""
    CustomerCode: str = ""
    EnablePartialAuthorization: str = "false"
    ForceDuplicate: str = "false"


class VaultTokenRequest:
    VaultToken: str = ""


class UpdateBoardedCardRequest(VaultTokenRequest):
    ExpirationDate: str = ""


class VoidRequest(BaseRequest):
    Token: str = ""
