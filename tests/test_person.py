from datetime import datetime
from unittest import TestCase

from pycrunchbase import Person

PERSON_DATA = {
 "uuid": "uuid",
 "type": "Person",
 "properties": {
  "role_investor": True,
  "last_name": "Last",
  "first_name": "First",
  "permalink": "first-last",
  "died_on_trust_code": 0,
  "died_on_day": None,
  "died_on_month": None,
  "died_on_year": None,
  "died_on": None,
  "bio": "Bio",
  "born_on_trust_code": 7,
  "born_on_day": 2,
  "born_on_month": 1,
  "born_on_year": 2000,
  "born_on": "2000-01-02",
  "created_at": 1233271545,
  "updated_at": 1419596914,
  "location_uuid": "locationid"
 },
 "relationships": {
  "news": {
   "paging": {
    "total_items": 2,
    "first_page_url": "https://api.crunchbase.com/v/2/person/first-last/news",
    "sort_order": "created_at DESC"
   },
   "items": [
    {
     "url": "http://example.com/news_1/",
     "author": "Author 1",
     "posted_on": "2012-12-28",
     "type": "PressReference",
     "title": "Title 1",
     "created_at": 1356743058,
     "updated_at": 2012
    },
    {
     "url": "example.com/news_2/",
     "author": "Author 2",
     "posted_on": "2012-04-20",
     "type": "PressReference",
     "title": "Title 2",
     "created_at": 1334962777,
     "updated_at": 2012
    },
   ]
  }
 }
}


class PersonTestCase(TestCase):
    def test_properties(self):
        person = Person(PERSON_DATA)
        self.assertEqual(person.role_investor, True)
        self.assertEqual(person.last_name, 'Last')
        self.assertEqual(person.first_name, 'First')
        self.assertEqual(person.permalink, 'first-last')
        self.assertEqual(person.died_on_trust_code, 0)
        self.assertEqual(person.died_on_day, None)
        self.assertEqual(person.died_on_month, None)
        self.assertEqual(person.died_on_year, None)
        self.assertEqual(person.died_on, None)
        self.assertEqual(person.bio, 'Bio')
        self.assertEqual(person.born_on_trust_code, 7)
        self.assertEqual(person.born_on_day, 2)
        self.assertEqual(person.born_on_month, 1)
        self.assertEqual(person.born_on_year, 2000)
        self.assertEqual(person.born_on, datetime(2000, 1, 2))
        self.assertEqual(person.location_uuid, 'locationid')

    def test_relationships(self):
        person = Person(PERSON_DATA)
        self.assertIsNotNone(person.news)
        self.assertEqual(2, len(person.news))
