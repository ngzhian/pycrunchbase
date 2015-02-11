===============================
pycrunchbase
===============================

| |docs| |travis| |appveyor| |coveralls| |landscape| |scrutinizer|
| |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/pycrunchbase/badge/?style=flat
    :target: https://readthedocs.org/projects/pycrunchbase
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/ngzhian/pycrunchbase/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ngzhian/pycrunchbase

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ngzhian/pycrunchbase?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ngzhian/pycrunchbase

.. |coveralls| image:: http://img.shields.io/coveralls/ngzhian/pycrunchbase/master.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/ngzhian/pycrunchbase

.. |landscape| image:: https://landscape.io/github/ngzhian/pycrunchbase/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ngzhian/pycrunchbase/master
    :alt: Code Quality Status

.. |version| image:: http://img.shields.io/pypi/v/pycrunchbase.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pycrunchbase

.. |downloads| image:: http://img.shields.io/pypi/dm/pycrunchbase.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/pycrunchbase

.. |wheel| image:: https://pypip.in/wheel/pycrunchbase/badge.png?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pycrunchbase

.. |supported-versions| image:: https://pypip.in/py_versions/pycrunchbase/badge.png?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pycrunchbase

.. |supported-implementations| image:: https://pypip.in/implementation/pycrunchbase/badge.png?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/pycrunchbase

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ngzhian/pycrunchbase/master.png?style=flat
    :alt: Scrtinizer Status
    :target: https://scrutinizer-ci.com/g/ngzhian/pycrunchbase/

Python bindings to CrunchBase

Examples
========

::

    cb = CrunchBase(API_KEY)
    github = cb.organization('github')
    funding_rounds_summary = github.funding_rounds

    more_funding_rounds = cb.more(funding_rounds_summary)

    funding_round_details = [
        cb.funding_round(round.cbid) for round in funding_rounds_summary
    ]


Installation
============

::

    pip install pycrunchbase

Documentation
=============

https://pycrunchbase.readthedocs.org/

Development
===========

To run the all tests run::

    tox

Goals
=====

1. Support all (or almost all) of CrunchBase's API functionalities
2. Speedy updates when CrunchBase's API changes
3. 'Pythonic' bindings, user doesn't feel like we're requesting URLs


TODO
===========

Support other nodes (Person, Product, FundingRound, Acquisition, IPO, FundRaise)

License
=======

MIT
