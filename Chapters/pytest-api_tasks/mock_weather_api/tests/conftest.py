import pytest
from src.weather_client import WeatherClient

@pytest.fixture(scope="session")
def base_url():
    return "https://mock.weatherapi.com"


@pytest.fixture
def weather_client(base_url):
    return WeatherClient(base_url)