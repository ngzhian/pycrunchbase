import six

from .node import Node


@six.python_2_unicode_compatible
class Website(Node):
    """Represents a Website on CrunchBase"""

    KNOWN_PROPERTIES = [
        'website_type',
        'url',
        'created_at',
        'updated_at',
    ]

    def __str__(self):
        return u'{website} {url}'.format(
            website=self.website_type,
            url=self.url,
        )

    def __repr__(self):
        return self.__str__()
