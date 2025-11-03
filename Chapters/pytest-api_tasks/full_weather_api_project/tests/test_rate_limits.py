import pytest
import requests
import time

# Rate Limiting and Retry Logic Tests
def test_rate_limit(base_url, api_key, default_city):
    params = {"q": default_city, "appid": api_key}
    failed = 0
    for i in range(70):  # Exceed limit of 60/min
        response = requests.get(base_url, params=params)
        if response.status_code == 429:
            failed += 1
            time.sleep(1)  # wait and retry
    assert failed == 0, "No 429 errors detected even after exceeding limit"
