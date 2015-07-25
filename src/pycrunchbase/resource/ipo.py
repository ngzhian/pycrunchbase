import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class IPO(Node):
    """Represents an IPO on CrunchBase"""

    KNOWN_RELATIONSHIPS = [
        'funded_company',
        'stock_exchange',
        'images',
        'videos',
        'news',
    ]

    KNOWN_PROPERTIES = [
        "api_path",
        "web_path",
        "went_public_on",
        "went_public_on_trust_code",
        "stock_exchange_symbol",
        "stock_symbol",
        "shares_sold",
        "opening_share_price",
        "opening_share_price_currency_code",
        "opening_share_price_usd",
        "opening_valuation",
        "opening_valuation_currency_code",
        "opening_valuation_usd",
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
        for attr in ['went_public_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))
        for attr in ['opening_share_price_usd', 'opening_share_price']:
            if getattr(self, attr, None):
                setattr(self, attr, float(getattr(self, attr)))

    def __str__(self):
        return 'IPO: %s' % (self.stock_symbol or self.stock_exchange_symbol, )

    def __repr__(self):
        return self.__str__()
