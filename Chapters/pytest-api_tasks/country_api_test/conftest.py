import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://restcountries.com/v3.1/all"

@pytest.fixture(scope="session")
def all_countries(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200, "Status code is not 200"
    countries = response.json()