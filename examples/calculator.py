def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result.

    Raises:
        ZeroDivisionError: If b is 0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
