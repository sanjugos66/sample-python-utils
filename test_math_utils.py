import pytest
from math_utils import add, divide

# Tests for add() function
def test_add_positive_numbers():
    assert add(1, 2) == 3
    assert add(10, 20) == 30

def test_add_negative_numbers():
    assert add(-1, -2) == -3
    assert add(-5, -10) == -15

def test_add_mixed_numbers():
    assert add(-1, 2) == 1
    assert add(5, -10) == -5

def test_add_with_zero():
    assert add(0, 5) == 5
    assert add(10, 0) == 10
    assert add(0, 0) == 0

# Tests for divide() function
def test_divide_positive_numbers():
    assert divide(10, 2) == 5
    assert divide(20, 4) == 5

def test_divide_negative_numbers():
    assert divide(-10, -2) == 5
    assert divide(-20, -4) == 5

def test_divide_mixed_numbers():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5

def test_divide_by_one():
    assert divide(10, 1) == 10
    assert divide(-5, 1) == -5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
