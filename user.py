class User(object):

    def __init__(self, username, playlist = []):
        self.username = username
        self.playlist = playlist

    def return_username(self):
        return self.username

    def return_playlist(self):
        for song in self.playlist:
            print(song)