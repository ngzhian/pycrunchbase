from unittest import TestCase
from datetime import datetime

from pycrunchbase import Degree

TEST_DATA = {
    "type": "Degree",
    "uuid": "uuid",
    "properties": {
        "degree_type_name": "MS",
        "degree_subject": "Public Policy",
        "started_on": "2014-01-02",
        "started_on_trust_code": 7,
        "is_completed": False,
        "completed_on": None,
        "completed_on_trust_code": None,
        "created_at": 1210047688,
        "updated_at": 1397992862
    }
}


class DegreeTestCase(TestCase):
    def test_degree_built(self):
        degree = Degree(TEST_DATA)
        self.assertEqual(degree.degree_type_name, "MS")
        self.assertEqual(degree.degree_subject, "Public Policy")
        self.assertEqual(degree.started_on, datetime(2014, 1, 2))
        self.assertEqual(degree.started_on_trust_code, 7)
        self.assertEqual(degree.is_completed, False)
        self.assertEqual(degree.completed_on, None)
        self.assertEqual(degree.completed_on_trust_code, None)
        self.assertEqual(degree.created_at, 1210047688)
        self.assertEqual(degree.updated_at, 1397992862)

    def test_string(self):
        degree = Degree(TEST_DATA)
        str(degree)
