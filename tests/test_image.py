from unittest import TestCase

from pycrunchbase import Image

TEST_DATA = {
    "type": "Image",
    "uuid": "6e11f9b6b0ef6bb94bb245e52eb24523",
    "properties": {
        "asset_path": "path.jpg",
        "content_type": "image/jpeg",
        "height": 170,
        "width": 147,
        "filesize": 8837,
        "created_at": 1398019105,
        "updated_at": 1398019105
    }
}


class ImageTestCase(TestCase):
    def test_image_built(self):
        image = Image(TEST_DATA)
        self.assertEqual(image.asset_path, "path.jpg")
        self.assertEqual(image.content_type, "image/jpeg")
        self.assertEqual(image.height, 170)
        self.assertEqual(image.width, 147)
        self.assertEqual(image.filesize, 8837)
        self.assertEqual(image.created_at, 1398019105)
        self.assertEqual(image.updated_at, 1398019105)

    def test_string(self):
        image = Image(TEST_DATA)
        str(image)
