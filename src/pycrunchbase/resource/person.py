import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class Person(Node):
    """Represents a Person on CrunchBase"""

    KNOWN_RELATIONSHIPS = [
        "primary_affiliation",
        "primary_location",
        "primary_image",
        "websites",
        "degrees",
        "jobs",
        "advisory_roles",
        "founded_companies",
        "investments",
        "memberships",
        "images",
        "videos",
        "news",
    ]

    KNOWN_PROPERTIES = [
        "permalink",
        "api_path",
        "web_path",
        "last_name",
        "first_name",
        "also_known_as",
        "bio",
        "role_investor",
        "born_on",
        "born_on_trust_code",
        "is_deceased",
        "died_on",
        "died_on_trust_code",
        "created_at",
        "updated_at",
    ]

    def _coerce_values(self):
        """A delegate method to handle parsing all data and converting
        them into python values
        """
        # special cases to convert strings to pythonic value
        for attr in ['born_on', 'died_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))

    def __str__(self):
        return u'{first} {last} ({permalink})'.format(
            first=self.first_name,
            last=self.last_name,
            permalink=self.permalink,
        )

    def __repr__(self):
        return self.__str__()
