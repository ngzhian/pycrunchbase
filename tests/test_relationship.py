from unittest import TestCase

from mock import patch

from pycrunchbase import CrunchBase, Relationship

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
        one = past_team.get(1)
        self.assertEqual(one.first_name, "First")

    def test_relationship_exceed_total_items(self):
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        one = past_team.get(3)
        self.assertIsNone(one)

    @patch.object(CrunchBase, '_make_request')
    def test_load_more_error(self, mock_response):
        mock_response.return_value = {'data': {'error': 'error'}}
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        one = past_team.get(3)
        self.assertIsNone(one)

    def test_retrieval(self):
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        with self.assertRaises(TypeError):
            past_team['bad']

        self.assertEqual(past_team[1], past_team.get(1))

    def test_iterate(self):
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        members = [member for member in past_team]
        self.assertEqual(1, len(members))
