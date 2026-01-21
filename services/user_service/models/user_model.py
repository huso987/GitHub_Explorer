class User:
    def __init__(self, data):
        self.username = data.get("login")
        self.avatar_url = data.get("avatar_url")
        self.followers = data.get("followers")
        self.following = data.get("following")
        self.public_repos = data.get("public_repos")
