import pytest

@pytest.mark.dependency(name = "one")
def test_one():
    pass
@pytest.mark.dependency(name = "two", depends = ["one"])
def test_two():
    assert 1 != 1
@pytest.mark.dependency(name = "done", depends = ["one"])
def test_three():
    print("three")