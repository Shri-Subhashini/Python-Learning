import pytest
import requests

# Auth Tests
def test_valid_api_key(base_url, api_key, default_city):
    params = {"q": default_city, "appid": api_key}
    response = requests.get(base_url, params=params)
    assert response.status_code == 200

def test_missing_api_key(base_url, default_city):
    params = {"q": default_city}  # No API key
    response = requests.get(base_url, params=params)
    assert response.status_code == 401

def test_invalid_api_key(base_url, default_city):
    params = {"q": default_city, "appid": "INVALID_KEY"}
    response = requests.get(base_url, params=params)
    assert response.status_code == 401
