import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            print("Before break")
            #f()
            return 
            
        f()
    assert "maximum recursion" in str(excinfo.value)


def test_foo_not_implemented():
    def foo():
        raise NotImplementedError

    with pytest.raises(RuntimeError) as excinfo:
        foo()
    assert excinfo.type is RuntimeError


# The main attributes of interest are .type, .value and .traceback.

def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


def test_exception_in_group_at_given_depth():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
                ExceptionGroup(
                    "Nested group",
                    [
                        TypeError(),
                    ],
                ),
            ],
        )
    assert excinfo.group_contains(RuntimeError, depth=1)
    assert excinfo.group_contains(TypeError, depth=2)
    assert not excinfo.group_contains(RuntimeError, depth=2)
    assert not excinfo.group_contains(TypeError, depth=1)