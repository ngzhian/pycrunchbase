from unittest import TestCase

from pycrunchbase import PageItem
from pycrunchbase.resource.pageitem import (
    AcquisitionPageItem,
    FundingRoundPageItem,
    IpoPageItem,
    OrganizationPageItem,
    PersonPageItem,
    ProductPageItem,
)


class PageItemTestCase(TestCase):
    def test_acquisition_page_item(self):
        data = {
            "announced_on": "2015-01-16",
            "type": "Acquisition",
            "name": "Acquisition",
            "path": "acquisition/4292239d4dbbc52eeee0856612ed9c47",
            "created_at": 1421443747,
            "updated_at": 1421689170
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, AcquisitionPageItem)
        self.assertEqual(page_item.announced_on, "2015-01-16")
        self.assertEqual(page_item.type, "Acquisition")
        self.assertEqual(page_item.name, "Acquisition")
        self.assertEqual(
            page_item.path, "acquisition/4292239d4dbbc52eeee0856612ed9c47")
        self.assertEqual(
            page_item.uuid, "4292239d4dbbc52eeee0856612ed9c47")

    def test_funding_round_page_item(self):
        data = {
            "type": "FundingRound",
            "name": "Funding Round Name",
            "path": "funding-round/37bd05f961af726ba3c1b279da842805",
            "created_at": 1295843747,
            "updated_at": 1419019444
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, FundingRoundPageItem)
        self.assertEqual(page_item.type, "FundingRound")
        self.assertEqual(page_item.name, "Funding Round Name")
        self.assertEqual(
            page_item.path, "funding-round/37bd05f961af726ba3c1b279da842805")
        self.assertEqual(
            page_item.uuid, "37bd05f961af726ba3c1b279da842805")

    def test_ipo_page_item(self):
        data = {
            "type": "Ipo",
            "name": "Ipo Name",
            "path": "ipo/a3bc391490d52ba8529d1cfc20550a87",
            "created_at": 1407165772,
            "updated_at": 1412285699
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, IpoPageItem)
        self.assertEqual(page_item.type, "Ipo")
        self.assertEqual(page_item.name, "Ipo Name")
        self.assertEqual(
            page_item.path, "ipo/a3bc391490d52ba8529d1cfc20550a87")
        self.assertEqual(
            page_item.uuid, "a3bc391490d52ba8529d1cfc20550a87")

    def test_organization_page_item(self):
        data = {
            "type": "Organization",
            "name": "Example",
            "path": "organization/example",
            "created_at": 1419162865,
            "updated_at": 1419596914
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, OrganizationPageItem)
        self.assertEqual(page_item.type, "Organization")
        self.assertEqual(page_item.name, "Example")
        self.assertEqual(page_item.path, "organization/example")
        self.assertEqual(page_item.permalink, "example")

    def test_person_page_item(self):
        data = {
            "first_name": "First",
            "last_name": "Last",
            "title": "Title",
            "started_on": None,
            "ended_on": None,
            "path": "person/first-last",
            "created_at": 1233300345,
            "updated_at": 1419596914
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, PersonPageItem)
        self.assertEqual(page_item.first_name, "First")
        self.assertEqual(page_item.last_name, "Last")
        self.assertEqual(page_item.title, "Title")
        self.assertEqual(page_item.started_on, None)
        self.assertEqual(page_item.ended_on, None)
        self.assertEqual(page_item.path, "person/first-last")
        self.assertEqual(page_item.permalink, "first-last")

    def test_product_page_item(self):
        data = {
            "type": "Product",
            "name": "Product Name",
            "path": "product/product-permalink",
            "created_at": 1422955389,
            "updated_at": 1422955417
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, ProductPageItem)
        self.assertEqual(page_item.type, "Product")
        self.assertEqual(page_item.name, "Product Name")
        self.assertEqual(page_item.path, "product/product-permalink")
        self.assertEqual(page_item.permalink, "product-permalink")

    def test_news_page_item(self):
        data = {
            "url": "http://example.com/1/",
            "author": "Author 1",
            "posted_on": "2015-02-05",
            "type": "PressReference",
            "title": "Title 1",
            "created_at": 1423206060,
            "updated_at": 1423207820
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, PageItem)
        self.assertEqual(page_item.url, "http://example.com/1/")
        self.assertEqual(page_item.author, "Author 1")
        self.assertEqual(page_item.title, "Title 1")

    def test_unknown_node_item(self):
        data = {
            "type": "Unknown",
            "name": "Unknown Name",
            "path": "unknown/unknown-permalink",
        }
        page_item = PageItem.build(data)
        self.assertIsInstance(page_item, PageItem)
        self.assertEqual(page_item.type, "Unknown")
        self.assertEqual(page_item.name, "Unknown Name")
        self.assertEqual(page_item.path, "unknown/unknown-permalink")
