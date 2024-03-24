from pymongo import MongoClient
import environment

class GameDatabase:
    def __init__(self):
        self.uri = environment.MONGO_URL
        self.db_name = environment.DATABASE_NAME
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.users_collection = self.db['users']

    def check_if_user_exists(self, user_name):
        """Check if the given username already exists in the database."""

        return self.users_collection.find_one({"user_name": user_name}) is not None

    def get_player_score(self, user_name):
        """Retrieve the score of the given username, if it exists."""

        user = self.users_collection.find_one({"user_name": user_name}, {"_id": 0, "score": 1})
        if user:
            return user.get('score', 0)  # Return 0 if 'score' is somehow missing
        else:
            return None  # Username does not exist

    def create_new_player(self, user_name):
        """Create a new player with the given username and an initial score of 0."""

        if not self.check_if_user_exists(user_name):
            self.users_collection.insert_one({"user_name": user_name, "score": 0})
            return True
        else:
            return False  # Username already exists

    def update_player_score(self, user_name, score):
        """Update the score of the existing player."""

        self.users_collection.update_one({"user_name": user_name}, {"$set": {"score": score}})

    def get_leaderboard(self):
        """Retrieve the top ten users and their scores."""
        top_players = self.users_collection.find().sort("score", -1).limit(10)
        return list(top_players)