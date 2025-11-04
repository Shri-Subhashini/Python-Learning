import json
import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.api_client import APIClient


@pytest.fixture(scope="session")
def base_url():
    return "https://example.com/api"

@pytest.fixture(scope="session")
def user_data():
    with open("data/user_data.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def api_client(base_url):
    return APIClient(base_url)

@pytest.fixture(scope="session")
def register_user(api_client, user_data):
    response = api_client.registration_user(user_data["email"], user_data["password"])
    assert response.status_code in [200, 201], "User registration failed"
    return response


@pytest.fixture(scope = "session")
def login_user(api_client, user_data):
    response= api_client.login_user(user_data["email"], user_data["password"])
    assert response.status_code == 200, "Login failed"
    assert api_client.token is not None, "Token not stored after login"
    return response

@pytest.fixture(scope="session")
def auth_token(api_client, login_user):
    return api_client.token

