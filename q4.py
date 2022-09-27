
from re import L


def get_digits(n):
    assert n >= 10, "Number should be >= 10"
    # return set(str(n))

    digits = set()
    str_num = str(n)
    for digit in str_num:
        digits.add(int(digit))
    return digits


print(get_digits(34))