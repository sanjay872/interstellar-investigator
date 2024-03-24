import unittest
from database import GameDatabase

class TestGameDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Connect to the test database
        uri = 'mongodb+srv://hhu:hhu@interstellar-investigat.k1riaic.mongodb.net/'
        cls.db = GameDatabase(uri=uri, db_name='test_game_database')
    

    @classmethod
    def tearDownClass(cls):
        # Clean up the test database after all tests
        #cls.db.client.drop_database('test_game_database')
        pass

    def test_user_creation_and_checking(self):
        user_name = "test_user_8"
        # Ensure the user doesn't exist initially
        self.assertFalse(self.db.check_if_user_exists(user_name))

        # Create a new user and verify creation was successful
        self.assertTrue(self.db.create_new_player(user_name))

        # Check the user exists now
        self.assertTrue(self.db.check_if_user_exists(user_name))

        # Attempt to create the same user should fail
        self.assertFalse(self.db.create_new_player(user_name))

    def test_score_updating_and_retrieval(self):
        user_name = "test_user_2"
        initial_score = 0
        new_score = 200
        #self.db.create_new_player(user_name)
        # Retrieve initial score
        self.assertEqual(self.db.get_player_score(user_name), 200)

        # Update score
        self.db.update_player_score(user_name, new_score)

        # Check updated score
        self.assertEqual(self.db.get_player_score(user_name), new_score)
    
    def test_print_leaderboard(self):

        leaderboard = self.db.get_leaderboard()
       
        max_username_length = max(len(player['user_name']) for player in leaderboard) if leaderboard else 0
        for rank, player in enumerate(leaderboard, start=1):
            print(f"{rank}. {player['user_name']:{max_username_length}} - {player['score']}")
        

if __name__ == '__main__':
    unittest.main()
    