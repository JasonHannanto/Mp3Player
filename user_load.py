from user import User

def load_users(username):
    with open("user_list.txt") as f:
        for line in f:
            if username == line:
                return(True)
    f.close
    return(False)