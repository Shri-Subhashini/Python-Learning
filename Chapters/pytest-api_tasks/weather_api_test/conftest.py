import pytest
import os
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def base_url():
    return "https://api.openweathermap.org/data/2.5/weather"


@pytest.fixture(scope="session")
def api_key():
    load_dotenv()
    key = os.getenv("API_KEY")
    if not key:
        pytest.skip("API_KEY not found in environment variables")
    return key

@pytest.fixture(scope="session")
def default_city():
    load_dotenv()
    return os.getenv("CITY", "London")





