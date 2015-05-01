import six

from .node import Node


@six.python_2_unicode_compatible
class Degree(Node):
    """Represents a Degree on CrunchBase"""

    KNOWN_PROPERTIES = [
        'type',
        'uuid',
        'started_on',
        'completed_on',
        'degree_type_name',
        'degree_subject',
        'created_at',
        'updated_at',
    ]

    KNOWN_RELATIONSHIPS = [
        'school',
        'person',
    ]

    def __str__(self):
        return u'{name} {subject}'.format(
            name=self.degree_type_name,
            subject=self.degree_subject,
        )

    def __repr__(self):
        return self.__str__()
