import pytest 

#Passing Tests

def test_addition():
    assert 3 + 2 == 5

def test_subtract():
    assert 7 - 3 == 4

def test_multiplication():
    assert 6 * 2 == 12

def test_division():
    assert 8 / 4 == 2

def test_string():
    assert "Welcome" + " " + "Subha!" == "Welcome Subha!"

def test_lowercase():
    assert "HeLlo".lower() == "hello"

def test_length():
    arr = [8, 4, 2, 0, 1, 3]
    assert len(arr) == 6

def test_sum():
    assert sum([1, 2, 3, 4]) == 10

#Failing Tests

def test_dictionary_value():
    user = {"name": "Subha", "age": 25}
    assert user["name"] == "Shri Subha"

def test_boolean():
    assert True and False == True


# Auto re-run
# pytest --reruns 2 --reruns-delay 1 -v

# Last failed
# pytest --lf

