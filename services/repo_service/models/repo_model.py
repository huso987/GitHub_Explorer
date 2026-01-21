class Repo:
    def __init__(self, data):
        self.name = data.get("name")
        self.language = data.get("language")
        self.stars = data.get("stargazers_count")
        self.url = data.get("html_url")
