import pytest
from testrail.testrail_api import add_result

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and "testrail_case_id" in item.keywords:
        case_id = item.get_closest_marker("testrail_case_id").args[0]

        if result.failed:
            add_result(case_id, status_id=5, comment="Test failed")
        elif result.passed:
            add_result(case_id, status_id=1, comment="Test passed")
