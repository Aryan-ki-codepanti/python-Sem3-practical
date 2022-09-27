
from cgitb import reset


def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fib_fac(n):
    result = [fibonacci(n), factorial(n)]
    return result


