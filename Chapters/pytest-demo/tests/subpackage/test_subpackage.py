import pytest

@pytest.fixture
def innermost(order, mid):
    order.append("innermost subpackage")

def test_order(order, top):
    assert order == ["mid subpackage", "innermost subpackage", "top"]

 @pytest.fixture
def inner(order, mid, a_fix):
    order.append("inner subpackage")

def test_order(order, inner):
    assert order == ["b_fix", "mid subpackage", "a_fix", "inner subpackage"]