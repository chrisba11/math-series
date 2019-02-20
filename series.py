"""

"""


def fibonacci(n):
    """

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
