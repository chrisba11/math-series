"""
These are functions that create a sequence by adding the first number to the
second number and then adding the third number to the second, and so on.
"""


def fibonacci(n):
    """
    This function assumed the first number is 0 and the second number is 1.

    fibonacci(nth number in sequence you want returned)
    """
    first = 0
    second = 1
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(n - 2):
            next_num = first + second
            first, second = second, next_num
    return next_num

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...


def lucas(n):
    """
    This function assumes the first number is 2 and the second number is 1.

    lucas(nth number in sequence you want returned)
    """
    first = 2
    second = 1
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(n - 2):
            next_num = first + second
            first, second = second, next_num
    return next_num

# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76 ...


def sum_series(n, first=0, second=1):
    """
    This function accepts up to three arguments. The first arg is the number
    of the sequence you would like to return. The second and third args are
    optional, where the second arg is the first number in the sequence and the
    third arg is the second number in the sequence.

    The second arg will default to 0 if not supplied.
    The third arg will default to 1 if not supplied.

    sum_series(nth number in sequence you want returned,
    [first num in sequence], [second num in sequence])
    """
    first = first
    second = second
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(n - 2):
            next_num = first + second
            first, second = second, next_num
    return next_num

# 4, 9, 13, 22, 35, 57, 92, 149, 241, 390
