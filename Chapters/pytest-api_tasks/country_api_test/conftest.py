import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://restcountries.com/v3.1/all"