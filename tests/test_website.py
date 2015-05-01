from unittest import TestCase

from pycrunchbase import Website

TEST_DATA = {
    "type": "Website",
    "uuid": "6e11f9b6b0ef6bb94bb245e52eb24523",
    "properties": {
        "website_type": "blog",
        "url": "http://website",
        "created_at": 1398019105,
        "updated_at": 1398019105
    }
}


class WebsiteTestCase(TestCase):
    def test_website_built(self):
        website = Website(TEST_DATA)
        self.assertEqual(website.website_type, "blog")
        self.assertEqual(website.url, "http://website")
        self.assertEqual(website.created_at, 1398019105)
        self.assertEqual(website.updated_at, 1398019105)

    def test_string(self):
        website = Website(TEST_DATA)
        str(website)
