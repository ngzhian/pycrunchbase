import six

from .utils import safe_int
from .pageitem import NonePageItemSingleton, PageItem


@six.python_2_unicode_compatible
class Relationship(object):
    """A Relationhip represents relationship between a Node and interesting
    information regarding the Node.
    Relationships can be retrieved in two ways, via a call to a Node
    1. /organization/name
    or a direct call to a relationship page
    2. /organization/name/current_team
    We try to make this object easy to use by making this iterable,
    hiding the complexities of paging.

    A call of type 1. will only get the summary of the relationships,
    to get the details we need to explicitly call methods on
    CrunchBase and retrieve them.
    """
    def __init__(self, name, data):
        self.name = name
        paging = data.get('paging')
        self.total_items = safe_int(paging.get('total_items')) or 0
        self.first_page_url = paging.get('first_page_url')
        self.sort_order = paging.get('sort_order')

        # this are returnd by individual relationship pages
        # i.e. /organization/<organization>/past_team
        self.next_page_url = paging.get('next_page_url')
        self.prev_page_url = paging.get('prev_page_url')
        self.items_per_page = safe_int(paging.get('items_per_page'))
        # being on page 0 means this is a summary returned as part of the node
        self.number_of_pages = safe_int(paging.get('number_of_pages')) or 0

        self.items = [PageItem.build(item) for item in data.get('items')]
        self.current_page = paging.get('current_page') or 1

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError()
        return self.get(key)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        """Allows callers to iterate through a relationship like this:

            team_members = [member for member in company.current_team]
        """
        for item in six.moves.range(len(self)):
            yield self.get(item)

    def get(self, i):
        """Gets the i-th element of this relationship

        Args:
            i (int): 0-based index of the element to retrieve

        Returns:
            PageItem: if valid item exists at index i
            None if the index is too small or too large
        """
        if i < 0 or i >= len(self.items):
            return NonePageItemSingleton
        return self.items[i]

    def __str__(self):
        return "{name} {count}/{total}".format(
            name=self.name,
            count=len(self),
            total=self.total_items
        )


@six.python_2_unicode_compatible
class NoneRelationship(object):
    def get(self, _):
        return NonePageItemSingleton

    def __len__(self):
        return 0

    def __str__(self):
        return "NoneRelationship"

NoneRelationshipSingleton = NoneRelationship()
