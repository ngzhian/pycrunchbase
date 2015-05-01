import six

from .node import Node
from .utils import parse_date


@six.python_2_unicode_compatible
class Degree(Node):
    """Represents a Degree on CrunchBase"""

    KNOWN_PROPERTIES = [
        # 'type',
        # 'uuid',
        'started_on',
        'started_on_trust_code',
        'is_completed',
        'completed_on',
        'completed_on_trust_code',
        'degree_type_name',
        'degree_subject',
        'created_at',
        'updated_at',
    ]

    KNOWN_RELATIONSHIPS = [
        'school',
        'person',
    ]

    def _coerce_values(self):
        for attr in ['started_on', 'completed_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))

    def __str__(self):
        return u'{name} {subject}'.format(
            name=self.degree_type_name,
            subject=self.degree_subject,
        )

    def __repr__(self):
        return self.__str__()
