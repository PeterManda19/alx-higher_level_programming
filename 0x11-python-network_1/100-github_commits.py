#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <repository owner>")
        sys.exit(1)
        
    repo_name, repo_owner = sys.argv[1], sys.argv[2]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    try:
        r = requests.get(url)
        r.raise_for_status()
        commits = r.json()
        for commit in commits[:10]:
            sha = commit["sha"]
            author = commit["commit"]["author"]["name"]
            print(f"{sha}: {author}")
    except requests.HTTPError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
