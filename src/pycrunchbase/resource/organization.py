import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class Organization(Node):
    """Represents an Organization on CrunchBase
    API Docs: https://developer.crunchbase.com/docs
    """

    KNOWN_RELATIONSHIPS = [
        'acquisitions',
        'board_members_and_advisors',
        'categories',
        'competitors',
        'current_team',
        'customers',
        'founders',
        'funding_rounds',
        'headquarters',
        'images',
        'investments',
        'ipo',
        'members',
        'news',
        'offices',
        'past_team',
        'primary_image',
        'products',
        'sub_organizations'
        'websites',
    ]

    KNOWN_PROPERTIES = [
        'closed_on',
        'description',
        'founded_on',
        'homepage_url',
        'name',
        'number_of_employees',
        'number_of_investments',
        'permalink',
        'short_description',
        'stock_symbol',
        'total_funding_usd',
    ]

    def _coerce_values(self):
        """A delegate method to handle parsing all data and converting
        them into python values
        """
        # special cases to convert strings to pythonic value
        for attr in ['closed_on', 'founded_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))
        for attr in ['number_of_employees', 'number_of_investments']:
            if getattr(self, attr, None):
                setattr(self, attr, int(getattr(self, attr)))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
