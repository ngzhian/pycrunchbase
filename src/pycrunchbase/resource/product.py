import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class Product(Node):
    """Represents a Product on CrunchBase"""

    KNOWN_PROPERTIES = [
        "permalink",
        "api_path",
        "web_path",
        "name",
        "also_known_as",
        "lifecycle_stage",
        "launched_on",
        "launched_on_trust_code",
        "closed_on",
        "closed_on_trust_code",
        "homepage_url",
        "short_description",
        "description",
        "created_at",
        "updated_at",
    ]

    KNOWN_RELATIONSHIPS = [
        "owner",
        "categories",
        "primary_image",
        "competitors",
        "customers",
        "websites",
        "images",
        "videos",
        "news",
    ]

    def _coerce_values(self):
        for attr in ['launched_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))

    def __str__(self):
        return u'{name} by {owner}'.format(
            name=self.name,
            owner=self.owner_name
        )

    def __repr__(self):
        return self.__str__()
