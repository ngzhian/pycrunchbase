import six


class PageItem(object):
    def __init__(self, data):
        self.data = data
        for k, v in six.iteritems(data):
            setattr(self, k, v)

    @classmethod
    def build(cls, data):
        path = data.get('path')
        if not path:
            return cls(data)
        if path.startswith('acquisition'):
            return AcquisitionPageItem(data)
        if path.startswith('funding-round'):
            return FundingRoundPageItem(data)
        if path.startswith('ipo'):
            return IpoPageItem(data)
        if path.startswith('organization'):
            return OrganizationPageItem(data)
        if path.startswith('person'):
            return PersonPageItem(data)
        if path.startswith('product'):
            return ProductPageItem(data)
        return cls(data)


class UuidPageItem(PageItem):
    def __init__(self, data):
        uuid = data.get('path').split('/')[-1]
        setattr(self, 'uuid', uuid)
        super(UuidPageItem, self).__init__(data)


class PermalinkPageItem(PageItem):
    def __init__(self, data):
        permalink = data.get('path').split('/')[-1]
        setattr(self, 'permalink', permalink)
        super(PermalinkPageItem, self).__init__(data)


class AcquisitionPageItem(UuidPageItem):
    pass


class FundingRoundPageItem(UuidPageItem):
    pass


class IpoPageItem(UuidPageItem):
    pass


class OrganizationPageItem(PermalinkPageItem):
    pass


class PersonPageItem(PermalinkPageItem):
    pass


class ProductPageItem(PermalinkPageItem):
    pass


class NonePageItem(object):
    def __getattr__(self, attr):
        return None

    def __len__(self):
        return 0


NonePageItemSingleton = NonePageItem()
