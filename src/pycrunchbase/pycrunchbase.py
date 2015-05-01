import requests
import six

from .resource import (
    Acquisition,
    FundingRound,
    Fund,
    IPO,
    Organization,
    Page,
    Person,
    Product,
)


@six.python_2_unicode_compatible
class CrunchBase(object):
    """Class that manages talking to CrunchBase API"""
    BASE_URL = 'https://api.crunchbase.com/v/3/'
    ORGANIZATIONS_URL = BASE_URL + 'organizations'
    LOCATIONS_URL = BASE_URL + 'locations'
    CATEGORIES_URL = BASE_URL + 'categories'
    PRODUCTS_URL = BASE_URL + 'products'

    def __init__(self, api_key=None):
        if not api_key:
            raise ValueError('API key for CrunchBase not supplied')
        self.api_key = api_key

    def organizations(self, name):
        """
        Search for a organization given a name, returns the first
        :class:`Page` of results

        Returns:
            Page or None
        """
        url = self.ORGANIZATIONS_URL
        data = self._make_request(url, {'name': name})
        if not data or data.get('error'):
            return None
        return Page(name, data)

    def organization(self, permalink):
        """Get the details of a organization given a organization's permalink.

        Returns:
            Organization or None
        """
        node_data = self.get_node('organizations', permalink)
        return Organization(node_data) if node_data else None

    def person(self, permalink):
        """Helper to maintain backward compatability"""
        return self.people(permalink)

    def people(self, permalink):
        """Get the details of a person given a person's permalink

        Returns:
            Person or None
        """
        node_data = self.get_node('people', permalink)
        return Person(node_data) if node_data else None

    def funding_round(self, uuid):
        """Get the details of a FundingRound given the uuid.

        Returns
            FundingRound or None
        """
        node_data = self.get_node('funding-rounds', uuid)
        return FundingRound(node_data) if node_data else None

    def acquisition(self, uuid):
        """Get the details of a acquisition given a uuid.

        Returns:
            Acquisition or None
        """
        node_data = self.get_node('acquisition', uuid)
        return Acquisition(node_data) if node_data else None

    def product(self, permalink):
        """Get the details of a product given a product permalink.

        Returns:
            Product or None
        """
        node_data = self.get_node('product', permalink)
        return Product(node_data) if node_data else None

    def products(self):
        """Gets a list of products on CrunchBase"""
        url = self.PRODUCTS_URL
        page = self._page('Products', url)
        return page

    def ipo(self, permalink):
        """Get the details of an ipo given a ipo uuid.

        Returns:
            IPO or None
        """
        node_data = self.get_node('ipo', permalink)
        return IPO(node_data) if node_data else None

    def fund(self, permalink):
        """Get the details of an fundraise given a fundraise uuid.

        Returns:
            Fund or None
        """
        node_data = self.get_node('funds', permalink)
        return Fund(node_data) if node_data else None

    def fundraise(self, permalink):
        """Get the details of an fundraise given a fundraise uuid.

        Returns:
            Fund or None
        """
        node_data = self.get_node('funds', permalink)
        return Fund(node_data) if node_data else None

    def locations(self):
        """
        Queries for a list of all active Locations,
        returns the first :class:`Page` of results.

        Returns:
            Page or None
        """
        url = self.LOCATIONS_URL
        page = self._page('Locations', url)
        return page

    def categories(self):
        """
        Queries for a list of all active Categories,
        returns the first :class:`Page` of results.

        Returns:
            Page or None
        """
        url = self.CATEGORIES_URL
        page = self._page('Categories', url)
        return page

    def get_node(self, node_type, uuid, params=None):
        """Get the details of a Node from CrunchBase.
        The node_type must match that of CrunchBase's, and the uuid
        is either the {uuid} or {permalink} as stated on their docs.

        Returns:
            dict: containing the data describing this node with the keys
            uuid, type, properties, relationships.
            Or None if there's an error.
        """
        node_url = self.BASE_URL + node_type + '/' + uuid
        data = self._make_request(node_url, params=params)
        if not data or data.get('error'):
            return None
        return data

    def more(self, page):
        """Given a Page, tries to get more data using the
        first_page_url or next_page_url given in the response.

        If page happens to be a Relationship, i.e. page.first_page_url
        is not None, we just call that url to retrieve the first page.

        Returns:
            None if there is no more page to get, else
            Relationship with the new data
        """
        if page.first_page_url:
            url_to_call = page.first_page_url
            return self._page(page.name, url_to_call)
        elif page.next_page_url:
            url_to_call = page.next_page_url
            return self._page(page.name, url_to_call)
        else:
            return None

    def _page(self, name, url):
        """Loads a page for a Node

        Args:
            name (str): name of page we are getting
            url (str): url of the page to make the call to

        Returns:
            page if we can get the data
            None if we have an error
        """
        data = self._make_request(url)
        if not data or data.get('error'):
            return None
        return Page(name, data)

    def _build_url(self, base_url, params=None):
        """Helper to build urls by appending all queries and the API key.
        The API key is always the last query parameter."""

        join_char = '&' if '?' in base_url else '?'

        params_string = '&'.join(
            '%s=%s' % (k, v) for k, v in six.iteritems(params or {}))

        if params_string:
            params_string += "&user_key=%s" % self.api_key
        else:
            params_string = "user_key=%s" % self.api_key

        return base_url + join_char + params_string

    def _make_request(self, url, params=None):
        """Makes the actual API call to CrunchBase"""
        final_url = self._build_url(url, params)
        response = requests.get(final_url)
        response.raise_for_status()
        return response.json().get('data')

    def __str__(self):
        return "pycrunchbase CrunchBase API"

    def __repr__(self):
        return self.__str__()
