import six

from .node import Node


@six.python_2_unicode_compatible
class Location(Node):
    """Represents a Location on CrunchBase"""

    KNOWN_PROPERTIES = [
        "web_path",
        "name",
        "location_type",
        "parent_location_uuid",
        "created_at",
        "updated_at",
    ]

    KNOWN_RELATIONSHIPS = [
        "parent_locations",
    ]

    def __str__(self):
        return u'{name} {location_type}'.format(
            name=self.name,
            location_type=self.location_type,
        )

    def __repr__(self):
        return self.__str__()
