import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    """Test that the add function works correctly."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    """Test that the subtract function works correctly."""
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(0, 0) == 0


def test_multiply():
    """Test that the multiply function works correctly."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


def test_divide():
    """Test that the divide function works correctly."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3


def test_divide_by_zero():
    """Test that dividing by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
