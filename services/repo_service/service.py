from core.github_client import GitHubClient
from services.repo_service.models.repo_model import Repo

class RepoService:
    def __init__(self):
        self.client = GitHubClient()

    def get_repos(self, username):
        repo_data = self.client.get_repos(username)
        return [Repo(repo) for repo in repo_data]
