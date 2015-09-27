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
        'investors',
    ]

    def __str__(self):
        if self.money_invested:
            return u'{invested}'.format(
                self.money_invested
            )

        if hasattr(self, 'investors'):
            return u'{investors}'.format(self.investors)

        if self.type:
            return u'{type}'.format(self.type)

        return u'Investment'

    def __repr__(self):
        return self.__str__()
