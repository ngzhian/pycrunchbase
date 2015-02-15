====
Page
====

.. class:: Page
    A ``Page`` presents a page of results as returned by a query on an endpoint of CrunchBase, e.g. the `/organizations` endpoint.

    A ``Page`` contains information on how items there are per page, the current page number, amongst others.

    .. attribute:: items_per_page

        an ``int`` representing the maximum number of items there can be in a page

    .. attribute:: current_page

        The page number of this current page

    .. attribute:: number_of_pages

        Number of pages there are for this query result

    .. attribute:: next_page_url

        A url that you can request to get the next page of data

    .. attribute:: prev_page_url

        A url that you can request to get the prev page of data

    .. attribute:: total_items

        Total number of items that exist for this endpoint/query

    .. attribute:: sort_oder

        The sorting order of this list of results

    .. method:: get(i)

        Gets the i-th element in this page, 0-based.

        :param int i: Index of :class:`PageItem` to get, 0-based.
        :return: the :class:`PageItem`
        :rtype: :class:`PageItem`
        :raises IndexError: if i is out the bounds
        :raises TypeError: if i is not an int
