from series import fibonacci, lucas


def test_fib_n_at_1():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected


def test_fib_n_at_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fib_n_at_3():
    actual = fibonacci(3)
    expected = 1
    assert actual == expected


def test_fib_n_at_4():
    actual = fibonacci(4)
    expected = 2
    assert actual == expected


def test_fib_n_at_8():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected


def test_lucas_n_at_1():
    actual = lucas(1)
    expected = 2
    assert actual == expected


def test_lucas_n_at_2():
    actual = lucas(2)
    expected = 1
    assert actual == expected


def test_lucas_n_at_3():
    actual = lucas(3)
    expected = 3
    assert actual == expected


def test_lucas_n_at_4():
    actual = lucas(4)
    expected = 4
    assert actual == expected


def test_lucas_n_at_8():
    actual = lucas(8)
    expected = 29
    assert actual == expected


def test_both_n_at_1_0_1():
    actual = sum_series(1, 0, 1)
    expected = 0
    assert actual = expected


def test_both_n_at_6_0_1():
    actual = sum_series(6, 0, 1)
    expected = 5
    assert actual = expected


def test_both_n_at_10_0_1():
    actual = sum_series(10, 0, 1)
    expected = 34
    assert actual = expected


def test_both_n_at_1_2_1():
    actual = sum_series(1, 2, 1)
    expected = 2
    assert actual = expected


def test_both_n_at_6_2_1():
    actual = sum_series(6, 2, 1)
    expected = 11
    assert actual = expected


def test_both_n_at_10_2_1():
    actual = sum_series(10, 2, 1)
    expected = 76
    assert actual = expected


def test_both_n_at_1_4_9():
    actual = sum_series(1, 4, 9)
    expected = 13
    assert actual = expected


def test_both_n_at_6_4_9():
    actual = sum_series(6, 4, 9)
    expected = 57
    assert actual = expected


def test_both_n_at_10_4_9():
    actual = sum_series(10, 4, 9)
    expected = 390
    assert actual = expected


# 4, 9, 13, 22, 35, 57, 92, 149, 241, 390
