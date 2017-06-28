from songplayer import SongPlayer
from user_load import *
from user import User
def main():

    username = raw_input("Enter your name: ")
    playlist = load_playlist(username)

    user = User(username, playlist)

    songplayer = SongPlayer(user)
    songplayer.menu()

main()