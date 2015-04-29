import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class FundingRound(Node):
    """Represents a FundingRound on CrunchBase"""

    KNOWN_PROPERTIES = [
        "permalink",  # check that this is actually returned
        "api_path",
        "web_path",
        "funding_type",
        "series",
        "series_qualifier",
        "announced_on",
        "announced_on_trust_code",
        "closed_on",
        "closed_on_trust_code",
        "money_raised",
        "money_raised_currency_code",
        "money_raised_usd",
        "target_money_raised",
        "target_money_raised_currency_code",
        "target_money_raised_usd",
        "created_at",
        "updated_at",
    ]

    KNOWN_RELATIONSHIPS = [
        "investments",
        "funded_organization",
        "images",
        "videos",
        "news",
    ]

    def _coerce_values(self):
        for attr in ['announced_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))

    def __str__(self):
        return (u'{funding_type} ${money} on '
                u'{announced} by {investments}').format(
            funding_type=self.funding_type,
            money=self.money_raised_usd,
            announced=self.announced_on,
            investments=self.investments,
        )

    def __repr__(self):
        return self.__str__()
