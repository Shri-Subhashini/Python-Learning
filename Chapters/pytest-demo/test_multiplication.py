import pytest

@pytest.mark.parametrize("num, output", [(1, 11), (2, 22),(3, 33), (4, 44), (5,5)])
def test_multiplication_11(num, output):
    assert 11*num == output