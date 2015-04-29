from datetime import datetime
from unittest import TestCase

from pycrunchbase import IPO

TEST_DATA = {
    "uuid": "a3bc391490d52ba8529d1cfc20550a87",
    "type": "Ipo",
    "properties": {
        "went_public_on": "2012-05-18",
        "went_public_on_trust_code": 7,
        "stock_exchange_symbol": None,
        "stock_symbol": "FB",
        "shares_sold": 421000000,
        "opening_share_price": "38.0",
        "opening_share_price_currency_code": "USD",
        "opening_share_price_usd": "38.0",
        "opening_valuation": 104000000000,
        "opening_valuation_currency_code": "USD",
        "opening_valuation_usd": 104000000000,
        "money_raised": 16000000000,
        "money_raised_currency_code": "USD",
        "money_raised_usd": 16000000000,
        "created_at": 1407165772,
        "updated_at": 1427313923
        },
    "relationships": {
        "funded_company": {
            "cardinality": "OneToOne",
            "item": {
                "type": "Organization",
                "uuid": "uuidorg",
                "properties": {
                    "name": "Facebook",
                    "path": "organization/facebook",
                }
            }
        }
    }
}


class IPOTestCase(TestCase):
    def test_ipo_built(self):
        ipo = IPO(TEST_DATA)
        self.assertEqual(ipo.went_public_on, datetime(2012, 5, 18))
        self.assertEqual(ipo.went_public_on_trust_code, 7)
        self.assertEqual(ipo.stock_exchange_symbol, None)
        self.assertEqual(ipo.stock_symbol, "FB")
        self.assertEqual(ipo.shares_sold, 421000000)
        self.assertEqual(ipo.opening_share_price, 38.0)
        self.assertEqual(ipo.opening_share_price_currency_code, "USD")
        self.assertEqual(ipo.opening_share_price_usd, 38.0)
        self.assertEqual(ipo.opening_valuation, 104000000000)
        self.assertEqual(ipo.opening_valuation_currency_code, "USD")
        self.assertEqual(ipo.opening_valuation_usd, 104000000000)
        self.assertEqual(ipo.money_raised, 16000000000)
        self.assertEqual(ipo.money_raised_currency_code, "USD")
        self.assertEqual(ipo.money_raised_usd, 16000000000)

    def test_ipo_relationships_built(self):
        ipo = IPO(TEST_DATA)
        self.assertIsNotNone(ipo.funded_company)
        self.assertEqual('Facebook', ipo.funded_company.name)
