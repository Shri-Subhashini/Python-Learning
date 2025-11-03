import pytest

@pytest.fixture(scope = "session")
def base_url():
    return "https://reqres.in/api/login"


@pytest.fixture(scope = "session")
def valid_credentials():
    return {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }