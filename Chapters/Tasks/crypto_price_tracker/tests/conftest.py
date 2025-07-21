import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from testrail.testrail_api import add_result



@pytest.fixture
def sample_tracker():
    from src.price_tracker import CryptoPriceTracker
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Step 1: Yield to let Pytest run its internal logic
    outcome = yield
    # Step 2: Get the real result object
    result = outcome.get_result()

    # Step 3: Process only actual test call results (not setup/teardown)
    if result.when == "call" and "testrail_case_id" in item.keywords:
        case_id = item.get_closest_marker("testrail_case_id").args[0]

        if result.failed:
            add_result(case_id, status_id=5, comment="Test failed")
        elif result.passed:
            add_result(case_id, status_id=1, comment="Test passed")

