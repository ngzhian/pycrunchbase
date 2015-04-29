import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class Job(Node):
    """Represents a Job on CrunchBase"""

    KNOWN_PROPERTIES = [
        "title",
        "started_on",
        "started_on_trust_code",
        "ended_on",
        "ended_on_trust_code",
        "created_at",
        "updated_at",
    ]

    KNOWN_RELATIONSHIPS = [
        "person",
    ]

    def _coerce_values(self):
        for attr in ['started_on', 'ended_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))

    def __str__(self):
        return (u'{title}').format(
            title=self.title,
        )

    def __repr__(self):
        return self.__str__()
