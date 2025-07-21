# # tests/test_repos.py
# import pytest
# from src.github_api import get_user_repos

# @pytest.mark.testrail_case_id(15)
# def test_get_user_repos_pagination(requests_mock, sample_repos):
#     username = "octocat"
#     url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=5&page=1"
#     requests_mock.get(url, json=sample_repos)

#     repos = get_user_repos(username, per_page=5, page=1)
#     assert len(repos) == 3
#     assert repos[0]["name"] == "repo1"


import pytest
from src.github_api import get_user_repos
import requests_mock

@pytest.mark.testrail_case_id(18)
def test_get_user_repos_pagination(sample_repos):
    username = "octocat"
    with requests_mock.Mocker() as m:
        m.get(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=5&page=1", json=sample_repos)
        repos = get_user_repos(username, per_page=5, page=1)
        assert len(repos) == 3

