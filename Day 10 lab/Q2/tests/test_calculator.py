import pytest
from app.calculator import add, subtract, multiply, divide

# ---------- xUnit STYLE SETUP / TEARDOWN ----------
def setup_module(module):
    print("\n[SETUP MODULE] test_calculator_basic")

def teardown_module(module):
    print("\n[TEARDOWN MODULE] test_calculator_basic")

def setup_function(function):
    print("\n[SETUP FUNCTION]", function.__name__)

def teardown_function(function):
    print("\n[TEARDOWN FUNCTION]", function.__name__)


# ---------- TEST CASES ----------
def test_addition(numbers):
    a, b = numbers
    assert add(a, b) == 15


def test_subtraction(numbers):
    a, b = numbers
    assert subtract(a, b) == 5


def test_multiplication(numbers):
    a, b = numbers
    assert multiply(a, b) == 50


def test_division(numbers):
    a, b = numbers
    assert divide(a, b) == 2
