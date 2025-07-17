# tests/conftest.py

import pytest
from unittest.mock import patch
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from testrail.testrail_api import add_result

@pytest.fixture
def valid_api_response():
    return {
        "name": "London",
        "main": {"temp": 21.0, "humidity": 60},
        "weather": [{"description": "light rain"}]
    }
    

@pytest.fixture
def patch_requests_get():
    with patch("app.weather.requests.get") as mock_get:
        yield mock_get


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

