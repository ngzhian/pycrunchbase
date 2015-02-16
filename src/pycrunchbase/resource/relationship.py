import six

from .page import Page
from .pageitem import NonePageItemSingleton


class Relationship(Page):
    """A Relationhip represents relationship between a Node and interesting
    information regarding the Node.

    This is a summary returned alongside the Node details information, e.g.
    ad call to /organizatin/example will return many properties and many
    relationships.

    To get more details of this relationship, call :class:`CrunchBase`'s
    :meth:`more`.
    """

    def __str__(self):
        return ("Relationship {name} Total items: {total}").format(
            name=self.name,
            total=self.total_items,
        )


@six.python_2_unicode_compatible
class NoneRelationship(Relationship):
    def __init__(self):
        super(NoneRelationship, self).__init__(
            None, {'paging': {}, 'items': {}})

    def get(self, _):
        return NonePageItemSingleton

    def __len__(self):
        return 0

    def __str__(self):
        return "NoneRelationship"

NoneRelationshipSingleton = NoneRelationship()
