# test_login_handler.py
import pytest
from unittest.mock import patch
import requests
from login_handler import login_user

# Test ConnectionError for invalid/missing endpoint

# It replaces the actual requests.post function with a mock object during the test.
# This is useful when testing code that makes HTTP requests—you can simulate responses or errors without actually calling a real API.

@patch("requests.post") 
def test_login_connection_error(mock_post):
    mock_post.side_effect = requests.exceptions.ConnectionError()
    payload = {"username": "admin", "password": "secret123"}

    result = login_user("http://invalid-api.com/login", payload)

    assert "error" in result
    assert result["error"] == "Connection failed: Endpoint not reachable."


# Test 404 Not Found scenario
@patch("requests.post")
def test_login_http_404(mock_post):
    mock_response = requests.Response()
    mock_response.status_code = 404
    mock_response.raise_for_status = lambda: (_ for _ in ()).throw(requests.exceptions.HTTPError("404 Not Found"))
    mock_post.return_value = mock_response

    payload = {"username": "admin", "password": "secret123"}
    result = login_user("http://localhost:5000/wrong-endpoint", payload)

    assert "error" in result
    assert "HTTP error" in result["error"]
    assert "404" in result["error"]
