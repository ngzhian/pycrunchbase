from datetime import datetime
from unittest import TestCase

from pycrunchbase import Acquisition

ACQUISITION_DATA = {
  "uuid": "4292239d4dbbc52eeee0856612ed9c47",
  "type": "Acquisition",
  "properties": {
   "disposition_of_acquired": "Combined",
   "acquisition_type": "Acqui-hire",
   "acquisition_status": "Pending",
   "payment_type": None,
   "announced_on_year": 2015,
   "announced_on_day": 16,
   "announced_on_month": 1,
   "announced_on": "2015-01-16",
   "announced_on_trust_code": 7,
   "price": None,
   "price_currency_code": "USD",
   "permalink": "4292239d4dbbc52eeee0856612ed9c47",
   "name": "Acquisition",
   "created_at": 1421443747,
   "updated_at": 1421689170
 },
 "relationships": {
  "acquirer": {
   "paging": {
    "total_items": 1,
    "first_page_url": "https://api.crunchbase.com/v/2/acquisition/4292239d4dbbc52eeee0856612ed9c47/acquirer",
    "sort_order": "created_at DESC"
   },
   "items": [
    {
     "type": "Organization",
     "name": "Facebook",
     "path": "organization/facebook",
     "created_at": 1180153335,
     "updated_at": 1423701973
    }
   ]
  },
  "acquiree": {
   "paging": {
    "total_items": 1,
    "first_page_url": "https://api.crunchbase.com/v/2/acquisition/4292239d4dbbc52eeee0856612ed9c47/acquiree",
    "sort_order": "created_at DESC"
   },
   "items": [
    {
     "type": "Organization",
     "name": "Teehan+Lax",
     "path": "organization/teehan-lax",
     "created_at": 1269182020,
     "updated_at": 1423382284
    }
   ]
  },
  "news": {
   "paging": {
    "total_items": 1,
    "first_page_url": "https://api.crunchbase.com/v/2/acquisition/4292239d4dbbc52eeee0856612ed9c47/news",
    "sort_order": "created_at DESC"
   },
   "items": [
    {
     "url": "http://techcrunch.com/2015/01/16/partners-at-teehanlax-the-design-firm-behind-medium-join-facebook/",
     "author": "Darrell Etherington",
     "posted_on": "2015-01-16",
     "type": "PressReference",
     "title": "Partners At Teehan+Lax, The Design Firm Behind Medium, Join Facebook",
     "created_at": 1421444079,
     "updated_at": 1423382296
    }
   ]
  }
 }
}


class AcquisitionTestCase(TestCase):
    def test_properties(self):
        acquisition = Acquisition(ACQUISITION_DATA)
        self.assertEqual(acquisition.disposition_of_acquired, "Combined")
        self.assertEqual(acquisition.acquisition_type, "Acqui-hire")
        self.assertEqual(acquisition.acquisition_status, "Pending")
        self.assertEqual(acquisition.payment_type, None)
        self.assertEqual(acquisition.announced_on_year, 2015)
        self.assertEqual(acquisition.announced_on_day, 16)
        self.assertEqual(acquisition.announced_on_month, 1)
        self.assertEqual(acquisition.announced_on, datetime(2015, 1, 16))
        self.assertEqual(acquisition.announced_on_trust_code, 7)
        self.assertEqual(acquisition.price, None)
        self.assertEqual(acquisition.price_currency_code, "USD")
        self.assertEqual(acquisition.permalink, "4292239d4dbbc52eeee0856612ed9c47")
        self.assertEqual(acquisition.name, "Acquisition")
        self.assertEqual(acquisition.created_at, 1421443747)
        self.assertEqual(acquisition.updated_at, 1421689170)

    def test_relationships(self):
        acquisition = Acquisition(ACQUISITION_DATA)
        self.assertEqual(len(acquisition.acquirer), 1)
        self.assertEqual(len(acquisition.acquiree), 1)
        self.assertEqual(len(acquisition.news), 1)
