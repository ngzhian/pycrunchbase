from six.moves import range

from .utils import safe_int
from .pageitem import NonePageItemSingleton, PageItem


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
    :class:`CrunchBase` and retrieve them.
    """
    def __init__(self, name, data, crunchbase=None):
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

        self.items = [PageItem(item) for item in data.get('items')]
        self.current_page = paging.get('current_page') or 1
        self.crunchbase = crunchbase

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
        for item in range(len(self)):
            yield self.get(item - 1)

    def get(self, i):
        """Gets the i-th element of this relationship

        Args:
            i(int): 1-based index of the element to retrieve

        Returns:
            :class:`PageItem` if valid item exists at index i
            None if the index is too small or too large
        """
        if (i < 1 or i > len(self.items)):
            return None
        if (i <= len(self.items)):
            return self.items[i-1]


class NoneRelationship(object):
    def get(self, i):
        return NonePageItemSingleton

    def __len__(self):
        return 0

NoneRelationshipSingleton = NoneRelationship()
