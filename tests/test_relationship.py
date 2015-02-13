from unittest import TestCase

from mock import patch

from pycrunchbase import CrunchBase, Relationship
from pycrunchbase.resource.pageitem import NonePageItem

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

    def test_relationship_exceed_total_items(self):
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        one = past_team.get(2)
        self.assertFalse(one)
        self.assertIsInstance(one, NonePageItem)

    @patch.object(CrunchBase, '_make_request')
    def test_load_more_error(self, mock_response):
        mock_response.return_value = {'data': {'error': 'error'}}
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        one = past_team.get(2)
        self.assertFalse(one)
        self.assertIsInstance(one, NonePageItem)

    def test_retrieval(self):
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        with self.assertRaises(TypeError):
            past_team['bad']

        self.assertEqual(past_team[0], past_team.get(0))

    def test_iterate(self):
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        members = [member for member in past_team]
        self.assertEqual(1, len(members))
        self.assertEqual(past_team[0], members[0])
