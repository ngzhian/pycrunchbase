from unittest import TestCase

from pycrunchbase import Video

TEST_DATA = {
    "type": "Video",
    "uuid": "6e11f9b6b0ef6bb94bb245e52eb24523",
    "properties": {
        "title": "Title",
        "service_name": "youtube",
        "url": "http://videourl",
        "created_at": 1398019105,
        "updated_at": 1398019105
    }
}


class VideoTestCase(TestCase):
    def test_video_built(self):
        video = Video(TEST_DATA)
        self.assertEqual(video.title, "Title")
        self.assertEqual(video.service_name, "youtube")
        self.assertEqual(video.url, "http://videourl")
        self.assertEqual(video.created_at, 1398019105)
        self.assertEqual(video.updated_at, 1398019105)

    def test_string(self):
        video = Video(TEST_DATA)
        str(video)
