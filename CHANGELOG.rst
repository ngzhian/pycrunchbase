
Changelog
=========

0.1.5 (2015-02-13)
-----------------------------------------

* Add a `cb_url` attribute for all PageItem, this url is a CrunchBase page
  (not the API) that holds more information for a particular PageItem
  Allows you to make calls like::

    company.funding_rounds[0].cb_url

  to get the url of the page for the first funding round of `company`.

* A new page item, InvestorInvestmentPageItem, that is useful for FundingRound info::

    round = cb.funding_round('round_uuid')
    an_investor = round.investments[0]  # a InvestorInvestmentPageItem
    print(str(an_investor))  # prints: Investor Name $100000

* Add simplified Contribution guidelines in README

0.1.4 (2015-02-13)
-----------------------------------------

* Relationship retrieval is 0-based now, 1-based just doesn't fit well with array
* Better `__str__` for `Node` and `Relationship`
* `Relationship.get(i)` if `i` is too large or small will return a NonePageItem singleton

0.1.3 (2015-02-12)
-----------------------------------------

* Fix Relationship: wasn't using the right build method of PageItem
* Add test to checkk for the above
* remove unused reference to CrunchBase in Relationship


0.1.2 (2015-02-12)
-----------------------------------------

* PageItem and it's subclasses to represent an item within a relationship
  of a Node
* Cleanup of where utility methods live (parse_date)
* More tests as always, overall 98.21% coverage

0.1.0 (2015-02-21)
-----------------------------------------

* First release on PyPI.
