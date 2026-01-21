import requests
from core.config import Config
from core.exceptions import GitHubAPIException

class GitHubClient:
    def __init__(self):
        self.base_url = Config.GITHUB_API_URL

    def _get(self, endpoint):
        response = requests.get(
            f"{self.base_url}{endpoint}",
            timeout=Config.REQUEST_TIMEOUT
        )

        if response.status_code != 200:
            raise GitHubAPIException(
                f"GitHub API Error: {response.status_code}"
            )

        return response.json()

    def get_user(self, username):
        return self._get(f"/users/{username}")

    def get_repos(self, username):
        return self._get(f"/users/{username}/repos")
