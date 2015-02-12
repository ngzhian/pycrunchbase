from datetime import datetime
from unittest import TestCase

from pycrunchbase import Product

PRODUCT_DATA = {
  "uuid": "d00804b457a0a9743671d596e8f3be35",
  "type": "Product",
  "properties": {
   "lifecycle_stage": "live",
   "short_description": "short",
   "permalink": "internet-org",
   "homepage_url": "http://internet.org",
   "name": "Internet.org",
   "description": "Description",
   "launched_on_year": 2013,
   "launched_on_day": 1,
   "launched_on_month": 8,
   "launched_on": "2013-08-01",
   "launched_on_trust_code": 6,
   "created_at": 1406929558,
   "updated_at": 1406929776,
   "owner_name": "Facebook",
   "owner_path": "organization/facebook"
 },
"relationships": {
   "primary_image": {
    "paging": {
     "total_items": 1,
     "first_page_url": "https://api.crunchbase.com/v/2/product/internet-org/primary_image",
     "sort_order": "created_at DESC"
    },
    "items": [
     {
      "type": "ImageAsset",
      "title": None,
      "path": "image/upload/v1406929651/mxamrknopytunfw9xlin.jpg",
      "created_at": 1406929654,
      "updated_at": 1406929654
     }
    ]
   },
   "images": {
    "paging": {
     "total_items": 1,
     "first_page_url": "https://api.crunchbase.com/v/2/product/internet-org/images",
     "sort_order": "created_at DESC"
    },
    "items": [
     {
      "type": "ImageAsset",
      "title": None,
      "path": "image/upload/v1406929774/eqvq7iqkemvm0dmfttcp.png",
      "created_at": 1406929776,
      "updated_at": 1406929776
     }
    ]
   },
   "websites": {
    "paging": {
     "total_items": 1,
     "first_page_url": "https://api.crunchbase.com/v/2/product/internet-org/websites",
     "sort_order": "created_at DESC"
    },
    "items": [
     {
      "url": "http://internet.org",
      "type": "WebPresence",
      "title": "homepage",
      "created_at": 1406929559,
      "updated_at": 1406929559
     }
    ]
   },
   "news": {
    "paging": {
     "total_items": 2,
     "first_page_url": "https://api.crunchbase.com/v/2/product/internet-org/news",
     "sort_order": "created_at DESC"
    },
    "items": [
     {
     "url": "http://example.com/1/",
      "author": "Author 1",
      "posted_on": "2014-07-30",
      "type": "PressReference",
      "title": "Title 1",
      "created_at": 1406929752,
      "updated_at": 1406929752
     },
     {
     "url": "http://example.com/2/",
      "author": "Author 2",
      "posted_on": "2014-07-31",
      "type": "PressReference",
      "title": "Title 2",
      "created_at": 1406929720,
      "updated_at": 1406929720
     }
    ]
   }
  }
}


class ProductTestCase(TestCase):
    def test_properties(self):
        product = Product(PRODUCT_DATA)
        self.assertEqual(product.lifecycle_stage, "live")
        self.assertEqual(product.short_description, "short")
        self.assertEqual(product.permalink, "internet-org")
        self.assertEqual(product.homepage_url, "http://internet.org")
        self.assertEqual(product.name, "Internet.org")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.launched_on_year, 2013)
        self.assertEqual(product.launched_on_day, 1)
        self.assertEqual(product.launched_on_month, 8)
        self.assertEqual(product.launched_on, datetime(2013, 8, 1))
        self.assertEqual(product.launched_on_trust_code, 6)
        self.assertEqual(product.created_at, 1406929558)
        self.assertEqual(product.updated_at, 1406929776)
        self.assertEqual(product.owner_name, "Facebook")
        self.assertEqual(product.owner_path, "organization/facebook")

    def test_relationships(self):
            product = Product(PRODUCT_DATA)
            self.assertEqual(len(product.primary_image), 1)
            self.assertEqual(len(product.images), 1)
            self.assertEqual(len(product.websites), 1)
            self.assertEqual(len(product.news), 2)
