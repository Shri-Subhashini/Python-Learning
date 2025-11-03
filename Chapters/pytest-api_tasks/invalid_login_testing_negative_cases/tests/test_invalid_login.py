import pytest
import requests

# Missing Email
# 401 Unauthorized

def test_missing_email(base_url, valid_credentials):
    payload = {"password": valid_credentials["password"]}
    response = requests.post(base_url, json = payload)  #json: The data is sent in the request body
    assert response.status_code == 401
    assert "error" in response.json()

# Missing Password

def test_missing_password(base_url, valid_credentials):
    payload = {"email": valid_credentials["email"]}
    response = requests.post(base_url, payload)
    assert response.status_code == 401
    assert "error" in response.json()


# Wrong Password

def test_wrong_password(base_url, valid_credentials):
    payload = {"email": valid_credentials["email"], "password": "wrongpassword"}
    response = requests.post(base_url, json = payload)
    assert response.status_code == 401
    assert "error" in response.json()


# Invalid email format

@pytest.mark.parametrize("email", ["invalidemail", "user@.com", "@domain.zom"])
def test_invalid_email_format(base_url, valid_credentials, email):
    payload = {"email": email, "password": valid_credentials["password"]}
    response = requests.post(base_url, json = payload)
    assert response.status_code == 401
    assert "error" in response.json()


# Blank email and password

def test_blank_email_password(base_url):
    payload = {"email": "", "password": ""}
    response = requests.post(base_url, json = payload)
    assert response.status_code == 401
    assert "error" in response.json()

# Extra fields in payload

def test_extra_fields(base_url, valid_credentials):
    payload = valid_credentials.copy() #Shallow copy: avoid modifying the original fixture (valid_credentials) in-place.
    payload["extra_field"] = "Hi"
    response = requests.post(base_url, json = payload)
    assert response.status_code in [200, 400, 401]
    assert "error" in response.json() or "token" in response.json()

#Numeric email

def test_numeric_email(base_url, valid_credentials):
    payload = {"email": 5678, "password": valid_credentials["password"]}
    response = requests.post(base_url, json = payload)
    assert response.status_code == 401
    assert "error" in response.json()

# SQL Injection

def test_sql_injection_email(base_url, valid_credentials):
    payload = {"email": "' OR 1=1 --", "password": valid_credentials["password"]}
    response = requests.post(base_url, json = payload)
    assert response.status_code in [403, 401]
    try:
        data = response.json()
        assert "error" in data
    except ValueError:
        assert response.text != ""


# Long strings

def test_long_strings(base_url, valid_credentials):
    payload = {
        "email": "a"*500 + "@test.com",
        "password": "p"*500
    }
    response = requests.post(base_url, json = payload)
    assert response.status_code == 401
    assert "error" in response.json()


# Wrong content type
# 415 Unsupported Media Type

def test_wrong_content_type(base_url, valid_credentials):
    payload = valid_credentials
    response = requests.post(base_url, data = payload)
    assert response.status_code in [400, 401, 415]