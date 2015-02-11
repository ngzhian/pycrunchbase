from datetime import datetime
from unittest import TestCase

from pycrunchbase import Organization

TEST_DATA = {
    "uuid": "df6628127f970b439d3e12f64f504fbb",
    "type": "Organization",
    "properties": {
        "description": "Description",
        "short_description": "short description",
        "founded_on_day": 2,
        "founded_on_month": 1,
        "founded_on_year": 2012,
        "founded_on": "2012-01-02",
        "permalink": "testpermalink",
        "homepage_url": "http://www.example.com",
        "name": "Organization",
        "closed_on_day": None,
        "closed_on_month": None,
        "closed_on_year": None,
        "closed_on": None,
        "total_funding_usd": 1234567,
        "number_of_investments": 1,
        "stock_symbol": "COY",
        "number_of_employees": 1234
    },
    "relationships": {
     "past_team": {
      "paging": {
       "total_items": 3,
       "first_page_url": "https://api.crunchbase.com/v/2/\
                          organization/example/past_team",
       "sort_order": "created_at DESC"
      },
      "items": [
       {
        "first_name": "First",
        "last_name": "Last",
        "title": "Director of Title",
        "started_on": None,
        "ended_on": None,
        "path": "person/first-last",
        "created_at": 1234567890,
        "updated_at": 1234567890
       }
      ]
     }
    }
}


class OrganizationTestCase(TestCase):
    def test_organization_built(self):
        org = Organization(TEST_DATA)
        self.assertEqual(org.description, 'Description')
        self.assertEqual(org.short_description, 'short description')
        self.assertEqual(org.founded_on, datetime(2012, 1, 2))
        self.assertEqual(org.permalink, "testpermalink")
        self.assertEqual(org.homepage_url, "http://www.example.com")
        self.assertEqual(org.name, "Organization")
        self.assertEqual(org.total_funding_usd, 1234567)
        self.assertEqual(org.number_of_investments, 1)
        self.assertEqual(org.stock_symbol, "COY")
        self.assertEqual(org.number_of_employees, 1234)

    def test_organization_relationships_built(self):
        org = Organization(TEST_DATA)
        self.assertIsNotNone(org.past_team)
        self.assertEqual('First', org.past_team.get(1).first_name)
        self.assertFalse(org.news)
        self.assertFalse(org.news.get(1))
        self.assertIsNone(org.news.get(1).first_name)
