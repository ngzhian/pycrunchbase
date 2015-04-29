from unittest import TestCase

from pycrunchbase import Address

TEST_DATA = {
    "type": "Address",
    "uuid": "9e5927f1697ad924c7ac46482d2aeb31",
    "properties": {
        "name": "New York",
        "street_1": "340 Madison Ave",
        "street_2": None,
        "postal_code": "10017",
        "city": "New York",
        "city_web_path": "location/new-york/d64b7615985cfbf44affaa89d70c4050",
        "region": "New York",
        "region_web_path": "location/new-york/83ead471332bd02e67b767279aed075b",
        "country": "United States",
        "country_web_path": "location/united-states/f110fca2105599f6996d011c198b3928",
        "latitude": 40.7557162,
        "longitude": -73.9792469,
        "created_at": 1229781627,
        "updated_at": 1397990749
    }
}


class AddressTestCase(TestCase):
    def test_address_built(self):
        address = Address(TEST_DATA)
        self.assertEqual(address.name, "New York")
        self.assertEqual(address.street_1, "340 Madison Ave")
        self.assertEqual(address.street_2, None)
        self.assertEqual(address.postal_code, "10017")
        self.assertEqual(address.city, "New York")
        self.assertEqual(
            address.city_web_path,
            "location/new-york/d64b7615985cfbf44affaa89d70c4050")
        self.assertEqual(address.region, "New York")
        self.assertEqual(
            address.region_web_path,
            "location/new-york/83ead471332bd02e67b767279aed075b")
        self.assertEqual(address.country, "United States")
        self.assertEqual(
            address.country_web_path,
            "location/united-states/f110fca2105599f6996d011c198b3928")
        self.assertEqual(address.latitude, 40.7557162)
        self.assertEqual(address.longitude, -73.9792469)

    def test_string(self):
        address = Address(TEST_DATA)
        str(address)
