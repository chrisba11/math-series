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
            first = second
            second = next_num
    return next_num

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
