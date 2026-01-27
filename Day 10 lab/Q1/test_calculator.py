import pytest
from calculator import add, subtract, multiply, divide

def test_addition():
    result = add(2, 3)
    print("Addition result:", result)
    assert result == 5

def test_subtraction():
    assert subtract(5, 2) == 3

def test_multiplication():
    assert multiply(4, 3) == 12

def test_division():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
