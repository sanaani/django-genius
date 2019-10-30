from unittest.mock import MagicMock

from django.test import TestCase

from djangogenius.transaction import Sale, PaymentData, SaleData, CardData, BoardCard, FindBoardedCard
from tests.utils import build_client


class CreditCardTestCase(TestCase):
    VALID_CARD_NUMBER = 4012000033330026

    def setUp(self):
        self.client = build_client()

    def test_board_card(self):
        service = self.client.client.service
        card_data = CardData(self.VALID_CARD_NUMBER, 1220, "John Doe", 123, street="5th ave", zip_code="10153")
        self.assertEqual("Keyed", card_data.source)

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

        payment_data = PaymentData(token="1")
        sale_data = SaleData(100, "1")

        client.client.service.Sale = MagicMock(name="MockedSale")
        sale.process(payment_data, sale_data)
        client.client.service.Sale.assert_called()
