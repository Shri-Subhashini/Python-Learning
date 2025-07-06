# test_math.py
import pytest

@pytest.mark.testrail_case_id(3)
def test_add():
    assert 2 + 3 == 5

@pytest.mark.testrail_case_id(4)
def test_subtract():
    assert 5 - 2 == 3

@pytest.mark.testrail_case_id(5)
def test_multiply():
    assert 4 * 2 == 8

@pytest.mark.testrail_case_id(6)
def test_fail_case():
    assert 1 == 0
