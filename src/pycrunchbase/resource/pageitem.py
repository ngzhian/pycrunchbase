import six


class PageItem(object):
    def __init__(self, data):
        for k, v in six.iteritems(data):
            setattr(self, k, v)

        # if this page item is a Node on CrunchBase, it probably has a path
        # we copy it to cbid so we can refer to it when grabbing details
        path = getattr(self, 'path', None)
        if path:
            setattr(self, 'cbid', path.split('/')[-1])


class NonePageItem(object):
    def __getattr__(self, attr):
        return None

    def __len__(self):
        return 0


NonePageItemSingleton = NonePageItem()
