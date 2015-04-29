from unittest import TestCase

import json

from pycrunchbase.resource.node import Node
from pycrunchbase.resource.utils import parse_date


class TestNode(Node):
    KNOWN_PROPERTIES = ['property1', 'property2']

    def _coerce_values(self):
        # intentionally coerce bad values for test purposes
        attr = 'property1'
        if getattr(self, attr, None):
            setattr(self, attr, parse_date(getattr(self, attr)))

data = {
    "type": "TestNode",
    "uuid": "uuid",
    'properties': {
        'property1': 'one',
        'property2': 'two'
    },
    'relationships': {
        'unknown': {
            'paging': {},
            'items': {}
        }
    },
}


class NodeTestCase(TestCase):
    def test_node_creation_from_dict(self):
        node = TestNode(data)
        self.assertEqual(node.property1, 'one')
        self.assertEqual(node.property2, 'two')

    def test_node_creation_from_string(self):
        node = TestNode(json.dumps(data))
        self.assertEqual(node.property1, 'one')
        self.assertEqual(node.property2, 'two')
