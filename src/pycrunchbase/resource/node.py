import json

from .relationship import NoneRelationshipSingleton, Relationship


class Node(object):
    KNOWN_RELATIONSHIPS = []
    KNOWN_PROPERTIES = []

    def __init__(self, data):
        """Accepts a dict or json string and constructs an
        object that represents a Node on CrunchBase
        """
        if not isinstance(data, dict):
            self.data = json.loads(data)
        else:
            self.data = data
        self.uuid = self.data.get('uuid')
        self._parse_properties()
        self._parse_relationship()
        self._coerce_values()

    def _parse_properties(self):
        """Nodes have properties, which are facts like the
        name, description, url etc.
        Loop through each of them and set it as attributes on this company so
        that we can make calls like
            company.name
            person.description
        """
        props_dict = self.data.get('properties', {})
        for prop_name in self.KNOWN_PROPERTIES:
            if prop_name in props_dict:
                setattr(self, prop_name, props_dict.get(prop_name))
            else:
                setattr(self, prop_name, None)

    def _parse_relationship(self):
        """Nodes have Relationships, and similarly to properties,
        we set it as an attribute on the Organization so we can make calls like
            company.current_team
            person.degrees
        """
        rs_dict = self.data.get('relationships', {})
        for rs_name in self.KNOWN_RELATIONSHIPS:
            if rs_name in rs_dict:
                setattr(
                    self, rs_name, Relationship(rs_name, rs_dict.get(rs_name)))
            else:
                # fill in other relationships with None values
                setattr(self, rs_name, NoneRelationshipSingleton)

    def _coerce_values(self):
        """Method that subclasses can override to coerce values,
        e.g. a date string to date object
        """
