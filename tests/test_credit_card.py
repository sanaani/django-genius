from unittest.mock import MagicMock

from django.test import TestCase

from djangogenius.transaction import Sale, BoardCard, FindBoardedCard
from djangogenius.ds import VaultPaymentData, KeyedPaymentData, SaleRequest
from tests.utils import build_client


class CreditCardTestCase(TestCase):
    VALID_CARD_NUMBER = "4012000033330026"

    def setUp(self):
        self.client = build_client()

    def test_board_card(self):
        service = self.client.client.service
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

        service.BoardCard = MagicMock(name="MockedBoardCard")
        board_card.process(card_data)
        service.BoardCard.assert_called()

    def test_find_boarded_card(self):
        service = self.client.client.service
        service.FindBoardedCard = MagicMock(name="MockedBoardCard")

        board_card = FindBoardedCard(self.client)
        board_card.process("TEST-TOKEN")
        service.FindBoardedCard.assert_called()

    def test_sale(self):
        """Test Sale method of MerchantWare API"""

        client = build_client()
        sale = Sale(client)

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

        client.client.service.Sale = MagicMock(name="MockedSale")
        sale.process(payment_data, sale_data)
        client.client.service.Sale.assert_called()
