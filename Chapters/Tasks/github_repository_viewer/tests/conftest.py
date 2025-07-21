# tests/conftest.py
import pytest
import requests_mock
from testrail.testrail_api import add_result

@pytest.fixture
def sample_user():
    return {
        "login": "octocat",
        "name": "The Octocat",
        "followers": 100,
        "public_repos": 8
    }

@pytest.fixture
def sample_repos():
    return [
        {"name": "repo1", "stargazers_count": 10, "forks_count": 2, "language": "Python"},
        {"name": "repo2", "stargazers_count": 5, "forks_count": 1, "language": "JavaScript"},
        {"name": "repo3", "stargazers_count": 3, "forks_count": 0, "language": "Python"},
    ]

# Auto-hook for TestRail update
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        marker = item.get_closest_marker("testrail_case_id")
        if marker:
            case_id = marker.args[0]
            if call.excinfo is None:
                add_result(case_id, status_id=1, comment="Passed")
            else:
                add_result(case_id, status_id=5, comment=f"Failed: {call.excinfo.value}")
