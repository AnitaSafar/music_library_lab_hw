import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Queen")

    def test_artist_has_name(self):
        self.assertEqual("Queen", self.artist.name)