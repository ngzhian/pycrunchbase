import six

from .page import Page
from .pageitem import PageItem
from .pageitem import NonePageItemSingleton
from .utils import safe_int


class Relationship(object):
    """A Relationhip represents relationship between a Node and interesting
    information regarding the Node.

    This is a summary returned alongside the Node details information, e.g.
    ad call to /organizatin/example will return many properties and many
    relationships.

    To get more details of this relationship, call :class:`CrunchBase`'s
    :meth:`more`.
    """
    def __init__(self, name, data):
        cardinality = data.get('cardinality')
        self._name = name
        if cardinality in ['OneToMany', 'ManyToMany']:
            self.buildPage(name, data)
        else:
            self.buildPageItem(data)

    def buildPage(self, name, data):
        self.name = name
        paging = data.get('paging')
        self.total_items = safe_int(paging.get('total_items')) or 0
        self.first_page_url = paging.get('first_page_url')
        self.sort_order = paging.get('sort_order')

        self.next_page_url = paging.get('next_page_url')
        self.prev_page_url = paging.get('prev_page_url')
        self.items_per_page = safe_int(paging.get('items_per_page'))

        # if these 2 fields are 0, we know that this Page is a result of
        # a call to retrieve a relationship of a Node
        self.current_page = paging.get('current_page') or 0
        self.number_of_pages = safe_int(paging.get('number_of_pages')) or 0

        self.items = [PageItem.build(item) for item in data.get('items')]

    def buildPageItem(self, data):
        node = PageItem.build(data.get('item'))
        print(data)
        for prop in node.KNOWN_PROPERTIES:
            setattr(self, prop, getattr(node, prop))


    def __str__(self):
        return u"{total} {name} {items}".format(
            total=self.total_items,
            name=self.name,
            items=self.items,
        )

    def __getitem__(self, key):
        """Allows caller to use array indices to get a :class:`PageItem`

        Args:
            i (int): 0-based index of the element to retrieve

        Returns:
            PageItem: if valid item exists at index i
            None if the index is too small or too large
        """
        if not isinstance(key, int):
            raise TypeError()
        return self.items[key]

    def __len__(self):
        """Returns the number of items this Page holds"""
        return len(self.items)

    def __iter__(self):
        """Allows callers to iterate through the items of this page as such:

            team_members = [member for member in page_of_members]
        """
        return iter(self.items)

    def get(self, i):
        """Gets the i-th element of this page

        Args:
            i (int): 0-based index of the element to retrieve

        Returns:
            PageItem: if valid item exists at index i
            None if the index is too small or too large
        """
        return self[i]

    def __str__(self):
        return (u"Page {name} {current}/{pages} Per Page: {per_page} "
                u"Total items: {total}").format(
            name=self.name,
            current=self.current_page,
            pages=self.number_of_pages,
            per_page=self.items_per_page,
            total=self.total_items,
        )

    def __repr__(self):
        return self.__str__()

@six.python_2_unicode_compatible
class NoneRelationship(Relationship):
    def __init__(self):
        super(NoneRelationship, self).__init__(
        None, {'cardinality': 'OneToMany', 'paging': {}, 'items': {}})

    def get(self, _):
        return NonePageItemSingleton

    def __len__(self):
        return 0

    def __str__(self):
        return "NoneRelationship"

NoneRelationshipSingleton = NoneRelationship()
