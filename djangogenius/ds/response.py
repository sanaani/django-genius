from zeep.proxy import ServiceProxy


class TransactionResponse:
    def __init__(self, response: ServiceProxy):
        self.approval_status = response.ApprovalStatus
        self.token = response.Token
        self.authorization_code = response.AuthorizationCode
        self.transaction_date = response.TransactionDate
        self.amount = response.Amount
        self.remaining_card_balance = response.RemainingCardBalance
        self.card_number = response.CardNumber
        self.card_holder = response.Cardholder
        self.card_type = response.CardType
        self.fsa_card = response.FsaCard
        self.reader_entry_mode = response.ReaderEntryMode
        self.avs_response = response.AvsResponse
        self.cv_response = response.CvResponse
        self.error_message = response.ErrorMessage
        self.extra_data = response.ExtraData
        self._fraud_scoring = response.FraudScoring
        self.rfmiq = response.Rfmiq
        self.debit_trance_number = response.DebitTraceNumber
        self._invoice = response.Invoice
        self.customer_email_address = response.CustomerEmailAddress

    @property
    def fraud_scoring(self):
        # TODO: parse data structure
        return self._fraud_scoring

    @property
    def invoice(self):
        # TODO: parse data structure
        return self._invoice


class VaultTokenResponse45:
    def __init__(self, response: ServiceProxy):
        self.card_number = response.CardNumber
        self.expiration_date = response.ExpirationDate
        self.card_holder = response.Cardholder
        self.card_type = response.CardType
        self.avs_street_address = response.AvsStreetAddress
        self.avs_zip_code = response.AvsZipCode
        self.error_code = response.ErrorCode
        self.error_message = response.ErrorMessage
        self.rfmiq = response.Rfmiq


class VaultBoardingResponse:
    def __init__(self, response: ServiceProxy):
        self.vault_token = response.VaultToken
        self.error_code = response.ErrorCode
        self.error_message = response.ErrorMessage
        self.rfmiq = response.Rfmiq
