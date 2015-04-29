# vim: set fileencoding=utf-8 :

from datetime import datetime
from unittest import TestCase

from pycrunchbase import PageItem

from pycrunchbase import (
    Acquisition,
    Category,
    FundingRound,
    IPO,
    Investment,
    Location,
    News,
    Organization,
    Person,
    Product,
)


class PageItemTestCase(TestCase):
    def test_acquisition_page_item(self):
        data = {
            "type": "Acquisition",
            "uuid": "4292239d4dbbc52eeee0856612ed9c47",
            "properties": {
                "announced_on": "2015-01-16",
                "api_path": "acquisition/4292239d4dbbc52eeee0856612ed9c47",
                "created_at": 1421443747,
                "updated_at": 1421689170,
            }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, Acquisition)
        self.assertEqual(page_item.announced_on, datetime(2015, 1, 16))
        self.assertEqual(
            page_item.api_path, "acquisition/4292239d4dbbc52eeee0856612ed9c47")
        self.assertEqual(
            page_item.uuid, "4292239d4dbbc52eeee0856612ed9c47")

    def test_funding_round_page_item(self):
        data = {
            "type": "FundingRound",
            "uuid": "37bd05f961af726ba3c1b279da842805",
            "properties": {
                "api_path": "funding-rounds/37bd05f961af726ba3c1b279da842805",
                "funding_type": "private_equity",
            }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, FundingRound)
        self.assertEqual(page_item.funding_type, "private_equity")
        self.assertEqual(
            page_item.api_path,
            "funding-rounds/37bd05f961af726ba3c1b279da842805")
        self.assertEqual(
            page_item.uuid, "37bd05f961af726ba3c1b279da842805")

    def test_ipo_page_item(self):
        data = {
            "type": "Ipo",
            "uuid": "a3bc391490d52ba8529d1cfc20550a87",
            "properties": {
                "stock_symbol": "FB",
                "api_path": "ipo/a3bc391490d52ba8529d1cfc20550a87",
            }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, IPO)
        self.assertEqual(page_item.stock_symbol, "FB")
        self.assertEqual(
            page_item.api_path, "ipo/a3bc391490d52ba8529d1cfc20550a87")

    def test_organization_page_item(self):
        data = {
            "type": "Organization",
            "uuid": "df6628127f970b439d3e12f64f504fbb",
            "properties": {
                "api_path": "organizations/example",
                "web_path": "organization/example",
                "name": "Facebook",
            },
            "relationships": {
                "investors": {
                    "cardinality": "OneToMany",
                    "paging": {
                        "total_items": 17,
                        "first_page_url": "https://api.crunchbase.com/v/3/organizations/facebook/investors",
                        "sort_order": "created_at DESC"
                    },
                    "items": [
                        {
                            "type": "Organization",
                            "uuid": "8ce2fd0305ddab1d19e1826840e305f1",
                            "properties": {
                                "permalink": "elevation-partners",
                            },
                        }
                    ]
                },
                "headquarters": {
                    "cardinality": "OneToOne",
                    "item": {
                        "type": "Address",
                        "uuid": "31adbab5e90fc45a47ae873e0656fadd",
                        "properties": {
                            "name": "Headquarters",
                            "street_1": "1601 Willow Road",
                        }
                    }
                }
            }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, Organization)
        self.assertEqual(page_item.name, "Facebook")
        self.assertEqual(page_item.api_path, "organizations/example")
        self.assertEqual(page_item.web_path, "organization/example")
        self.assertEqual(1, len(page_item.investors))
        self.assertEqual(
            page_item.investors[0].permalink, "elevation-partners")
        self.assertEqual(
            page_item.headquarters.name, "Headquarters")
        self.assertEqual(
            page_item.headquarters.street_1, "1601 Willow Road")

    def test_person_page_item(self):
        data = {
            "type": "Person",
            "uuid": "b189fb60acc9668402e4c2e83b0de3f4",
            "properties": {
                "permalink": "louis-botes",
                "api_path": "people/louis-botes",
                "web_path": "person/louis-botes",
                "first_name": "Louis",
                "last_name": "Botes",
            }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, Person)
        self.assertEqual(page_item.first_name, "Louis")
        self.assertEqual(page_item.last_name, "Botes")
        self.assertEqual(page_item.permalink, "louis-botes")
        self.assertEqual(page_item.api_path, "people/louis-botes")
        self.assertEqual(page_item.web_path, "person/louis-botes")

    def test_product_page_item(self):
        data = {
            "type": "Product",
            "uuid": "71d7b04af6944553e845101d720e87a1",
            "properties": {
                "permalink": "hello",
                "api_path": "products/hello",
                "web_path": "product/hello",
                "name": "Hello",
            }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, Product)
        self.assertEqual(page_item.uuid, "71d7b04af6944553e845101d720e87a1")
        self.assertEqual(page_item.name, "Hello")
        self.assertEqual(page_item.permalink, "hello")
        self.assertEqual(page_item.api_path, "products/hello")
        self.assertEqual(page_item.web_path, "product/hello")

    def test_news_page_item(self):
        data = {
            "type": "News",
            "uuid": "3610c416c22e446380b3a4ef4b3c5fc1",
            "properties": {
                "title": "Title",
                "author": "Author 1",
                "posted_on": "2015-04-27",
                }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, News)
        self.assertEqual(page_item.title, "Title")
        self.assertEqual(page_item.author, "Author 1")
        self.assertEqual(page_item.posted_on, datetime(2015, 4, 27))

    def test_location_page_item(self):
        data = {
            "type": "Location",
            "uuid": "uuid",
            "properties": {
                "name": "New York",
                "location_type": "city",
            }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, Location)
        self.assertEqual(page_item.name, "New York")
        self.assertEqual(page_item.location_type, "city")

    def test_category_page_item(self):
        data = {
            "type": "Category",
            "uuid": "uuid",
            "properties": {
                "name": "Social",
                "organizations_in_category": 10,
                "products_in_category": 9,
            }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, Category)
        self.assertEqual(page_item.name, "Social")
        self.assertEqual(page_item.organizations_in_category, 10)
        self.assertEqual(page_item.products_in_category, 9)

    def test_investor_investment_investor(self):
        data = {
            "type": "InvestorInvestment",
            "uuid": "5807c4efa810655939cfda6f6d48f5a6",
            "properties": {
                "money_invested": 1234567,
                "money_invested_currency_code": "USD",
                "money_invested_usd": 1234567,
            },
            "relationships": {
                "funding_round": {
                    "type": "FundingRound",
                    "uuid": "8aeb5e3f786a23676ba62c8a00263ba6",
                    "properties": {
                        "funding_type": "seed",
                    }
                }
            }
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, Investment)
        self.assertEqual(page_item.money_invested, 1234567)
        self.assertEqual(page_item.money_invested_currency_code, "USD")
        self.assertEqual(page_item.money_invested_usd, 1234567)
        self.assertEqual(page_item.funding_round.funding_type, "seed")

    def test_unicode(self):
        data = {
            "type": "Person",
            "uuid": "b189fb60acc9668402e4c2e83b0de3f4",
            "properties": {
                "first_name": u"å",
                "last_name": "Last",
                "permalink": "permalink",
            }
        }
        page_item = PageItem.build(data)
        try:
            _ = unicode('')  #py2
            import codecs
            self.assertEqual(codecs.encode(u'å Last (permalink)', 'utf8'), str(page_item))
        except:
            # py3
            self.assertEqual(u'å Last (permalink)', str(page_item))

    def test_repr(self):
        page_item = PageItem.build({'sample': 'data'})
        assert repr(page_item) == "PageItem: {'sample': 'data'}"

    def test_str(self):
        page_item = PageItem.build({'sample': 'data'})
        assert str(page_item) == "PageItem: {'sample': 'data'}"
