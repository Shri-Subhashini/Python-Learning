import pytest
from config.config import BASE_URL, API_KEY, DEFAULT_CITY
import csv

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def api_key():
    return API_KEY

@pytest.fixture(scope="session")
def default_city():
    return DEFAULT_CITY

@pytest.fixture(scope="session")
def load_cities():
    data = []
    with open("data/cities.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((row["city"], int(row["expected_status"]), row["unit"]))
    return data
