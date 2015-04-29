from unittest import TestCase

from pycrunchbase import Page


DATA = {
    "paging": {
        "items_per_page": 1000,
        "current_page": 1,
        "number_of_pages": 1,
        "next_page_url": None,
        "prev_page_url": None,
        "total_items": 1,
        "sort_order": "custom"
    },
    "items": [
     {
         "type": "OrganizationSummary",
         "uuid": "df6628127f970b439d3e12f64f504fbb",
         "properties": {
             "permalink": "facebook",
             "api_path": "organizations/facebook",
             "web_path": "organization/facebook",
             "name": "Facebook",
         }
     }
    ]
}


class PageTestCase(TestCase):
    def test_can_retrieve_valid_index(self):
        past_team = Page('data', DATA)
        one = past_team.get(0)
        self.assertEqual(one.name, "Facebook")
        self.assertEqual(one.permalink, "facebook")
        self.assertEqual(one.api_path, "organizations/facebook")
        self.assertEqual(one.web_path, "organization/facebook")

    def test_retrieving_out_of_bound_index(self):
        past_team = Page('data', DATA)
        with self.assertRaises(IndexError):
            past_team.get(2)

    def test_passing_in_bad_key(self):
        past_team = Page('data', DATA)
        with self.assertRaises(TypeError):
            past_team['bad']

        self.assertEqual(past_team[0], past_team.get(0))

    def test_iterate(self):
        past_team = Page('data', DATA)
        members = [member for member in past_team]
        self.assertEqual(1, len(members))
        self.assertEqual(past_team[0], members[0])
