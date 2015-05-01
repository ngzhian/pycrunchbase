import six

from .node import Node


@six.python_2_unicode_compatible
class Image(Node):
    """Represents a Image on CrunchBase"""

    KNOWN_PROPERTIES = [
        # 'type',
        # 'uuid',
        'asset_path',
        'content_type',
        'height',
        'width',
        'filesize',
        'created_at',
        'updated_at',
    ]

    def __str__(self):
        return u'{asset_path}'.format(asset_path=self.asset_path)

    def __repr__(self):
        return self.__str__()
