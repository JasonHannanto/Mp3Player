from songplayer import SongPlayer
from user import User

def main():

    username = raw_input("Enter your name: ")

    user = User(username)

    songplayer = SongPlayer(user)
    songplayer.menu()

main()