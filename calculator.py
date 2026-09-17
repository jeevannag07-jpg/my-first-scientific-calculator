import math

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

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)

    def power(self, a, b):
        return a ** b

    def factorial(self, a):
        if a < 0 or a != int(a):
            raise ValueError("Factorial only works for non-negative whole numbers")
        return math.factorial(int(a))

    def sine(self, a):
        return math.sin(math.radians(a))

    def cosine(self, a):
        return math.cos(math.radians(a))

    def logarithm(self, a):
        if a <= 0:
            raise ValueError("Logarithm undefined for zero or negative numbers")
        return math.log(a)