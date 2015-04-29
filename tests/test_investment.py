from unittest import TestCase

from pycrunchbase import Investment

TEST_DATA = {
    "type": "InvestorInvestment",
    "uuid": "5807c4efa810655939cfda6f6d48f5a6",
    "properties": {
        "money_invested": 1000000,
        "money_invested_currency_code": "USD",
        "money_invested_usd": 1000000,
        "created_at": 1384319072,
        "updated_at": 1412126184
    },
    "relationships": {
        "funding_round": {
            "type": "FundingRound",
            "uuid": "8aeb5e3f786a23676ba62c8a00263ba6",
            "properties": {
                "api_path": "funding-rounds/8aeb5e3f786a23676ba62c8a00263ba6",
                "web_path": "funding-round/8aeb5e3f786a23676ba62c8a00263ba6",
                "funding_type": "seed",
                "series": None,
                "series_qualifier": None,
                "announced_on": "2015-01-05",
                "announced_on_trust_code": 7,
                "closed_on": None,
                "closed_on_trust_code": None,
                "money_raised": 50000,
                "money_raised_currency_code": "USD",
                "money_raised_usd": 50000,
                "target_money_raised": 50000,
                "target_money_raised_currency_code": "USD",
                "target_money_raised_usd": 50000,
                "created_at": 1424893720,
                "updated_at": 1424893982
            },
            "relationships": {
                "funded_organization": {
                    "type": "Organization",
                    "uuid": "5c8927ec6aa3c19796e51a8d34ef143e",
                    "properties": {
                        "permalink": "hyrecar",
                        "api_path": "organizations/hyrecar",
                        "web_path": "organization/hyrecar",
                        "name": "HyreCar",
                        "short_description": "short",
                        "primary_role": "company",
                        "role_company": True,
                        "role_investor": False,
                        "role_group": False,
                        "role_school": False,
                        "founded_on": "2014-12-01",
                        "founded_on_trust_code": 7,
                        "is_closed": False,
                        "closed_on": None,
                        "closed_on_trust_code": 0,
                        "num_employees_min": 11,
                        "num_employees_max": 50,
                        "total_funding_usd": 50000,
                        "number_of_investments": 0,
                        "homepage_url": "http://www.hyrecar.com",
                        "created_at": 1405764176,
                        "updated_at": 1429918751
                        }
                    }
                }
        }
    },
}


class InvestmentTestCase(TestCase):
    def test_investment_built(self):
        investment = Investment(TEST_DATA)
        self.assertEqual(investment.money_invested, 1000000)
        self.assertEqual(investment.money_invested_currency_code, "USD")
        self.assertEqual(investment.money_invested_usd, 1000000)

    def test_fundraise_relationships_built(self):
        investment = Investment(TEST_DATA)
        self.assertIsNotNone(investment.funding_round)
        self.assertEqual('seed', investment.funding_round.funding_type)
        self.assertEqual(
            'HyreCar',
            investment.funding_round.funded_organization.name)

    def test_string(self):
        investment = Investment(TEST_DATA)
        str(investment)
