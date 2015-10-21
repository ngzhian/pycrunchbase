import six


class PageItem(object):
    """A item within a Page.

    A page is a homogenous collection of PageItem, and there are many
    kinds of PageItem. :meth:`build` is a helper class method to
    help build the correct type of PageItem based on

    1. path, or
    2. type
    """
    def __init__(self, data):
        self.data = data
        for k, v in six.iteritems(data):
            setattr(self, k, v)
        if 'path' in self.data:
            setattr(self, 'cb_url', 'crunchbase.com/' + data.get('path'))

    @classmethod
    def build(cls, data):
        path = data.get('type', '').lower()
        if path == 'acquisition':
            from .acquisition import Acquisition
            return Acquisition(data)
        if path == 'fundinground':
            from .fundinground import FundingRound
            return FundingRound(data)
        if path == 'ipo':
            from .ipo import IPO
            return IPO(data)
        if path == 'organization' or path == 'organizationsummary':
            from .organization import Organization
            return Organization(data)
        if path == 'person' or path == 'personsummary':
            from .person import Person
            return Person(data)
        if path == 'product' or path == 'productsummary':
            from .product import Product
            return Product(data)
        if path == 'investorinvestment' or path == 'investment':
            from .investment import Investment
            return Investment(data)
        if path == 'location':
            from .location import Location
            return Location(data)
        if path == 'category':
            from .category import Category
            return Category(data)
        if path == 'fund':
            from .fund import Fund
            return Fund(data)
        if path == 'job':
            from .job import Job
            return Job(data)
        if path == 'address':
            from .address import Address
            return Address(data)
        if path == 'news' or path == 'pressreference':
            from .news import News
            return News(data)
        if path == 'image':
            from .image import Image
            return Image(data)
        if path == 'degree':
            from .degree import Degree
            return Degree(data)
        if path == 'video':
            from .video import Video
            return Video(data)
        if path == 'website':
            from .website import Website
            return Website(data)
        if path == 'stockexchange':
            from .stockexchange import StockExchange
            return StockExchange(data)

        from .node import Node
        return Node(data)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'PageItem: %s' % self.data


class UuidPageItem(PageItem):
    def __init__(self, data):
        uuid = data.get('uuid')
        setattr(self, 'uuid', uuid)
        super(UuidPageItem, self).__init__(data)


class PermalinkPageItem(PageItem):
    def __init__(self, data):
        permalink = data.get('properties', {}).get('permalink')
        setattr(self, 'permalink', permalink)
        super(PermalinkPageItem, self).__init__(data)


@six.python_2_unicode_compatible
class NonePageItem(PageItem):
    def __init__(self):
        super(NonePageItem, self).__init__({})

    def __getattr__(self, attr):
        return None

    def __len__(self):
        return 0

    def __str__(self):
        return 'NonePageItem'

NonePageItemSingleton = NonePageItem()
