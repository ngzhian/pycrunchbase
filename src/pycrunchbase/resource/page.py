import six

from .utils import safe_int
from .pageitem import PageItem


@six.python_2_unicode_compatible
class Page(object):
    """A Page represents a a page of results returned by CrunchBase.
    Page contains useful information regarding how many items there are
    in total (total_items), items per page (items_per_page), etc.

    A page contains information for going to the prev/next page (if available).

    The data that is used to initialize a Page looks like this::

        "data": {
            "paging": {
                "items_per_page": 1000,
                "current_page": 1,
                "number_of_pages": 1,
                "next_page_url": null,
                "prev_page_url": null,
                "total_items": 1,
                "sort_order": "custom"
            },
            "items": [
             {
                 "updated_at": 1423666090,
                 "created_at": 1371717055,
                 "path": "organization/example",
                 "name": "Example",
                 "type": "Organization"
             }
            ]
        }

    A special note is that current_page might be 0, this is when
    the page is returned as part of a :class:`Relationship`.
    """
    def __init__(self, name, data):
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
        return ("Page {name} {current}/{pages} Per Page: {per_page} "
                "Total items: {total}").format(
            name=self.name,
            current=self.current_page,
            pages=self.number_of_pages,
            per_page=self.items_per_page,
            total=self.total_items,
        )

    def __repr__(self):
        return self.__str__()
