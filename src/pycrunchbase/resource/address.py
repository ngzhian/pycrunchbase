import six

from .node import Node


@six.python_2_unicode_compatible
class Address(Node):
    """Represents a Address on CrunchBase"""

    KNOWN_PROPERTIES = [
        "name",
        "street_1",
        "street_2",
        "postal_code",
        "city",
        "city_path",
        "city_web_path",  # this may not be needed
        "region",
        "region_path",
        "region_web_path",  # this may not be needed
        "country",
        "country_path",
        "country_web_path",  # this may not be needed
        "latitude",
        "longitude",
        "created_at",
        "updated_at",
    ]

    def _coerce_values(self):
        for attr in ['latitude', 'longitude']:
            if getattr(self, attr, None):
                setattr(self, attr, float(getattr(self, attr)))

    def __str__(self):
        return u'{name} {street_1}'.format(
            name=self.name,
            street_1=self.street_1,
        )

    def __repr__(self):
        return self.__str__()
