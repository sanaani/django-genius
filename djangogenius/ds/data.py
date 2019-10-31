class PaymentData:
    Source: str = "Vault"

    def __repr__(self):
        return f"{self.__class__.__name__}: {str(self.__dict__)}"


class VaultPaymentData(PaymentData):
    def __init__(self, token: str = ""):
        self.VaultToken = token


class KeyedPaymentData(PaymentData):
    Source = "Keyed"

    def __init__(
        self,
        *,
        card_number: str,
        expiration_date: str,
        card_holder: str,
        verification_number: str,
        street: str,
        zip_code: str,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.CardNumber = card_number
        self.ExpirationDate = expiration_date
        self.CardHolder = card_holder
        self.CardVerificationValue = verification_number
        self.AvsStreetAddress = street
        self.AvsZipCode = zip_code
