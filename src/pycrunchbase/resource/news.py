import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class News(Node):
    """Represents a News on CrunchBase"""

    KNOWN_PROPERTIES = [
        "title",
        "author",
        "posted_on",
        "url",
        "created_at",
        "updated_at",
    ]

    def _coerce_values(self):
        for attr in ['posted_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))

    def __str__(self):
        return u'{title} by {author} on {posted_on}'.format(
            title=self.title,
            author=self.author,
            posted_on=self.posted_on,
        )

    def __repr__(self):
        return self.__str__()
