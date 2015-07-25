import six

from .node import Node


@six.python_2_unicode_compatible
class StockExchange(Node):
    """Represents a Website on CrunchBase"""

    KNOWN_PROPERTIES = [
        'name',
        'short_name',
        'symbol',
        'created_at',
        'updated_at',
    ]

    def __str__(self):
        return u'{name} {symbol}'.format(
            name=self.name,
            symbol=self.symbol,
        )

    def __repr__(self):
        return self.__str__()
