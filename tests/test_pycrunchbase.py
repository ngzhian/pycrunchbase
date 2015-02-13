from unittest import TestCase

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

import json

from requests.exceptions import HTTPError

import httpretty

from pycrunchbase import CrunchBase, Relationship

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
      "first_name": "First",
      "last_name": "Last",
      "title": "Director of Title",
      "started_on": null,
      "ended_on": null,
      "path": "person/first-last",
      "created_at": 1234567890,
      "updated_at": 1234567890
     },
     {
      "first_name": "First",
      "last_name": "Last",
      "title": "Director of Title",
      "started_on": null,
      "ended_on": null,
      "path": "person/first-last",
      "created_at": 1234567890,
      "updated_at": 1234567890
     },
     {
      "first_name": "First",
      "last_name": "Last",
      "title": "Director of Title",
      "started_on": null,
      "ended_on": null,
      "path": "person/first-last",
      "created_at": 1234567890,
      "updated_at": 1234567890
     }
    ]
}'''

PAST_TEAM_RELATIONSHIP = '''{
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
      "started_on": null,
      "ended_on": null,
      "path": "person/first-last",
      "created_at": 1234567890,
      "updated_at": 1234567890
     }
    ]
   }'''


class CrunchBaseTestCase(TestCase):
    base_url = 'https://api.crunchbase.com/v/2/'
    organizations_url = base_url + 'organizations'
    organization_url = base_url + 'organization'

    def test_missing_api_key(self):
        with self.assertRaises(ValueError):
            CrunchBase(None)

    @httpretty.activate
    def test_search_for_organization_fails(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/organizations?'
            'user_key=123&name=organization',
            body='''{
            }''')
        cb = CrunchBase('123')
        data = cb.organizations('organization')
        self.assertIsNone(data)

    @httpretty.activate
    def test_get_crunchbase_organization_returns_organization(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/organization/organization?'
            'user_key=123',
            body='''{
                "data": {
                    "uuid": "df6628127f970b439d3e12f64f504fbb",
                    "type": "Organization",
                    "properties": {
                        "description": "Description",
                        "short_description": "short description"
                    }
                }
            }''')
        cb = CrunchBase('123')
        organization = cb.organization('organization')
        self.assertEqual(organization.description, "Description")

    @httpretty.activate
    def test_get_crunchbase_organization_fails(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/organization/organization?'
            'user_key=123',
            body='''{
            }''')
        cb = CrunchBase('123')
        data = cb.organization('organization')
        self.assertIsNone(data)

    @httpretty.activate
    def test_search_for_organization_returns_a_list_of_matches(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/organizations?'
            'user_key=123&name=organization',
            body='''{
             "metadata": {
              "image_path_prefix": "https://example.com/",
              "www_path_prefix": "https://www.crunchbase.com/",
              "api_path_prefix": "https://api.crunchbase.com/v/2/",
              "version": 2
             },
             "data": {
              "paging": {
               "items_per_page": 1000,
               "current_page": 1,
               "number_of_pages": 1,
               "next_page_url": null,
               "prev_page_url": null,
               "total_items": 6,
               "sort_order": "custom"
              },
              "items": [
               {
                "updated_at": 1415895087,
                "created_at": 1371717055,
                "path": "organization/organization",
                "name": "organization",
                "type": "Organization"
               },
               {
                "updated_at": 1415768560,
                "created_at": 1310530681,
                "path": "organization/organization2",
                "name": "organization2",
                "type": "Organization"
               }
              ]
             }
            }''')
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/organization/organization?'
            'user_key=123',
            body='''{
             "data": {
              "properties": {
                  "description": "Description",
                  "short_description": "short description"
              },
              "relationships": {
               "news": {
                "paging": {
                 "total_items": 1,
                 "first_page_url": "https://api.crunchbase.com/v/2/\
                                    organization/organization/news",
                 "sort_order": "created_at DESC"
                },
                "items": [
                 {
                  "url": "https://example.com",
                  "author": null,
                  "posted_on": null,
                  "type": "PressReference",
                  "title": "Article Title",
                  "created_at": 1393522999,
                  "updated_at": 2014
                 }
                ]
               }
              }
              }}''')

        cb = CrunchBase('123')
        organization = cb.organizations('organization')
        self.assertEqual('Description', organization.description)
        self.assertTrue(organization.news)
        self.assertEqual('Article Title', organization.news.get(0).title)

    def test_exception_raised_when_making_calls(self):
        with patch('pycrunchbase.pycrunchbase.requests') as mock_request:
            mock_request.get = Mock(side_effect=HTTPError())
            httpretty.register_uri(
                httpretty.GET,
                'https://api.crunchbase.com/v/2/organizations?'
                'user_key=123&name=organization',
                body='''{
                }''')
            cb = CrunchBase('123')
            cb.organizations('organization')

    @httpretty.activate
    def test_more_relationship_for_relationship_summary(self):
        """Load more relationship data from summary"""
        data = {'data': json.loads(MOCK_RELATIONSHIP_PAGE)}
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/organization/example/past_team'
            '?user_key=123',
            body=json.dumps(data))

        rs = Relationship('past_team', json.loads(PAST_TEAM_RELATIONSHIP))
        cb = CrunchBase('123')

        rs = cb.more(rs)
        self.assertIsNotNone(rs)
        self.assertEquals(3, len(rs))

    def test_more_relationship_for_relationship_page1(self):
        """At summary page, there is no more next page, so return None"""
        past_team = json.loads(PAST_TEAM_RELATIONSHIP)
        past_team['paging']['total_items'] = 1
        rs = Relationship('past_team', past_team)
        cb = CrunchBase('123')

        self.assertIsNone(cb.more(rs))

    @httpretty.activate
    def test_more_relationship_for_relationship_page2(self):
        """At page 1, there is no more next page, so return None"""
        return_data = json.loads(MOCK_RELATIONSHIP_PAGE)
        return_data['paging']['total_items'] = 6
        return_data['paging']['first_page_url'] = None
        return_data['paging']['items_per_page'] = 3
        return_data['paging']['next_page_url'] = (
            'https://api.crunchbase.com/v/2/organization/example/past_team'
            'user_key=123&page=2')
        rs = Relationship('past_team', return_data)

        return_data['paging']['next_page_url'] = None
        return_data['paging']['current_page'] = 2
        data = {'data': return_data}
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/organization/example/past_team'
            'user_key=123&page=2',
            body=json.dumps(data))
        cb = CrunchBase('123')
        rs = cb.more(rs)

        self.assertIsNotNone(rs)
        self.assertEqual(2, rs.current_page)

    @httpretty.activate
    def test_get_funding_round_data(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/funding-round/uuid1'
            '?user_key=123',
            body='''{
                "data": {
                    "uuid": "uuid1",
                    "type": "FundingRound",
                    "properties": {
                        "funding_type": "private_equity",
                        "money_raised": 1000000
                    }
                }
            }''')
        cb = CrunchBase('123')
        organization = cb.funding_round('uuid1')
        self.assertEqual(organization.funding_type, "private_equity")
        self.assertEqual(organization.money_raised, 1000000)

    @httpretty.activate
    def test_get_person_data(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/person/name'
            '?user_key=123',
            body='''{
                "data": {
                    "uuid": "uuid1",
                    "type": "Person",
                    "properties": {
                        "last_name": "Last",
                        "first_name": "First"
                    }
                }
            }''')
        cb = CrunchBase('123')
        person = cb.person('name')
        self.assertEqual(person.last_name, "Last")
        self.assertEqual(person.first_name, "First")

    @httpretty.activate
    def test_get_product_data(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/product/permalink1'
            '?user_key=123',
            body='''{
                "data": {
                    "uuid": "uuid1",
                    "type": "Person",
                    "properties": {
                        "lifecycle_stage": "Stage",
                        "permalink": "permalink1"
                    }
                }
            }''')
        cb = CrunchBase('123')
        product = cb.product('permalink1')
        self.assertEqual(product.lifecycle_stage, "Stage")
        self.assertEqual(product.permalink, "permalink1")

    @httpretty.activate
    def test_get_acquisition_data(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://api.crunchbase.com/v/2/acquisition/uuid1'
            '?user_key=123',
            body='''{
                "data": {
                    "uuid": "uuid1",
                    "type": "Person",
                    "properties": {
                        "disposition_of_acquired": "Combined",
                        "acquisition_type": "Acqui-hire"
                    }
                }
            }''')
        cb = CrunchBase('uuid1')
        acquisition = cb.acquisition('uuid1')
        self.assertEqual(acquisition.disposition_of_acquired, "Combined")
        self.assertEqual(acquisition.acquisition_type, "Acqui-hire")
