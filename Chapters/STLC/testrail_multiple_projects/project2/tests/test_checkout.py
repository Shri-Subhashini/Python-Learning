import pytest

@pytest.mark.testrail_case_id(8)
def test_checkout_success():
    assert True

@pytest.mark.testrail_case_id(10)
def test_checkout_failure():
    assert False
