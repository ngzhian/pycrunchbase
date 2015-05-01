from unittest import TestCase

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

import json

from requests.exceptions import HTTPError

from pycrunchbase import CrunchBase, Relationship, Page

MOCK_RELATIONSHIP_PAGE = '''{
    "paging": {
      "total_items": 3,
      "items_per_page": 1000,
      "number_of_pages": 1,
      "current_page": 1,
      "next_page_url": null,
      "prev_page_url": null,
      "sort_order": "created_at desc"
    },
    "items": [
     {
      "type": "Job",
      "uuid": "befc22dec7892096e4d6919935cf4204",
      "properties": {
        "title": "Title 1",
        "started_on": null,
        "ended_on": null,
        "created_at": 1234567890,
        "updated_at": 1234567890
      }
     },
     {
      "type": "Job",
      "uuid": "a0e3eb89f81bc79ee797deae68e6ade7",
      "properties": {
        "title": "Title 2",
        "started_on": null,
        "ended_on": null,
        "created_at": 1234567890,
        "updated_at": 1234567890
      }
     },
     {
       "type": "Job",
       "uuid": "570bed9be95838b52045d84b30b80490",
       "properties": {
         "title": "Title 3",
         "started_on": null,
         "ended_on": null,
         "created_at": 1234567890,
         "updated_at": 1234567890
     }
     }
    ]
}'''

PAST_TEAM_RELATIONSHIP = '''{
    "cardinality": "OneToMany",
    "paging": {
     "total_items": 3,
     "first_page_url": "https://api.crunchbase.com/v/3/organizations/example/past_team",
     "sort_order": "created_at DESC"
    },
    "items": [
     {
       "type": "Job",
       "uuid": "570bed9be95838b52045d84b30b80490",
       "properties": {
         "title": "Title 3",
         "started_on": null,
         "ended_on": null,
         "created_at": 1234567890,
         "updated_at": 1234567890
       }
     }
    ]
   }'''


class CrunchBaseTestCase(TestCase):
    base_url = 'https://api.crunchbase.com/v/3/'
    organizations_url = base_url + 'organizations'
    organization_url = base_url + 'organization'

    def test_missing_api_key(self):
        with self.assertRaises(ValueError):
            CrunchBase(None)

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_search_for_organization_fails(self, mock_get):
        mock_get.return_value = Mock(json=Mock(return_value={}))

        cb = CrunchBase('123')
        data = cb.organizations('organization')

        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/organizations?'
            'name=organization&user_key=123')
        self.assertIsNone(data)

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_crunchbase_organization_returns_organization(self, mock_get):
        mock_json = make_mock_response_json({
                "data": {
                    "uuid": "df6628127f970b439d3e12f64f504fbb",
                    "type": "Organization",
                    "properties": {
                        "description": "Description",
                        "short_description": "short description"
                    }
                }
            })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        organization = cb.organization('organization')

        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/organizations/organization?'
            'user_key=123')
        self.assertEqual(organization.description, "Description")

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_crunchbase_organization_fails(self, mock_get):
        mock_json = make_mock_response_json({})
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        data = cb.organization('organization')

        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/organizations/organization?'
            'user_key=123')
        self.assertIsNone(data)

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_search_for_organization_returns_a_list_of_matches(self, mock_get):
        mock_json = make_mock_response_json({
            "metadata": {
                "image_path_prefix": "https://example.com/",
                "www_path_prefix": "https://www.crunchbase.com/",
                "api_path_prefix": "https://api.crunchbase.com/v/3/",
                "version": 2
                },
            "data": {
                "paging": {
                    "items_per_page": 1000,
                    "current_page": 1,
                    "number_of_pages": 1,
                    "next_page_url": None,
                    "prev_page_url": None,
                    "total_items": 6,
                    "sort_order": "custom"
                    },
                "items": [
                    {
                        "uuid": "uuid1",
                        "type": "Organization",
                        "properties": {
                            "updated_at": 1415895087,
                            "created_at": 1371717055,
                            "path": "organization/organization",
                            "name": "organization",
                        }
                    },
                    {
                        "uuid": "uuid2",
                        "type": "Organization",
                        "properties": {
                            "updated_at": 1415768560,
                            "created_at": 1310530681,
                            "path": "organization/organization2",
                            "name": "organization2",
                        }
                    }
                ]
            }
        })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        orgs = cb.organizations('organization')
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/organizations?'
            'name=organization&user_key=123')

        self.assertIsInstance(orgs, Page)

    def test_exception_raised_when_making_calls(self):
        with patch('pycrunchbase.pycrunchbase.requests') as mock_request:
            mock_request.get = Mock(side_effect=HTTPError())
            cb = CrunchBase('123')
            with self.assertRaises(HTTPError):
                cb.organizations('organization')

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_funding_round_data(self, mock_get):
        mock_json = make_mock_response_json({
            "data": {
                "uuid": "uuid1",
                "type": "FundingRound",
                "properties": {
                    "funding_type": "private_equity",
                    "money_raised": 1000000
                }
            }
        })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        organization = cb.funding_round('uuid1')

        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/funding-rounds/uuid1'
            '?user_key=123')
        self.assertEqual(organization.funding_type, "private_equity")
        self.assertEqual(organization.money_raised, 1000000)

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_person_data(self, mock_get):
        mock_json = make_mock_response_json({
            "data": {
                "uuid": "uuid1",
                "type": "Person",
                "properties": {
                    "last_name": "Last",
                    "first_name": "First"
                }
            }
        })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        person = cb.person('name')

        self.assertEqual(person.last_name, "Last")
        self.assertEqual(person.first_name, "First")
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/people/name'
            '?user_key=123')

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_product_data(self, mock_get):
        mock_json = make_mock_response_json({
            "data": {
                "uuid": "uuid1",
                "type": "Person",
                "properties": {
                    "lifecycle_stage": "Stage",
                    "permalink": "permalink1"
                }
            }
        })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        product = cb.product('permalink1')

        self.assertEqual(product.lifecycle_stage, "Stage")
        self.assertEqual(product.permalink, "permalink1")
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/product/permalink1'
            '?user_key=123')

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_acquisition_data(self, mock_get):
        mock_json = make_mock_response_json({
            "data": {
                "uuid": "uuid1",
                "type": "Person",
                "properties": {
                    "disposition_of_acquired": "Combined",
                    "acquisition_type": "Acqui-hire"
                }
            }
        })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        acquisition = cb.acquisition('uuid1')

        self.assertEqual(acquisition.disposition_of_acquired, "Combined")
        self.assertEqual(acquisition.acquisition_type, "Acqui-hire")
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/acquisition/uuid1'
            '?user_key=123')

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_ipo_data(self, mock_get):
        mock_json = make_mock_response_json({
            "data": {
                "uuid": "uuid1",
                "type": "Ipo",
                "properties": {
                    "stock_symbol": "SS",
                }
            }
        })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        ipo = cb.ipo('uuid1')

        self.assertEqual(ipo.stock_symbol, "SS")
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/ipo/uuid1'
            '?user_key=123')

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_fundraise_data(self, mock_get):
        mock_json = make_mock_response_json({
            "data": {
                "uuid": "uuidfundraise",
                "type": "FundRaise",
                "properties": {
                    "name": "Raise Round I",
                }
            }
        })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        fundraise = cb.fundraise('uuidfundraise')

        self.assertEqual(fundraise.name, "Raise Round I")
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/funds/uuidfundraise'
            '?user_key=123')

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_locations(self, mock_get):
        mock_json = make_mock_response_json({
            "metadata": {
                "image_path_prefix": "https://example.com/",
                "www_path_prefix": "https://www.crunchbase.com/",
                "api_path_prefix": "https://api.crunchbase.com/v/3/",
                "version": 2
                },
            "data": {
                "paging": {
                    "items_per_page": 1000,
                    "current_page": 1,
                    "number_of_pages": 1,
                    "next_page_url": None,
                    "prev_page_url": None,
                    "total_items": 2,
                    "sort_order": "name ASC"
                    },
                "items": [
                    {
                        "type": "Location",
                        "uuid": "uuid",
                        "properties": {
                            "name": "loc 1",
                            "location_type": "city",
                            "parent_location_uuid": "uuidp1",
                            "created_at": 1229781627,
                            "updated_at": 1397990749
                        }
                    },
                    {
                        "type": "Location",
                        "uuid": "uuid",
                        "properties": {
                            "name": "loc 2",
                            "location_type": "city",
                            "parent_location_uuid": "uuidp2",
                            "created_at": 1229781627,
                            "updated_at": 1397990749
                        }
                    },
                    ]
                }
            })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        locations = cb.locations()
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/locations?user_key=123')

        self.assertIsInstance(locations, Page)
        self.assertEqual(2, len(locations))
        self.assertEqual(locations[0].name, "loc 1")
        self.assertEqual(locations[0].parent_location_uuid, "uuidp1")
        self.assertEqual(locations[1].name, "loc 2")
        self.assertEqual(locations[1].parent_location_uuid, "uuidp2")
        self.assertIn('loc 1', str(locations[0]))

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_get_categories(self, mock_get):
        mock_json = make_mock_response_json({
            "metadata": {
                "image_path_prefix": "https://example.com/",
                "www_path_prefix": "https://www.crunchbase.com/",
                "api_path_prefix": "https://api.crunchbase.com/v/3/",
                "version": 2
                },
            "data": {
                "paging": {
                    "items_per_page": 1000,
                    "current_page": 1,
                    "number_of_pages": 1,
                    "next_page_url": None,
                    "prev_page_url": None,
                    "total_items": 2,
                    "sort_order": "name ASC"
                    },
                "items": [
                    {
                        "type": "Category",
                        "uuid": "uuid",
                        "properties": {
                            "name": "cat 1",
                            "organizations_in_category": 10,
                            "products_in_category": 9,
                            "created_at": 1229781627,
                            "updated_at": 1397990749
                        }
                    },
                    {
                        "type": "Category",
                        "uuid": "uuid",
                        "properties": {
                            "name": "cat 2",
                            "organizations_in_category": 10,
                            "products_in_category": 9,
                            "created_at": 1229781627,
                            "updated_at": 1397990749
                        }
                    }
                ]
            }
        })
        mock_get.return_value = mock_json

        cb = CrunchBase('123')
        categories = cb.categories()
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/categories?user_key=123')

        self.assertIsInstance(categories, Page)
        self.assertEqual(2, len(categories))
        self.assertEqual(categories[0].name, "cat 1")
        self.assertEqual(categories[0].organizations_in_category, 10)
        self.assertEqual(categories[0].products_in_category, 9)
        self.assertEqual(categories[1].name, "cat 2")
        self.assertEqual(categories[1].organizations_in_category, 10)
        self.assertEqual(categories[1].products_in_category, 9)
        self.assertIn('cat 1', str(categories[0]))


class LoadMoreTestCase(TestCase):
    def setUp(self):
        self.cb = CrunchBase('123')

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_more_from_relationship_summary_returns_error(self, mock_get):
        """Load more relationship data from summary"""
        mock_json = make_mock_response_json(
                {'data': {'error': 'error'}})
        mock_get.return_value = mock_json

        rs = Relationship('past_team', json.loads(PAST_TEAM_RELATIONSHIP))

        rs = self.cb.more(rs)
        self.assertIsNone(rs)
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/organizations/example/past_team'
            '?user_key=123')

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_more_relationship_for_relationship_summary(self, mock_get):
        """Load more relationship data from summary"""
        mock_json = make_mock_response_json(
            {'data': json.loads(MOCK_RELATIONSHIP_PAGE)})
        mock_get.return_value = mock_json

        rs = Relationship('past_team', json.loads(PAST_TEAM_RELATIONSHIP))

        rs = self.cb.more(rs)
        self.assertIsNotNone(rs)
        self.assertEquals(3, len(rs))

        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/organizations/example/past_team'
            '?user_key=123')

    @patch('pycrunchbase.pycrunchbase.requests.get')
    def test_more_relationship_for_relationship_page2(self, mock_get):
        """At page 1, there a next_page, get it and return the Relationship"""
        mock_json = make_mock_response_json({
            "data": {
                "cardinality": "OneToMany",
                "paging": {
                    "items_per_page": 8,
                    "current_page": 2,
                    "number_of_pages": 2,
                    "next_page_url": None,
                    "prev_page_url": None,
                    "total_items": 10,
                    "sort_order": "custom"
                },
                "items": [{}, {}]
            }
        })
        mock_get.return_value = mock_json

        data = {
            "cardinality": "OneToMany",
            "paging": {
                "total_items": 10,
                "first_page_url": "https://api.crunchbase.com/v/3/"
                "organizations/example/past_team?page=2",
                "sort_order": "custom"
            },
            "items": [{}, {}, {}, {}, {}, {}, {}, {}]
        }
        rs = Relationship('past_team', data)

        more_rs = self.cb.more(rs)

        self.assertEqual(2, len(more_rs))
        mock_get.assert_called_with(
            'https://api.crunchbase.com/v/3/organizations/example/past_team'
            '?page=2&user_key=123')


def make_mock_response_json(dict_to_return):
    return Mock(json=Mock(return_value=dict_to_return))
