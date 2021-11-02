import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album("Hot Space", "pop rock", "Queen")

    def test_album_has_title(self):
        self.assertEqual("Hot Space", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("pop rock", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Queen", self.album.artist)
