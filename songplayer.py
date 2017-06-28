from pygame import *
from song import Song
from user import User

class SongPlayer(object):

    def __init__(self, user):

        self.raw_songlist = self.data_input("song_list.txt")
        self.songlist = self.import_song(self.raw_songlist)
        self.user = user
        self.playlist = user.playlist
        self.currentsong = self.songlist[0]
        self.currentposition = 0

    # IMPORTS DATA FROM TEXT FILE
    def data_input(self, raw_songlist):

        line = []

        with open(raw_songlist) as f:
            for inputs in f:
                inputs = inputs.replace('\n', "")
                line.append(inputs)
        f.close()

        return (line)

    # CREATES LIST OF SONG OBJECTS FROM RAW DATA
    def import_song(self, raw_songlist):

        songs = []

        for line in raw_songlist:
            name, artist, genre, location = line.split(",")
            current_song = Song(name, artist, genre, location)
            songs.append(current_song)

        return (songs)

    # SEARCH BY NAME
    def search_by_name(self):

        searchword = raw_input("Enter Song Name: ")

        for songs in self.songlist:
            if searchword in songs.name:
                validchoice = False

                while (validchoice == False):
                    print("{} is in the song database.".format(songs.name))
                    print("1 - Add as current song")
                    print("2 - Add to playlist")
                    print("3 - Cancel")
                    choice = int(raw_input("--------"))

                    if choice == 1:
                        validchoice = True
                        self.currentsong = songs
                    elif choice == 2:
                        validchoice = True
                        self.playlist.append(songs)
                    elif choice == 3:
                        validchoice = True
                        break
                    else:
                        print("Not a valid choice.")
            else:
                "Song not found!"

    # SEARCH BY ARTIST
    def search_by_artist(self):
    
        searchword = raw_input("Enter Artist Name: ")

        for songs in self.songlist:
            if searchword in songs.artist:
                validchoice = False

                while (validchoice == False):
                    print("{} by {} is in the song database.".format(songs.name,songs.artist))
                    print("1 - Add as current song")
                    print("2 - Add to playlist")
                    print("3 - Cancel")
                    choice = int(raw_input("--------"))

                    if choice == 1:
                        validchoice = True
                        self.currentsong = songs
                    elif choice == 2:
                        validchoice = True
                        self.playlist.append(songs)
                    elif choice == 3:
                        validchoice = True
                        break
                    else:
                        print("Not a valid choice.")
        else:
            print("Artist not found!")

    # ADD SONG TO PLAYLIST
    def add_to_playlist(self, song):

        self.playlist.append(song)
        return self.playlist

    # PLAY CURRENT SONG
    def play(self, currentsonglocation):

        mixer.init()
        mixer.music.load("src/" + currentsonglocation)
        mixer.music.play()

        print("Now Playing: {}").format(self.currentsong.name)

        action = 0
        action = int(raw_input("Press 1 to Stop: "))

        # Continues untill user enters 1
        while (action != 1):
            time.Clock().tick(10)

        mixer.music.stop()

    # SKIP SONG
    def skip_song(self):
        if(self.currentposition + 1 < len(self.songlist)):
            self.currentposition = self.currentposition + 1
            self.currentsong = self.songlist[self.currentposition]
        else:
            print("No more songs!")

    # PRINT MENU
    def menu(self):
        valid_input = False
        exit = False

        while (valid_input == False and exit == False):

            print("-" * 50)
            print("{}'s Music Player".format(self.user.username))
            print("-" * 50)
            print("Current Song: {}").format(self.currentsong.name)
            self.currentsong.description()
            print("-" * 50)
            print("1: Search Song by Title ")
            print("2: Search Song by Artist")
            print("3: Skip to next song")
            print("4: Like current Song")
            print("5: Dislike current Song")
            print("6: Add current Song to Playlist")
            print("7: Remove current Song from Playlist")
            print("8: Show Song Database")
            print("9: Show Playlist")
            print("10: Play Current Song")
            print("11: Exit")
            print("-" * 50)
            choice = int(raw_input("Enter your action: "))
            print("-" * 50)
            print("Action Performed:")

            # SEARCH FOR A SPECIFIC SONG NAME
            if (choice == 1):
                validInput = True
                self.search_by_name()

            # SEARCH FOR A SPECIFIC ARTIST
            elif (choice == 2):
                validInput = True
                self.search_by_artist()
            # SKIP SONG
            elif (choice == 3):
                validInput = True
                self.skip_song()

            # LIKE
            elif (choice == 4):
                validInput = True

                if(self.currentsong.rating == 1):
                    print("You already liked this song!")

                else:
                    self.currentsong.set_rating(1)
            # DISLIKE
            elif (choice == 5):
                validInput = True

                if (self.currentsong.rating == -1):
                    print("You already liked this song!")

                else:
                    self.currentsong.set_rating(-1)

            # ADD TO PLAYLIST
            elif (choice == 6):
                validInput = True

                if(self.currentsong in self.playlist):
                    print("{} is already in your playlist".format(self.currentsong.name))
                else:
                    self.playlist.append(self.currentsong)
                    print("{} added to playlist!".format(self.currentsong.name))

            # REMOVE FROM PLAYLIST
            elif (choice == 7):
                validInput = True

                if len(self.playlist) == 0:
                    print("No songs in playlist to remove")

                elif self.currentsong in self.playlist:
                    self.playlist.remove(self.currentsong)
                    print("{} removed from playlist.").format(self.currentsong.name)

                else:
                    print("Current song is not in the playlist")

            # PRINT SONG DATABASE
            elif (choice == 8):
                validInput = True
                print("Current Songs:")
                for x in xrange(0, len(self.songlist)):
                    print(self.songlist[x].name + " - " + self.songlist[x].artist)

            # PRINT PLAYLIST
            elif (choice == 9):
                validInput = True

                if (len(self.playlist) == 0):
                    print("You have not added any songs to your playlist yet!")
                else:
                    print ("Playlist: ")
                    for songs in self.playlist:
                        print (songs.name)

            # PLAY CURRENT SONG
            elif (choice == 10):
                validInput = True
                self.play(self.currentsong.location)

            # EXIT
            elif (choice == 11):
                validInput = True
                exit = True
                print("See you later!")
            else:
                print("Invalid Input")