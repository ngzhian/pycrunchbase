=====
Usage
=====

To use pycrunchbase in a project::

    import pycrunchbase

Instantiate your :class:`CrunchBase` using your API Key::

    cb = pycrunchbase.CrunchBase(API_KEY)

Get details about an organization::

    github = cb.organization('github')

Get properties about the organization::

    what_is_github = github.description
    where_is_github = github.homepage_url

Get relationships (summarized version) about the organization::

    github_team = github.current_team
    who_started_github = github.founders
    in_the_news = github.news

Get more relationships about the organization::

    more_news = cb.more(in_the_news)
    all_news_urls = [news.url for news in more_news]

If the relationship has more details to it, e.g. a Person in the current team,
we need to do a bit more to grab those information::

    a_founder = who_started_github[0]
    cb.person(a_founder.permalink)

`permalink` is a special field on on an item in a relationship, this is the unique
CrunchBase identifier of that node.
