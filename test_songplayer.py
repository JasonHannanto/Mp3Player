import unittest
from songplayer import SongPlayer
from user import User

class SongPlayer_test(unittest.TestCase):

    def setUp(self):
        self.player = SongPlayer("Jason")
        self.raw_songlist = self.player.data_input("song_list.txt")
        self.songlist = self.player.import_song(self.raw_songlist)
        self.playlist = []
        self.currentsong = self.songlist[0]
        self.currentposition = 0

    def test_create_songplayer(self):
        self.assertEqual(self.player.username, "Jason")

    def test_adding_to_playlist(self):
        self.player.add_to_playlist("song1")
        self.assertEqual(self.player.playlist, ["song1"])

    def test_skip_song(self):
        self.player.skip_song()
        self.assertEqual(self.player.currentposition, 1)

if __name__ == '__main__':
    unittest.main()
