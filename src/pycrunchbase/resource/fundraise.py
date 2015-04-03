import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class FundRaise(Node):
    """Represents an FundRaise on CrunchBase
    API Docs: https://developer.crunchbase.com/docs
    """

    KNOWN_RELATIONSHIPS = [
        'venture_firm',
        'news',
    ]

    KNOWN_PROPERTIES = [
        "money_raised_usd",
        "money_raised",
        "money_raised_currency_code",
        "permalink",
        "name",
        "announced_on_year",
        "announced_on_day",
        "announced_on_month",
        "announced_on",
        "announced_on_trust_code",
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
