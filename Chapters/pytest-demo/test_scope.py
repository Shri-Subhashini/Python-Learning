# test_valid_class_scope.py

import pytest

@pytest.fixture(scope="session")
def fixture_a():
    print("\n[fixture_a] setup")
    return "class-resource"

@pytest.fixture(scope="module")
def fixture_b(fixture_a):
    print("[fixture_b] setup using fixture_a:", fixture_a)
    return fixture_a + "-with-b"

class TestExample:
    def test_one(self, fixture_b):
        assert fixture_b == "class-resource-with-b"

    def test_two(self, fixture_b):
        assert fixture_b.startswith("class-resource")
