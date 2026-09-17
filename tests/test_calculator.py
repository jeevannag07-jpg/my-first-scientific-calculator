import pytest
from calculator import Calculator

calc = Calculator()

# ---- Basic operations ----

def test_add():
    assert calc.add(2, 3) == 5

def test_subtract():
    assert calc.subtract(5, 3) == 2

def test_multiply():
    assert calc.multiply(4, 3) == 12

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)

# ---- Scientific operations ----

def test_square_root():
    assert calc.square_root(9) == 3

def test_square_root_negative():
    with pytest.raises(ValueError):
        calc.square_root(-4)

def test_power():
    assert calc.power(2, 3) == 8

def test_factorial():
    assert calc.factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        calc.factorial(-3)

def test_factorial_non_integer():
    with pytest.raises(ValueError):
        calc.factorial(2.5)

def test_sine():
    assert round(calc.sine(90), 2) == 1.0  # sin(90°) = 1

def test_cosine():
    assert round(calc.cosine(0), 2) == 1.0  # cos(0°) = 1

def test_logarithm():
    assert round(calc.logarithm(1), 2) == 0.0  # log(1) = 0

def test_logarithm_zero():
    with pytest.raises(ValueError):
        calc.logarithm(0)

def test_logarithm_negative():
    with pytest.raises(ValueError):
        calc.logarithm(-5)
