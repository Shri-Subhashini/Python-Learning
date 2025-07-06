import pytest
from auth import login

def test_login_success():
    assert login("admin", "admin123") == "Login successful"

def test_login_incorrect_password():
    assert login("admin", "subha123") == "Incorrect password"

def test_login_user_not_found():
    assert login("subha123", "admin123") == "User not found"

def test_login_empty_username():
    assert login("", "welcome") == "Username or password cannot be empty"

def test_login_empty_password():
    assert login("admin", "") == "Username or password cannot be empty"

