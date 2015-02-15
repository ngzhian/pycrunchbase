from unittest import TestCase

from pycrunchbase import Relationship

PAST_TEAM_RELATIONSHIP = {
    "paging": {
     "total_items": 3,
     "first_page_url": "https://api.crunchbase.com/v/2/\
organization/example/past_team",
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
      "updated_at": 1234567890
     }
    ]
   }


class RelationshipTestCase(TestCase):
    def test_relationship(self):
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        one = past_team.get(0)
        self.assertEqual(one.first_name, "First")
        self.assertEqual(one.permalink, "first-last")
        self.assertEqual('past_team', past_team.name)
