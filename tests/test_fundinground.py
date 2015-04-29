from datetime import datetime
from unittest import TestCase

from pycrunchbase import FundingRound

FUNDING_ROUND_DATA = {
 "uuid": "uuid1",
 "type": "FundingRound",
 "properties": {
  "permalink": "uuid1",
  "funding_type": "private_equity",
  "series": "c",
  "announced_on": "2011-01-21",
  "announced_on_trust_code": 7,
  "closed_on": None,
  "closed_on_trust_code": 7,
  "money_raised": 1500000000,
  "money_raised_currency_code": "USD",
  "money_raised_usd": 1500000000,
  "target_money_raised": 1500000000,
  "target_money_raised_currency_code": "USD",
  "target_money_raised_usd": 1500000000,
  "created_at": 1295843747,
  "updated_at": 1419019444,
 },
 "relationships": {
  "investments": {
   "cardinality": "OneToMany",
   "paging": {
    "total_items": 2,
    "first_page_url": "https://api.crunchbase.com/v/3/funding-round/uuid1/investments",
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
   "cardinality": "OneToOne",
   "item": {
       "type": "Organization",
       "uuid": "uuidorg",
       "properties": {
           "name": "Facebook",
           "path": "organization/facebook",
           "created_at": 1180153335,
           "updated_at": 1423385400,
       }
   }

  },
  "news": {
   "cardinality": "OneToMany",
   "paging": {
    "total_items": 1,
    "first_page_url": "https://api.crunchbase.com/v/3/funding-round/uuid1/news",
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
        self.assertEqual(funding_round.permalink, "uuid1")
        self.assertEqual(funding_round.funding_type, "private_equity")
        self.assertEqual(funding_round.series, "c")
        self.assertEqual(funding_round.announced_on, datetime(2011, 1, 21))
        self.assertEqual(funding_round.announced_on_trust_code, 7)
        self.assertEqual(funding_round.closed_on, None)
        self.assertEqual(funding_round.closed_on_trust_code, 7)
        self.assertEqual(funding_round.money_raised, 1500000000)
        self.assertEqual(funding_round.money_raised_currency_code, "USD")
        self.assertEqual(funding_round.money_raised_usd, 1500000000)
        self.assertEqual(funding_round.target_money_raised, 1500000000)
        self.assertEqual(funding_round.target_money_raised_currency_code, "USD")
        self.assertEqual(funding_round.target_money_raised_usd, 1500000000)
        self.assertEqual(funding_round.created_at, 1295843747)
        self.assertEqual(funding_round.updated_at, 1419019444)

    def test_relationships(self):
        funding_round = FundingRound(FUNDING_ROUND_DATA)
        self.assertEqual(len(funding_round.investments), 2)
        self.assertEqual(funding_round.funded_organization.name, "Facebook")
        self.assertEqual(len(funding_round.news), 1)
