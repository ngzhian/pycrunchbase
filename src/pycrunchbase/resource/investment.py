import six

from .node import Node


@six.python_2_unicode_compatible
class Investment(Node):
    """Represents a Investment (investor-investment) on CrunchBase"""

    KNOWN_PROPERTIES = [
        'type',
        'uuid',
        'money_invested',
        'money_invested_currency_code',
        'money_invested_usd',
    ]

    KNOWN_RELATIONSHIPS = [
        'funding_round',
        'invested_in',
    ]

    def __str__(self):
        return u'{series} {invested_in}'.format(
            series=self.funding_round.series,
            invested_in=self.invested_in.name,
        )

    def __repr__(self):
        return self.__str__()
