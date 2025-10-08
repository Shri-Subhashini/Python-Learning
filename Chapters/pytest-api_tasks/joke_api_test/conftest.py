import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://official-joke-api.appspot.com"