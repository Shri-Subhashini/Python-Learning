import pytest

@pytest.fixture
def mid(order):
    order.append("mid subpackage")

@pytest.fixture(autouse=True)
def mid(order, b_fix):
    order.append("mid subpackage")

@pytest.fixture
def b_fix(order):
    order.append("b_fix")

@pytest.fixture
def a_fix(order):
    order.append("a_fix")