# # tests/test_users.py
# import pytest
# from src.github_api import get_user_profile

# @pytest.mark.testrail_case_id(17)
# def test_get_user_profile_success(requests_mock, sample_user):
#     username = "octocat"
#     url = f"https://api.github.com/users/{username}"
#     requests_mock.get(url, json=sample_user)

#     user = get_user_profile(username)
#     assert user["login"] == "octocat"
#     assert user["name"] == "The Octocat"


import pytest
from src.github_api import get_user_profile
import requests_mock

@pytest.mark.testrail_case_id(19)
def test_get_user_profile_success(sample_user):
    username = "octocat"
    with requests_mock.Mocker() as m:
        m.get(f"https://api.github.com/users/{username}", json=sample_user)
        user = get_user_profile(username)
        assert user["login"] == "octocat"
        assert user["name"] == "The Octocat"
