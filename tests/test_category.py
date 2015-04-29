from unittest import TestCase

from pycrunchbase import Category

TEST_DATA = {
    "type": "Category",
    "uuid": "uuid",
    "properties": {
        "name": "Social",
        "organizations_in_category": 10,
        "products_in_category": 9,
        "created_at": 1229781627,
        "updated_at": 1397990749
    }
}


class LocationTestCase(TestCase):
    def test_location_built(self):
        category = Category(TEST_DATA)
        self.assertEqual(category.name, "Social")
        self.assertEqual(category.organizations_in_category, 10)
        self.assertEqual(category.products_in_category, 9)

    def test_string(self):
        category = Category(TEST_DATA)
        str(category)
