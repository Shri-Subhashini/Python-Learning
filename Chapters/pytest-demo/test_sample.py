import warnings

import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4, "value should be 4"

def test_modulo():
    assert 4 % 2 == 0, "value was odd, should be even"


def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("my warning", UserWarning)

# pytest.warns(UserWarning) is a context manager that checks whether a UserWarning is raised inside the with block.
# warnings.warn("my warning", UserWarning) issues a UserWarning.
# If the correct warning is triggered, the test passes.
# If no warning or a different type of warning is raised, the test fails.

def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2

# pytest test_sample.py::test_set_comparison












# import argparse

# def main():
#     parser = argparse.ArgumentParser("My Program")
#     parser.add_argument("--data", nargs=1, help="sdfsadfsafdsadfa")

#     args = parser.parse_args()
#     print(args.data)

# main()