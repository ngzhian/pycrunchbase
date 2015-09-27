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
        path = data.get('type', '')
        if path == 'Acquisition':
            from .acquisition import Acquisition
            return Acquisition(data)
        if path == 'FundingRound':
            from .fundinground import FundingRound
            return FundingRound(data)
        if path == 'Ipo':
            from .ipo import IPO
            return IPO(data)
        if path == 'Organization' or path == 'OrganizationSummary':
            from .organization import Organization
            return Organization(data)
        if path == 'Person' or path == 'PersonSummary':
            from .person import Person
            return Person(data)
        if path == 'Product' or path == 'ProductSummary':
            from .product import Product
            return Product(data)
        if path == 'InvestorInvestment' or path == 'Investment':
            from .investment import Investment
            return Investment(data)
        if path == 'Location':
            from .location import Location
            return Location(data)
        if path == 'Category':
            from .category import Category
            return Category(data)
        if path == 'Fund':
            from .fund import Fund
            return Fund(data)
        if path == 'Job':
            from .job import Job
            return Job(data)
        if path == 'Address':
            from .address import Address
            return Address(data)
        if path == 'News':
            from .news import News
            return News(data)
        if path == 'Image':
            from .image import Image
            return Image(data)
        if path == 'Degree':
            from .degree import Degree
            return Degree(data)
        if path == 'Video':
            from .video import Video
            return Video(data)
        if path == 'Website':
            from .website import Website
            return Website(data)
        if path == 'StockExchange':
            from .stockexchange import StockExchange
            return StockExchange(data)
        return cls(data)

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
