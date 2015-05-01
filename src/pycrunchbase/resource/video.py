import six

from .node import Node


@six.python_2_unicode_compatible
class Video(Node):
    """Represents a Video on CrunchBase"""

    KNOWN_PROPERTIES = [
        'title',
        'service_name',
        'url',
        'created_at',
        'updated_at',
    ]

    def __str__(self):
        return u'{title} {service} {url}'.format(
            title=self.title,
            service=self.service_name,
            url=self.url,
        )

    def __repr__(self):
        return self.__str__()
