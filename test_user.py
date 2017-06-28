import unittest
from user import User

class User_Test(unittest.TestCase):

    def test_user(self):
        user = User("Jason")
        self.assertEqual(user.username, "Jason")

if __name__ == '__main__':
    unittest.main()
