from core.github_client import GitHubClient
from services.user_service.models.user_model import User

class UserService:
    def __init__(self):
        self.client = GitHubClient()

    def get_user(self, username):
        user_data = self.client.get_user(username)
        return User(user_data)
