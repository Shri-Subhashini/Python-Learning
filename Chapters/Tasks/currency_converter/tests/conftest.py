import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from testrail.testrail_api import add_result


@pytest.fixture
def mock_conversion_response():
    return {
        "amount": 100,
        "base": "USD",
        "date": "2023-01-01",
        "rates": {
            "INR": 8300.0
        }
    }

@pytest.fixture
def mock_supported_currencies():
    return {"USD": "US Dollar", "INR": "Indian Rupee"}


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

