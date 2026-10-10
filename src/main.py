def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def power(base, exponent):
    """Return the base raised to the power of the exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("base and exponent must be numbers.")
    return base ** exponent


def multipy(a,b):
    return a*b

def divide(a, b):
    return a / b
