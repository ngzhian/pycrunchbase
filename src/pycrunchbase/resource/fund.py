import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class Fund(Node):
    """Represents an Fund on CrunchBase
    Previously known as a FundRaise.
    """

    KNOWN_RELATIONSHIPS = [
        'venture_firm',
        'investor',
        'images',
        'videos',
        'news',
    ]

    KNOWN_PROPERTIES = [
        "api_path",
        "web_path",
        "name",
        "announced_on",
        "announced_on_trust_code",
        "money_raised",
        "money_raised_currency_code",
        "money_raised_usd",
        "created_at",
        "updated_at",
    ]

    def _coerce_values(self):
        """A delegate method to handle parsing all data and converting
        them into python values
        """
        # special cases to convert strings to pythonic value
        for attr in ['announced_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))

    def __str__(self):
        return 'FundRaise: %s (USD$%s)' % (
            self.name,
            self.money_raised_usd
        )

    def __repr__(self):
        return self.__str__()
