from unittest import TestCase

from pycrunchbase import StockExchange


TEST_DATA = {
    "type": "StockExchange",
    "uuid": "f3931e1fe7720b6cf3124901723f4975",
    "properties": {
        "name": "National Association of Securities Dealers Automated Quotations",
        "short_name": "NASDAQ",
        "symbol": "NASDAQ",
        "created_at": 1437087616,
        "updated_at": 1437087616
    }
}


class StockExchangeTestCase(TestCase):
    def test_stockexchange_built(self):
        stockexchange = StockExchange(TEST_DATA)
        self.assertEqual(
            stockexchange.name,
            "National Association of Securities Dealers Automated Quotations")
        self.assertEqual(stockexchange.short_name, "NASDAQ")
        self.assertEqual(stockexchange.symbol, "NASDAQ")
        self.assertEqual(stockexchange.created_at, 1437087616)
        self.assertEqual(stockexchange.updated_at, 1437087616)

    def test_string(self):
        stockexchange = StockExchange(TEST_DATA)
        str(stockexchange)
