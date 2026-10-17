def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base: float, exponent: float) -> float:
    return base ** exponent


def is_even(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return number % 2 == 0
