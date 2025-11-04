import pytest


def test_register_user(register_user):
    data = register_user.json()
    assert "id" in data or "message" in data
    assert register_user.status_code in [200, 201]


def test_login_user(login_user):
    data = login_user.json()
    assert "token" in data, "No token in login response"
    assert login_user.status_code == 200


def test_access_profile(api_client, auth_token):
    response = api_client.get_profile()
    assert response.status_code == 200, "Profile access failed"
    data = response.json()
    assert "email" in data or "username" in data
    print(f"Profile:{data}")


def test_access_profile_without_token(api_client):
    api_client.token = None
    response = api_client.get_profile()
    assert response.status_code in [401, 403], "Unauthorized access allowed"

    
