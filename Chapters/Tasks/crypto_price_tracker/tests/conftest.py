import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



@pytest.fixture
def sample_tracker():
    from price_tracker import CryptoPriceTracker
    return CryptoPriceTracker(coins=["bitcoin", "ethereum", "dogecoin"])

@pytest.fixture
def mock_success_response(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200
            def json(self):
                return {
                    "bitcoin": {"usd": 31000},
                    "ethereum": {"usd": 2100},
                    "dogecoin": {"usd": 0.08}
                }
            def raise_for_status(self):
                pass
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

@pytest.fixture
def mock_rate_limit(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 429
            def raise_for_status(self): raise Exception("Rate limit exceeded")
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
