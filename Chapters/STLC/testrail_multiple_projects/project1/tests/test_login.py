import pytest

@pytest.mark.testrail_case_id(7)
def test_valid_login():
    assert 1 == 1  # simulate passing test

@pytest.mark.testrail_case_id(9)
def test_invalid_login():
    assert 1 == 0  # simulate failing test
