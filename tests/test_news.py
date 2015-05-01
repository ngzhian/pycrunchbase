from unittest import TestCase
from datetime import datetime

from pycrunchbase import News

TEST_DATA = {
    "type": "News",
    "uuid": "3610c416c22e446380b3a4ef4b3c5fc1",
    "properties": {
        "title": "Title",
        "author": "Author",
        "posted_on": "2015-04-27",
        "url": "http://newsurl",
        "created_at": 1430157435,
        "updated_at": 1430157435
    }
}


class NewsTestCase(TestCase):
    def test_news_built(self):
        news = News(TEST_DATA)
        self.assertEqual(news.title, "Title")
        self.assertEqual(news.author, "Author")
        self.assertEqual(news.posted_on, datetime(2015, 4, 27))
        self.assertEqual(news.url, "http://newsurl")
        self.assertEqual(news.created_at, 1430157435)
        self.assertEqual(news.updated_at, 1430157435)

    def test_string(self):
        news = News(TEST_DATA)
        str(news)
