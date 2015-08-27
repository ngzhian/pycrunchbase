import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class Organization(Node):
    """Represents an Organization on CrunchBase"""

    KNOWN_RELATIONSHIPS = [
        'primary_image',
        'founders',
        'current_team',
        'past_team',
        'board_members_and_advisors',
        'investors',
        'owned_by',
        'sub_organizations',
        'headquarters',
        'offices',
        'products',
        'categories',
        'customers',
        'competitors',
        'members',
        'memberships',
        'funding_rounds',
        'investments',
        'acquisitions',
        'acquired_by',
        'ipo',
        'funds',
        'websites',
        'images',
        'videos',
        'news',
    ]

    KNOWN_PROPERTIES = [
        "permalink",
        "api_path",
        "web_path",
        "name",
        "also_known_as",
        "short_description",
        "description",
        "primary_role",
        "role_company",
        "role_investor",
        "role_group",
        "role_school",
        "founded_on",
        "founded_on_trust_code",
        "is_closed",
        "closed_on",
        "closed_on_trust_code",
        "num_employees_min",
        "num_employees_max",
        "total_funding_usd",
        "number_of_investments",
        "homepage_url",
        "created_at",
        "updated_at",
        "stock_exchange",
        "stock_symbol",
    ]

    def _coerce_values(self):
        """A delegate method to handle parsing all data and converting
        them into python values
        """
        # special cases to convert strings to pythonic value
        for attr in ['closed_on', 'founded_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))

    def __str__(self):
        return 'Organization: %s' % self.name

    def __repr__(self):
        return self.__str__()
