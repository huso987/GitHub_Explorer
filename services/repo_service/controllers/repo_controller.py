class RepoController:
    def __init__(self, service):
        self.service = service

    def fetch_repos(self, username):
        repos = self.service.get_repos(username)
        return [repo.__dict__ for repo in repos]
