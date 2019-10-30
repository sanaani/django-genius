class PaymentData:
    def __init__(self, token=None):
        self.token = token

    @property
    def source(self):
        return "Vault"


class CardData(PaymentData):
    """Payment Data needed to Board a new Credit Card"""

    def __init__(self, card_number: int, expiration_date: int, card_holder: str, verification_number: int, **kwargs):
        super().__init__(token=kwargs.get("token"))
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.card_holder = card_holder
        self.card_verification_number = verification_number
        self.street = kwargs.get("street")
        self.zip_code = kwargs.get("zip_code")

    @property
    def source(self):
        return "Keyed"

    def __repr__(self):
        return str(self.__dict__)


class SaleData:
    def __init__(self, amount: float, invoice_number: str):
        self.amount = amount
        self.invoice_number = invoice_number

    @property
    def normalized_amount(self):
        return str(self.amount)
