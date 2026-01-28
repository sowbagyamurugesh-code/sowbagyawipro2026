import pytest

# Parametrize example
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (10, 20, 30)
    ]
)
@pytest.mark.regression
def test_addition(a, b, expected):
    assert a + b == expected


# Skip example
@pytest.mark.skip(reason="Feature under development")
def test_skip_example():
    assert False


# XFail example
@pytest.mark.xfail(reason="Known bug: division by zero")
def test_xfail_example():
    result = 1 / 0
    assert result == 0
