from datetime import datetime
from unittest import TestCase

from pycrunchbase import Acquisition

ACQUISITION_DATA = {
  "uuid": "4292239d4dbbc52eeee0856612ed9c47",
  "type": "Acquisition",
  "properties": {
   "price": None,
   "price_currency_code": "USD",
   "price_usd": None,
   "payment_type": None,
   "acquisition_type": "Acqui-hire",
   "acquisition_status": "Pending",
   "disposition_of_acquired": "Combined",
   "announced_on": "2015-01-16",
   "announced_on_trust_code": 7,
   "completed_on": "2015-01-20",
   "completed_on_trust_code": 7,
   "created_at": 1421443747,
   "updated_at": 1421689170
 },
 "relationships": {
  "acquirer": {
   "cardinality": "OneToOne",
   "item": {
       "type": "Organization",
       "uuid": "uuidorg",
       "properties": {
           "name": "Facebook",
           "created_at": 1180153335,
           "updated_at": 1423701973
       }
   }
  },
  "acquiree": {
   "cardinality": "OneToOne",
   "item": {
       "type": "Organization",
       "uuid": "uuidorg",
       "properties": {
           "name": "Teehan+Lax",
           "created_at": 1269182020,
           "updated_at": 1423382284
       }
       }
  },
 }
}


class AcquisitionTestCase(TestCase):
    def test_properties(self):
        acquisition = Acquisition(ACQUISITION_DATA)
        self.assertEqual(acquisition.price, None)
        self.assertEqual(acquisition.price_currency_code, "USD")
        self.assertEqual(acquisition.price_usd, None)
        self.assertEqual(acquisition.payment_type, None)
        self.assertEqual(acquisition.acquisition_type, "Acqui-hire")
        self.assertEqual(acquisition.acquisition_status, "Pending")
        self.assertEqual(acquisition.disposition_of_acquired, "Combined")
        self.assertEqual(acquisition.announced_on, datetime(2015, 1, 16))
        self.assertEqual(acquisition.announced_on_trust_code, 7)
        self.assertEqual(acquisition.completed_on, datetime(2015, 1, 20))
        self.assertEqual(acquisition.completed_on_trust_code, 7)
        self.assertEqual(acquisition.created_at, 1421443747)
        self.assertEqual(acquisition.updated_at, 1421689170)

    def test_relationships(self):
        acquisition = Acquisition(ACQUISITION_DATA)
        self.assertEqual(acquisition.acquirer.name, 'Facebook')
        self.assertEqual(acquisition.acquiree.name, "Teehan+Lax")
