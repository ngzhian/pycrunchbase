from datetime import datetime
from unittest import TestCase

from pycrunchbase import IPO

TEST_DATA = {
    "uuid": "a3bc391490d52ba8529d1cfc20550a87",
    "type": "Ipo",
    "properties": {
        "opening_share_price_currency_code": "USD",
        "went_public_on_month": 5,
        "went_public_on_day": 18,
        "went_public_on_year": 2012,
        "went_public_on": "2012-05-18",
        "went_public_on_trust_code": 7,
        "canonical_currency_code": "USD",
        "money_raised_currency_code": "USD",
        "opening_valuation_currency_code": "USD",
        "stock_symbol": "FB",
        "permalink": "a3bc391490d52ba8529d1cfc20550a87",
        "name": "Went public on May 18, 2012",
        "stock_exchange_symbol": None,
        "shares_outstanding": None,
        "money_raised_usd": 16000000000,
        "money_raised": 16000000000,
        "opening_share_price_usd": "38.0",
        "shares_sold": 421000000,
        "opening_share_price": "38.0",
        "opening_valuation_usd": 104000000000,
        "opening_valuation": 104000000000,
        "created_at": 1407165772,
        "updated_at": 1427313923
        },
    "relationships": {
        "funded_company": {
            "paging": {
                "total_items": 1,
                "first_page_url": "https://api.crunchbase.com/v/2/ipo/a3bc391490d52ba8529d1cfc20550a87/funded_company",
                "sort_order": "created_at DESC"
                },
            "items": [
                {
                    "type": "Organization",
                    "name": "Facebook",
                    "path": "organization/facebook",
                    "created_at": 1180153335,
                    "updated_at": 1428028619
                }
            ]
        }
    }
}


class IPOTestCase(TestCase):
    def test_ipo_built(self):
        ipo = IPO(TEST_DATA)
        self.assertEqual(ipo.opening_share_price_currency_code, "USD")
        self.assertEqual(ipo.went_public_on_month, 5)
        self.assertEqual(ipo.went_public_on_day, 18)
        self.assertEqual(ipo.went_public_on_year, 2012)
        self.assertEqual(ipo.went_public_on, datetime(2012, 5, 18))
        self.assertEqual(ipo.went_public_on_trust_code, 7)
        self.assertEqual(ipo.canonical_currency_code, "USD")
        self.assertEqual(ipo.money_raised_currency_code, "USD")
        self.assertEqual(ipo.opening_valuation_currency_code, "USD")
        self.assertEqual(ipo.stock_symbol, "FB")
        self.assertEqual(ipo.permalink, "a3bc391490d52ba8529d1cfc20550a87")
        self.assertEqual(ipo.name, "Went public on May 18, 2012")
        self.assertEqual(ipo.stock_exchange_symbol, None)
        self.assertEqual(ipo.shares_outstanding, None)
        self.assertEqual(ipo.money_raised_usd, 16000000000)
        self.assertEqual(ipo.money_raised, 16000000000)
        self.assertEqual(ipo.opening_share_price_usd, 38.0)
        self.assertEqual(ipo.shares_sold, 421000000)
        self.assertEqual(ipo.opening_share_price, 38.0)
        self.assertEqual(ipo.opening_valuation_usd, 104000000000)
        self.assertEqual(ipo.opening_valuation, 104000000000)

    def test_ipo_relationships_built(self):
        ipo = IPO(TEST_DATA)
        self.assertIsNotNone(ipo.funded_company)
        self.assertEqual('Facebook', ipo.funded_company.get(0).name)
