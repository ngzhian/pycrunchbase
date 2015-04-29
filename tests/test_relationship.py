from unittest import TestCase

from pycrunchbase import Relationship

PAST_TEAM_RELATIONSHIP = {
    "cardinality": "OneToMany",
    "paging": {
        "total_items": 3,
        "first_page_url": "https://api.crunchbase.com/v/3/"
        "organization/example/past_team",
        "sort_order": "created_at DESC"
    },
    "items": [
        {
            "first_name": "First",
            "last_name": "Last",
            "title": "Director of Title",
            "started_on": None,
            "ended_on": None,
            "path": "person/first-last",
            "created_at": 1234567890,
            "updated_at": 1234567890,
        }
    ]
}

HEADQUARTERS_RELATIONSHIP = {
    "cardinality": "OneToOne",
    "item": {
        "type": "Address",
        "uuid": "31adbab5e90fc45a47ae873e0656fadd",
        "properties": {
            "name": "Headquarters",
            "street_1": "1601 Willow Road",
            "street_2": None,
            "postal_code": "94025",
            "city": "Menlo Park",
            "city_web_path": "location/menlo-park/"
            "1f8abfef5379b26b702005a09908492f",
            "region": "California",
            "region_web_path": "location/california/"
            "eb879a83c91a121e0bb8829782dbcf04",
            "country": "United States",
            "country_web_path": "location/united-states/"
            "f110fca2105599f6996d011c198b3928",
            "latitude": 37.41605,
            "longitude": -122.151801,
            "created_at": 1205362453,
            "updated_at": 1398138077
        }
    }
}


class RelationshipTestCase(TestCase):
    def test_one_to_many_relationship(self):
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        one = past_team.get(0)
        self.assertEqual(one.first_name, "First")
        self.assertEqual('past_team', past_team.name)

    def test_one_to_one_relationship(self):
        hq = Relationship('headquarters', HEADQUARTERS_RELATIONSHIP)
        self.assertEqual(hq.name, "Headquarters")
