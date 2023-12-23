# Код калькулятора
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


# Тесты с использованием Pytest
import pytest

# Позитивный тест для метода add
def test_add():
    calculator = Calculator()
    result = calculator.add(3, 5)
    assert result == 8

# Позитивный тест для метода subtract
def test_subtract():
    calculator = Calculator()
    result = calculator.subtract(8, 3)
    assert result == 5

# Позитивный тест для метода multiply
def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(4, 6)
    assert result == 24

# Позитивный тест для метода divide
def test_divide():
    calculator = Calculator()
    result = calculator.divide(10, 2)
    assert result == 5
