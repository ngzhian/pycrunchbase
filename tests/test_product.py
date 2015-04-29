from datetime import datetime
from unittest import TestCase

from pycrunchbase import Product

PRODUCT_DATA = {
  "uuid": "d00804b457a0a9743671d596e8f3be35",
  "type": "Product",
  "properties": {
   "permalink": "internet-org",
   "name": "Internet.org",
   "lifecycle_stage": "live",
   "launched_on": "2013-08-01",
   "launched_on_trust_code": 7,
   "closed_on": None,
   "closed_on_trust_code": 7,
   "homepage_url": "http://internet.org",
   "short_description": "short",
   "description": "Description",
   "created_at": 1406929558,
   "updated_at": 1406929776,
 },
"relationships": {
   "primary_image": {
    "cardinality": "OneToMany",
    "paging": {
     "total_items": 1,
     "first_page_url": "https://api.crunchbase.com/v/3/product/internet-org/primary_image",
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
    "cardinality": "OneToMany",
    "paging": {
     "total_items": 1,
     "first_page_url": "https://api.crunchbase.com/v/3/product/internet-org/images",
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
    "cardinality": "OneToMany",
    "paging": {
     "total_items": 1,
     "first_page_url": "https://api.crunchbase.com/v/3/product/internet-org/websites",
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
    "cardinality": "OneToMany",
    "paging": {
     "total_items": 2,
     "first_page_url": "https://api.crunchbase.com/v/3/product/internet-org/news",
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
        self.assertEqual(product.permalink, "internet-org")
        self.assertEqual(product.name, "Internet.org")
        self.assertEqual(product.lifecycle_stage, "live")
        self.assertEqual(product.launched_on, datetime(2013, 8, 1))
        self.assertEqual(product.launched_on_trust_code, 7)
        self.assertEqual(product.closed_on, None)
        self.assertEqual(product.homepage_url, "http://internet.org")
        self.assertEqual(product.short_description, "short")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.created_at, 1406929558)
        self.assertEqual(product.updated_at, 1406929776)

    def test_relationships(self):
        product = Product(PRODUCT_DATA)
        self.assertEqual(len(product.primary_image), 1)
        self.assertEqual(len(product.images), 1)
        self.assertEqual(len(product.websites), 1)
        self.assertEqual(len(product.news), 2)
