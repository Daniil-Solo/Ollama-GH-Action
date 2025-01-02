import os
import requests
from github import Github, PullRequest


GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_NAME = os.environ.get("REPO_NAME")
PULL_NUMBER = int(os.environ.get("PULL_NUMBER"))

g = Github(login_or_token=GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)  # Login/Repo
pr = repo.get_pull(PULL_NUMBER)
with open("description.txt", "w", encoding="utf-8") as f:
    f.write(pr.body)
last_commit = pr.get_commits()[pr.commits - 1]
comments = []

for file in pr.get_files():
    file_url = file.blob_url
    resp = requests.get(file_url)
    file_content = resp.text
    new_comment = PullRequest.ReviewComment(path=file.filename, position=1, body=file_content)
    comments.append(new_comment)

pr.create_review(last_commit, "New answer" + pr.body, "REQUEST_CHANGES", comments)
