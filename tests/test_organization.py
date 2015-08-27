from datetime import datetime
from unittest import TestCase

from pycrunchbase import Organization

TEST_DATA = {
    "uuid": "df6628127f970b439d3e12f64f504fbb",
    "type": "Organization",
    "properties": {
        "permalink": "testpermalink",
        "api_path": "organizations/testpermalink",
        "web_path": "organization/testpermalink",
        "name": "Organization",
        "short_description": "short description",
        "description": "Description",
        "primary_role": "company",
        "role_company": True,
        "role_investor": False,
        "role_group": False,
        "role_school": False,
        "founded_on": "2012-01-02",
        "founded_on_trust_code": "7",
        "is_closed": False,
        "closed_on": None,
        "closed_on_trust_code": 0,
        "num_employees_min": 1234,
        "num_employees_max": 2345,
        "total_funding_usd": 1234567,
        "number_of_investments": 1,
        "homepage_url": "http://www.example.com",
        "created_at": 1180153335,
        "updated_at": 1430157435,
        "stock_exchange": "NASDAQ",
        "stock_symbol": "COY"
    },
    "relationships": {
     "current_team": {
      "cardinality": "OneToMany",
      "paging": {
       "total_items": 3,
       "first_page_url": "https://api.crunchbase.com/v/3/\
                          organizations/example/current_team",
       "sort_order": "created_at DESC"
      },
      "items": [
          {
              "type": "Job",
              "uuid": "uuid123",
              "properties": {
                  "title": "Director of Title",
                  "started_on": "2010-01-02",
                  "started_on_trust_code": 0,
                  "ended_on": None,
                  "ended_on_trust_code": 0,
                  "created_at": 1234567890,
                  "updated_at": 1234567890
              },
              "relationships": {
                  "person": {
                      "type": "Person",
                      "uuid": "uuidperson",
                      "properties": {
                          "permalink": "person1",
                          "api_path": "people/person1",
                          "web_path": "person/person1",
                          "first_name": "Person",
                          "last_name": "1",
                          "role_investor": True,
                          "born_on": "1911-01-02",
                          "born_on_trust_code": 7,
                          "is_deceased": False,
                          "died_on": None,
                          "died_on_trust_code": 0,
                          "created_at": 1180155106,
                          "updated_at": 1430155880
                      }
                  }
              }
          }
      ]
     }
    }
}


class OrganizationTestCase(TestCase):
    def test_organization_built(self):
        org = Organization(TEST_DATA)
        self.assertEqual(org.permalink, "testpermalink")
        self.assertEqual(org.name, "Organization")
        self.assertEqual(org.short_description, 'short description')
        self.assertEqual(org.description, 'Description')
        self.assertEqual(org.primary_role, 'company')
        self.assertEqual(org.role_company, True)
        self.assertEqual(org.role_investor, False)
        self.assertEqual(org.role_group, False)
        self.assertEqual(org.role_school, False)
        self.assertEqual(org.founded_on, datetime(2012, 1, 2))
        self.assertEqual(org.is_closed, False)
        self.assertEqual(org.closed_on, None)
        self.assertEqual(org.num_employees_min, 1234)
        self.assertEqual(org.num_employees_max, 2345)
        self.assertEqual(org.total_funding_usd, 1234567)
        self.assertEqual(org.number_of_investments, 1)
        self.assertEqual(org.homepage_url, "http://www.example.com")
        self.assertEqual(org.stock_exchange, "NASDAQ")
        self.assertEqual(org.stock_symbol, "COY")

    def test_organization_relationships_built(self):
        org = Organization(TEST_DATA)
        self.assertIsNotNone(org.current_team)
        self.assertEqual('Director of Title', org.current_team.get(0).title)
        # todo, relationship of a resource as a PageItem doesnt not work
        # self.assertEqual('Person', org.current_team.get(0).person.first_name)
