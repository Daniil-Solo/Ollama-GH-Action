import os
from github import Github


GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_NAME = os.environ.get("REPO_NAME")
PULL_NUMBER = int(os.environ.get("PULL_NUMBER"))

g = Github(login_or_token=GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)  # Login/Repo
pr = repo.get_pull(PULL_NUMBER)
with open("description.txt", "w", encoding="utf-8") as f:
    f.write(pr.body)
pr.create_comment("New answer" + pr.body)
