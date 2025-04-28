import pytest

def f():
    raise SystemExit(1)
    # raise ExceptionGroup(
    #     "Group message",
    #     [
    #         RuntimeError(),
    #     ],
    # )

def test_mytest():
    with pytest.raises(SystemExit):
        f()


# def test_exception_in_group():
#     with pytest.raises(ExceptionGroup) as excinfo:
#         f()
#     assert excinfo.group_contains(RuntimeError)
#     assert not excinfo.group_contains(TypeError)
    