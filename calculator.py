import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        return "Error: Invalid input for logarithm."
    except ZeroDivisionError:
        return "Error: Logarithm base cannot be zero."
    
def exp(a, b):
    return a ** b

