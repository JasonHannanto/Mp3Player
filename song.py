class Song(object):

    def __init__(self, name, artist, genre, location):

        self.name = name
        self.artist = artist
        self.genre = genre
        self.location = location
        self.rating = 0

        #RETURN SONG INFORMATION
        def name(self):
            return self.name
        def rating(self):
            return self.rating
        def artist(self):
            return self.artist
        def genre(self):
            return self.genre

    #RETURN FULL SONG DESCRIPTION
    def description(self):
        print("Title: {}".format(self.name))
        print("Artist: {}".format(self.artist))
        print("Genre: {}".format(self.genre))
        print("Rating: {}".format(self.rating))

    # SET RATINGS FOR SONGS (Like/Dislike)
    def set_rating(self, rating):
        self.rating = (rating)

        if (rating == 1):
            print ("You have liked the current song.")
        elif (rating == -1):
            print ("You have disliked the current song.")