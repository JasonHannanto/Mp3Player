def load_playlist(username):

    playlist = []

    with open("user_list.txt") as f:
        for line in f:
            if line.strip() == username:
                print("FOUND USERNAME")
                playlist = f.next().split(",")
                print playlist
                f.close()
                return playlist

    f.close()
    print("DIDNT RAN")
    return([])