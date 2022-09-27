from q3 import factorial


def series(x, n):
    result = 1

    for i in range(1, n):
        term = (x ** (2*i)) / factorial(2*i)
        if i % 2 == 0:
            result += term
        else:
            result -= term

    return result

print(series(1,3))