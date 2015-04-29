from unittest import TestCase

from pycrunchbase import Location

TEST_DATA = {
    "type": "Location",
    "uuid": "uuid",
    "properties": {
        "name": "New York",
        "location_type": "city",
        "parent_location_uuid": "uuidp",
        "created_at": 1229781627,
        "updated_at": 1397990749
    }
}


class LocationTestCae(TestCase):
    def test_location_built(self):
        location = Location(TEST_DATA)
        self.assertEqual(location.name, "New York")
        self.assertEqual(location.location_type, "city")
        self.assertEqual(location.parent_location_uuid, "uuidp")

    def test_string(self):
        location = Location(TEST_DATA)
        str(location)
