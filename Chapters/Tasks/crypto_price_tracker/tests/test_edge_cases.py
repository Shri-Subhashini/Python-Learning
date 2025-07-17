import pytest
from src.price_tracker import CryptoPriceTracker


def test_api_rate_limit(sample_tracker, mock_rate_limit):
    with pytest.raises(Exception, match="Rate limit exceeded"):
        sample_tracker.fetch_prices()

def test_invalid_coin(monkeypatch):
   

    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200
            def json(self):
                return {}
            def raise_for_status(self):
                pass
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    tracker = CryptoPriceTracker(["invalidcoin"])
    prices = tracker.fetch_prices()
    assert prices == {}
