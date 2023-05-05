# Class User
class User:
    def __init__(self, username):
        self.username = username
    
    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username

# Class Game 
class Game:
    def __init__(self, users):
        self.sessionid = uuid.uuid4()
        self.users = users
    
    def get_sessionid(self):
        return self.sessionid

    def get_users(self):
        return self.users
    
    def add_users(self, users):
        self.users = self.users + users
        return

# Specification of game sessions
game_sessions = {}
