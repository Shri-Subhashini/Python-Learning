# src/github_api.py
import requests

def get_user_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_user_repos(username, per_page=5, page=1):
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page={per_page}&page={page}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
