import pytest

@pytest.mark.xfail   #=> If did'nt meantion , error will come and mention as 1 failure; if mention, warning will come and mention as 1 xfailed
@pytest.mark.great

def test_greater():
    num = 100
    assert num > 100
# pytest test_compare.py -m great

@pytest.mark.xfail
@pytest.mark.great

def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.skip   # Skip the test entirely.
@pytest.mark.others  # Custom marks

def test_less():
    num = 100
    assert num < 200

#  @pytest.mark.skipif   #  Conditionally skip a test based on some logic.
import sys

@pytest.mark.skipif(sys.platform != 'win32', reason = "Only runs on Window")
def test_windows_only():
    assert True

# python -m pytest test_compare.py   - can run like this also. Now python runs from parent directory
# But pytest runs from current directory only