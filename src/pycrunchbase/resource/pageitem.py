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
        path = data.get('path', '')
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
        if data.get('type') == 'InvestorInvestment':
            return InvestorInvestmentPageItem(data)
        return cls(data)

    def __repr__(self):
        return self.__str__()


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


@six.python_2_unicode_compatible
class AcquisitionPageItem(UuidPageItem):
    def __str__(self):
        return '{name} {announced_on}'.format(
            name=self.name,
            announced_on=self.announced_on,
        )


@six.python_2_unicode_compatible
class FundingRoundPageItem(UuidPageItem):
    def __str__(self):
        return self.name


@six.python_2_unicode_compatible
class InvestorInvestmentPageItem(PageItem):
    def __init__(self, data):
        super(InvestorInvestmentPageItem, self).__init__(data)
        if 'investor' in data:
            self.investor = PageItem.build(self.investor)
        if 'invested_in' in data:
            self.invested_in = PageItem.build(self.invested_in)

    def __str__(self):
        return '{investor} ${money}'.format(
            investor=self.investor,
            money=self.money_invested_usd,
        )


@six.python_2_unicode_compatible
class IpoPageItem(UuidPageItem):
    def __str__(self):
        return self.name


@six.python_2_unicode_compatible
class OrganizationPageItem(PermalinkPageItem):
    def __str__(self):
        return self.name


@six.python_2_unicode_compatible
class PersonPageItem(PermalinkPageItem):
    def __str__(self):
        return '{first} {last}'.format(
            first=self.first_name,
            last=self.last_name,
        )


@six.python_2_unicode_compatible
class ProductPageItem(PermalinkPageItem):
    def __str__(self):
        return self.name


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
