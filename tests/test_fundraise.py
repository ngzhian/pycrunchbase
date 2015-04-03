from datetime import datetime
from unittest import TestCase

from pycrunchbase import FundRaise

TEST_DATA = {
    "uuid": "5807c4efa810655939cfda6f6d48f5a6",
    "type": "FundRaise",
    "properties": {
        "money_raised_usd": 550000000,
        "money_raised": 550000000,
        "money_raised_currency_code": "USD",
        "permalink": "5807c4efa810655939cfda6f6d48f5a6",
        "name": "Early-stage Fund VII",
        "announced_on_year": 2014,
        "announced_on_day": 10,
        "announced_on_month": 6,
        "announced_on": "2014-06-10",
        "announced_on_trust_code": 7,
        },
    "relationships": {
        "venture_firm": {
            "paging": {
                "total_items": 1,
                "first_page_url": "https://api.crunchbase.com/v/2/fund-raise/5807c4efa810655939cfda6f6d48f5a6/venture_firm",
                "sort_order": "created_at DESC"
                },
            "items": [
                {
                    "type": "Organization",
                    "name": "Index Ventures",
                    "path": "organization/index-ventures",
                    "created_at": 1201114688,
                    "updated_at": 1428059455
                    }
                ]
            },
        "news": {
            "paging": {
                "total_items": 1,
                "first_page_url": "https://api.crunchbase.com/v/2/fund-raise/5807c4efa810655939cfda6f6d48f5a6/news",
                "sort_order": "created_at DESC"
                },
            "items": [
                {
                    "url": "http://techcrunch.com/2014/06/10/index-ventures-raises-new-550m-early-stage-fund-for-europe-us-israel-aims-for-the-big-league/",
                    "author": None,
                    "posted_on": None,
                    "type": "PressReference",
                    "title": "Index Ventures Raises New $550M Early-Stage Fund For Europe, The US And Israel | TechCrunch",
                    "created_at": 1402455813,
                    "updated_at": 1402455813
                    }
                ]
            }
        }
}


class FundRaiseTestCase(TestCase):
    def test_fundraise_built(self):
        fundraise = FundRaise(TEST_DATA)
        self.assertEqual(fundraise.money_raised_usd, 550000000)
        self.assertEqual(fundraise.money_raised, 550000000)
        self.assertEqual(fundraise.money_raised_currency_code, "USD")
        self.assertEqual(fundraise.permalink, "5807c4efa810655939cfda6f6d48f5a6")
        self.assertEqual(fundraise.name, "Early-stage Fund VII")
        self.assertEqual(fundraise.announced_on_year, 2014)
        self.assertEqual(fundraise.announced_on_day, 10)
        self.assertEqual(fundraise.announced_on_month, 6)
        self.assertEqual(fundraise.announced_on, datetime(2014, 6, 10))
        self.assertEqual(fundraise.announced_on_trust_code, 7)

    def test_fundraise_relationships_built(self):
        fundraise = FundRaise(TEST_DATA)
        self.assertIsNotNone(fundraise.venture_firm)
        self.assertEqual('Index Ventures', fundraise.venture_firm.get(0).name)
        self.assertIsNotNone(fundraise.news)
        self.assertIn('Index Ventures Raise', fundraise.news.get(0).title)
