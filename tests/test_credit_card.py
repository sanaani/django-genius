from unittest.mock import MagicMock

from django.test import TestCase

from djangogenius.transaction import Sale, BoardCard, FindBoardedCard, UpdateBoardedCard, Authorize, Capture
from djangogenius.ds import VaultPaymentData, KeyedPaymentData, SaleRequest, AuthorizationRequest, CaptureRequest
from tests.utils import build_client


class CreditCardTestCase(TestCase):
    VALID_CARD_NUMBER = "4012000033330026"

    def setUp(self):
        self.client = build_client()

    def test_board_card(self):
        service = self.client.client.service
        service.BoardCard = MagicMock(name="MockedBoardCard")

        card_data = KeyedPaymentData(
            card_number=self.VALID_CARD_NUMBER,
            expiration_date="1220",
            card_holder="John Doe",
            verification_number="123",
            street="5th ave",
            zip_code="10153",
        )
        self.assertEqual("Keyed", card_data.Source)

        board_card = BoardCard(self.client)

        board_card.process(card_data)
        service.BoardCard.assert_called()

    def test_find_boarded_card(self):
        service = self.client.client.service
        service.FindBoardedCard = MagicMock(name="MockedFindBoardedCard")

        board_card = FindBoardedCard(self.client)
        board_card.process("TEST-TOKEN")
        service.FindBoardedCard.assert_called()

    def test_update_boarded_card(self):
        service = self.client.client.service
        service.UpdateBoardedCard = MagicMock(name="MockedUpdateBoardedCard")

        board_card = UpdateBoardedCard(self.client)
        board_card.process("TEST-TOKEN")
        service.UpdateBoardedCard.assert_called()

    def test_sale(self):
        """Test Sale method of MerchantWare API"""

        sale = Sale(self.client)

        payment_data = VaultPaymentData()
        sale_data = SaleRequest(
            tax_amount="0.00",
            customer_code="1",
            purchase_order_number="1",
            amount=100,
            invoice_number=1,
            register_number=1,
            merchant_transaction_id=1,
            card_acceptor_terminal_id=1,
        )

        self.client.client.service.Sale = MagicMock(name="MockedSale")
        sale.process(payment_data, sale_data)
        self.client.client.service.Sale.assert_called()

    def test_authorize(self):
        """Test Authorize method of MerchantWare API"""

        authorize = Authorize(self.client)
        self.client.client.service.Authorize = MagicMock(name="MockedAuthorize")

        payment_data = VaultPaymentData("TEST-TOKEN")
        authorization_request = AuthorizationRequest(
            amount="100", invoice_number="1", register_number=1, merchant_transaction_id=1, card_acceptor_terminal_id=1
        )

        authorize.process(payment_data, authorization_request)
        self.client.client.service.Authorize.assert_called()

    def test_capture(self):
        """Test Capture method of MerchantWare API"""

        capture = Capture(self.client)
        self.client.client.service.Capture = MagicMock(name="MockedCapture")

        payment_data = VaultPaymentData("TEST-TOKEN")
        capture_request = CaptureRequest(
            amount="100", invoice_number="1", register_number=1, merchant_transaction_id=1, card_acceptor_terminal_id=1
        )

        capture.process(payment_data, capture_request)
        self.client.client.service.Capture.assert_called()
