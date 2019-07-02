from zeep.proxy import ServiceProxy


class TransactionResponse:
    def __init__(self, mercharware_response45: ServiceProxy):
        self.approval_status = mercharware_response45.ApprovalStatus
        self.token = mercharware_response45.Token
        self.authorization_code = mercharware_response45.AuthorizationCode
        self.transaction_date = mercharware_response45.TransactionDate
        self.amount = mercharware_response45.Amount
        self.remaining_card_balance = mercharware_response45.RemainingCardBalance
        self.card_number = mercharware_response45.CardNumber
        self.card_holder = mercharware_response45.Cardholder
        self.card_type = mercharware_response45.CardType
        self.fsa_card = mercharware_response45.FsaCard
        self.reader_entry_mode = mercharware_response45.ReaderEntryMode
        self.avs_response = mercharware_response45.AvsResponse
        self.cv_response = mercharware_response45.CvResponse
        self.error_message = mercharware_response45.ErrorMessage
        self.extra_data = mercharware_response45.ExtraData
        self._fraud_scoring = mercharware_response45.FraudScoring
        self.rfmiq = mercharware_response45.Rfmiq
        self.debit_trance_number = mercharware_response45.DebitTraceNumber
        self._invoice = mercharware_response45.Invoice
        self.customer_email_address = mercharware_response45.CustomerEmailAddress

    @property
    def fraud_scoring(self):
        # TODO: parse data structure
        return self._fraud_scoring

    @property
    def invoice(self):
        # TODO: parse data structure
        return self._invoice
