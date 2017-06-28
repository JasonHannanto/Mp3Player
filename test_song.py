import unittest
from song import Song

class Song_test(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Song1", "Artist1", "Genre1", "song1.mp3")

    def test_title(self):
        self.assertEqual(self.song1.name, "Song1")

    def test_artist(self):
        self.assertEqual(self.song1.artist, "Artist1")

    def test_genre(self):
        self.assertEqual(self.song1.genre, "Genre1")

    def test_location(self):
        self.assertEqual(self.song1.location, "song1.mp3")

    def test_rating(self):
        self.assertEqual(self.song1.rating, 0)

    def test_like(self):
        self.song1.set_rating(1)
        self.assertEqual(self.song1.rating, 1)

    def test_dislike(self):
        self.song1.set_rating(-1)
        self.assertEqual(self.song1.rating, -1)
