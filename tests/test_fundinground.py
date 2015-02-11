from datetime import datetime
from unittest import TestCase

from pycrunchbase import FundingRound

FUNDING_ROUND_DATA = {
 "uuid": "uuid1",
 "type": "FundingRound",
 "properties": {
  "funding_type": "private_equity",
  "money_raised_usd": 1500000000,
  "announced_on_year": 2011,
  "announced_on_day": 21,
  "announced_on_month": 1,
  "announced_on": "2011-01-21",
  "announced_on_trust_code": 7,
  "canonical_currency_code": "USD",
  "money_raised": 1500000000,
  "money_raised_currency_code": "USD",
  "permalink": "uuid1",
  "name": "funding round name",
  "post_money_valuation_currency_code": "USD",
  "created_at": 1295843747,
  "updated_at": 1419019444
 },
 "relationships": {
  "investments": {
   "paging": {
    "total_items": 2,
    "first_page_url": "https://api.crunchbase.com/v/2/funding-round/uuid1/investments",
    "sort_order": "created_at DESC"
   },
   "items": [
    {
     "type": "InvestorInvestment",
     "money_invested": None,
     "money_invested_currency_code": "USD",
     "money_invested_usd": None,
     "investor": {
      "type": "Organization",
      "name": "Digital Sky Technologies",
      "path": "organization/digital-sky-technologies-fo"
     }
    },
    {
     "type": "InvestorInvestment",
     "money_invested": None,
     "money_invested_currency_code": "USD",
     "money_invested_usd": None,
     "investor": {
      "type": "Organization",
      "name": "Goldman Sachs",
      "path": "organization/goldman-sachs"
     }
    }
   ]
  },
  "funded_organization": {
   "paging": {
    "total_items": 1,
    "first_page_url": "https://api.crunchbase.com/v/2/funding-round/uuid1/funded_organization",
    "sort_order": "created_at DESC"
   },
   "items": [
    {
     "type": "Organization",
     "name": "Facebook",
     "path": "organization/facebook",
     "created_at": 1180153335,
     "updated_at": 1423385400
    }
   ]
  },
  "news": {
   "paging": {
    "total_items": 1,
    "first_page_url": "https://api.crunchbase.com/v/2/funding-round/uuid1/news",
    "sort_order": "created_at DESC"
   },
   "items": [
    {
     "url": "http://example.com/url_1",
     "author": None,
     "posted_on": None,
     "type": "PressReference",
     "title": "Title 1",
     "created_at": 1295843747,
     "updated_at": 1398009912
    }
   ]
  }
 }
}


class FundingRoundTestCase(TestCase):
    def test_properties(self):
        funding_round = FundingRound(FUNDING_ROUND_DATA)
        self.assertEqual(funding_round.funding_type, "private_equity")
        self.assertEqual(funding_round.money_raised_usd, 1500000000)
        self.assertEqual(funding_round.announced_on_year, 2011)
        self.assertEqual(funding_round.announced_on_day, 21)
        self.assertEqual(funding_round.announced_on_month, 1)
        self.assertEqual(funding_round.announced_on, datetime(2011, 1, 21))
        self.assertEqual(funding_round.announced_on_trust_code, 7)
        self.assertEqual(funding_round.canonical_currency_code, "USD")
        self.assertEqual(funding_round.money_raised, 1500000000)
        self.assertEqual(funding_round.money_raised_currency_code, "USD")
        self.assertEqual(funding_round.permalink, "uuid1")
        self.assertEqual(funding_round.name, "funding round name")
        self.assertEqual(
            funding_round.post_money_valuation_currency_code, "USD")
        self.assertEqual(funding_round.created_at, 1295843747)
        self.assertEqual(funding_round.updated_at, 1419019444)

    def test_relationships(self):
        pass
