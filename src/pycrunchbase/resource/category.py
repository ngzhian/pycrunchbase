import six

from .node import Node


@six.python_2_unicode_compatible
class Category(Node):
    """Represents a Category on CrunchBase"""

    KNOWN_PROPERTIES = [
        "path",
        "name",
        "organizations_in_category",
        "products_in_category",
        "created_at",
        "updated_at",
    ]

    def __str__(self):
        return u'{name} {orgs} organizations {prods} products'.format(
            name=self.name,
            orgs=self.organizations_in_category,
            prods=self.products_in_category,
        )

    def __repr__(self):
        return self.__str__()
