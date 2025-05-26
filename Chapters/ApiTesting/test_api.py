import os
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

# Fetch the GitHub API token from the environment
GITHUB_API_TOKEN = "QpwL5tke4Pnpja7X4"
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN environment variable is not set."

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    """
    Creates a Playwright APIRequestContext with predefined headers for API testing.
    """
    headers = {
        # GitHub API version header
        "Accept": "application/json",
        # Authorization header with the personal access token
        # "Authorization": f"token {GITHUB_API_TOKEN}",
    }
    # Create a new API request context with the base URL and headers
    request_context = playwright.request.new_context(
        base_url="https://reqres.in", extra_http_headers=headers
    )
    yield request_context
    # Dispose of the request context after the session ends
    request_context.dispose()

def test_users(api_request_context):
    new_repo = api_request_context.get("/api/users?page=2")
    import pdb;pdb.set_trace()
    assert new_repo.ok


#  dir(new_repo)  
# new_repo.status     
# 200
# new_repo.json()
