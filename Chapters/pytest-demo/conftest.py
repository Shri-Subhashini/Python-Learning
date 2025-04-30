
import pytest 
from test_own_exception_writing import Foo 


#Fixtures
@pytest.fixture
def input_value():
    input = 27
    return input


# Defining your own explanation for failed assertions
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            f"   vals: {left.val} != {right.val}",
        ]